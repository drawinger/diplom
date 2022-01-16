from pathlib import Path
from functools import partial
from io import DEFAULT_BUFFER_SIZE
import re, struct
import data_types as tp
from collections import namedtuple
import numpy as np

dynamic_ids = [b'~~', b'SI', b'AN', b'rc', b'pc', b'RC', b'PC', b'NN', b'EL', b'AZ']

id_mapping = {
    b'~~': namedtuple('RT', ['id', 'len', 'tod', 'cs']),
    b'AN': namedtuple('AN', ['id', 'len', 'channel', 'cs']),
    b'SI': namedtuple('SI', ['id', 'len', 'usi', 'cs']),
    b'RC': namedtuple('RC', ['id', 'len', 'pr', 'cs']),
    b'PC': namedtuple('PC', ['id', 'len', 'cp', 'cs']),
    b'rc': namedtuple('rc', ['id', 'len', 'spr', 'cs']),
    b'pc': namedtuple('pc', ['id', 'len', 'scp', 'cs']),
    b'GE': namedtuple('GE', ['id', 'len', 'sv', 'tow', 'flags', 
                             'iodc', 'toc', 'ura',
                             'healthS', 'wn', 'tgd', 
                             'af2', 'af1', 'af0', 'toe', 
                             'iode', 'rootA', 'ecc', 'm0', 
                             'omega0', 'inc0', 'argPer', 
                             'deln', 'omegaDot', 'incDot', 
                             'crc', 'crs', 'cuc', 'cus', 'cic', 'cis', 'cs']),
    b'NE': namedtuple('NE', ['id', 'len', 'sv', 'frqNum', 'dne',
                             'tk', 'tb', 'health', 'age', 'flags',
                             'rx', 'ry', 'rz', 'vx', 'vy', 'vz', 'wx', 'wy', 'wz',
                             'tauSys', 'tau', 'gamma', 'cs']),
    b'NE88': namedtuple('NE', ['id', 'len', 'sv', 'frqNum', 'dne',
                             'tk', 'tb', 'health', 'age', 'flags',
                             'rx', 'ry', 'rz', 'vx', 'vy', 'vz', 'wx', 'wy', 'wz',
                             'tauSys', 'tau', 'gamma','fDelTauN', 'nFt', 'nN4', 'flags2', 'cs']),
    b'PV': namedtuple('PV', ['id', 'len', 'x', 'y', 'z', 'pSigma', 'vx', 'vy', 'vz', 'vSigma', 'solType', 'cs']),
    b'GT': namedtuple('GT', ['id', 'len', 'tow', 'wn', 'cs']),
    b'NN': namedtuple('GT', ['id', 'len', 'osn', 'cs']),
    b'UO': namedtuple('UO', ['id', 'len', 'a0','a1','tot','wnt','dtls','dn','wnlsf','dtlsf', 'cs']),
    b'NT': namedtuple('NT', ['id', 'len', 'tod', 'dn', 'cs']),
    b'EL': namedtuple('EL', ['id', 'len', 'elev', 'cs']),
    b'AZ': namedtuple('AZ', ['id', 'len', 'azim', 'cs']),
}


def gln_coord(time, dtls, NE, PDj):
    
    [sv, frqNum, dne,
    tk, tb, health, age, flags,
    rx, ry, rz, vx, vy, vz, wx, wy, wz,
    tauSys, tau, gamma] = NE[2:-1]

    Tj = (time - PDj - dtls) % 604800

    T_mdv = Tj + tau - gamma * (Tj - tb) + tauSys

    mu = 398600.44
    Re = 6378.136
    C20 = -1082.63e-6
    Wz = 0.7292115e-4#/(2*np.pi)

    def f(arg):
        r = np.sqrt(arg[0]**2 + arg[1]**2 + arg[2]**2)
        A = mu/(r**3)
        return np.array([
        arg[3],
        arg[4],
        arg[5],
        (Wz**2 - A)*arg[0] + 2*Wz*arg[4] + (3/2)*C20*((mu*Re**2)/r**5)*arg[0]*(1 - (5*arg[2]**2)/r**2) + wx,
        (Wz**2 - A)*arg[1] - 2*Wz*arg[3] + (3/2)*C20*((mu*Re**2)/r**5)*arg[1]*(1 - (5*arg[2]**2)/r**2) + wy,
        (-A)*arg[2] + (3/2)*C20*((mu*Re**2)/r**5)*arg[2]*(3 - (5*arg[2]**2)/r**2) + wz  
    ])

    def rungekut(s,h):
        arg = s
        k1 = h * f(arg)
        arg = s + 0.5 * k1
        k2 = h * f(arg)
        arg = s + 0.5 * k2
        k3 = h * f(arg)
        arg = s + k3
        k4 = h * f(arg)
        ds = (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        return s+ds   

    if T_mdv < 0:
        T_mdv += 86400

    S,tt = [[rx, ry, rz, vx, vy, vz]],[]

    t_s,t_e = tb, T_mdv
    if tb < T_mdv:
        h = 60
    else:
        h = -60 

    while t_s != t_e:
        if abs(t_e - t_s) < abs(h):
            h = t_e - t_s
        t_s += h
        #tt.append(h)
        S.append([*rungekut(np.array(S[-1]),h)])
    X,Y,Z,vX,vY,vZ = S[-1]
    return X*1e3,Y*1e3,Z*1e3 

def gps_coord(time, GE, PDj):
    
    [sv, tow, flags, 
     iodc, toc, ura,
     healthS, wn, tgd, 
     af2, af1, af0, toe, 
     iode, rootA, ecc, m0, 
     omega0, inc0, argPer, 
     deln, omegaDot, incDot, 
     crc, crs, cuc, cus, cic, cis] = GE[2:-1]

    N_days_of_week =  int(tow / 86400 )
    # текущ время приемника, взял из эфемериД, вроде герко говорил шо то ж самое
    sys_time = time + 86400 * N_days_of_week
    # pdj - псевдозадержка, посчитал заранее
    Tj = (sys_time - PDj) % 604800

    m0 = (m0)*np.pi
    omega0 = omega0*np.pi
    inc0 = inc0*np.pi
    argPer = argPer*np.pi
    deln = deln*np.pi
    omegaDot = omegaDot*np.pi
    incDot = incDot*np.pi

    c=299792458.
    omega3 = 7.2921151467e-5
    rootM = 1.996498184322e7
    C = -2*(rootM/(c**2))

    Tsys = Tj
    n0 = (rootM)/(rootA ** (3))
    n = n0 + deln
    tk = Tsys - toe
    Mk = m0 + n * tk
    dTr = C * ecc * rootA * np.sin(Mk)
    dTj = af0 + af1 * (Tsys - toc) + af2 * (Tsys - toc) ** 2 - tgd + dTr

    Ekn = Mk
    Ekj = Ekn - (Ekn - ecc * np.sin(Ekn) - Mk) / (1 - ecc * np.cos(Ekn))
    for i in range(10):
    #while (np.abs( Ekj[0] - Ekn[0] ) < 1e-9):
        Ekn = Ekj
        Ekj = Ekn - (Ekn - ecc * np.sin(Ekn) - Mk) / (1 - ecc * np.cos(Ekn))

    tettAk = np.arctan2((np.sqrt(1 - ecc ** 2) * np.sin(Ekj)),(np.cos(Ekj) - ecc))# * (180/np.pi)
    Fik = tettAk + argPer
    dUk = cuc * np.cos(2 * Fik) + cus * np.sin(2 * Fik)
    Uk = Fik + dUk
    drk = crc * np.cos(2 * Fik) + crs * np.sin(2 * Fik)
    rk = (rootA ** 2) * (1 - ecc * np.cos(Ekj)) + drk
    Vrk = (rootM * ecc * np.sin(tettAk))/(rootA * np.sqrt(1 - ecc ** 2))
    Vuk = (rootM * (1 + ecc * np.cos(tettAk)))/(rootA * np.sqrt(1 - ecc ** 2))
    dik = cic * np.cos(2 * Fik) + cis * np.sin(2 * Fik)
    ik = inc0 + dik + incDot * tk
    omegak = omega0 + (omegaDot - omega3) * tk - omega3 * toe

    X = rk * ( np.cos(Uk) * np.cos(omegak) - np.sin(Uk) * np.sin(omegak) * np.cos(ik) ) 
    Y = rk * ( np.cos(Uk) * np.sin(omegak) + np.sin(Uk) * np.cos(omegak) * np.cos(ik) ) 
    Z = rk * np.sin(Uk) * np.sin(ik)    
    
    return X,Y,Z

def file_byte_iterator(path):
    """given a path, return an iterator over the file
    that lazily loads the file
    """
    path = Path(path)
    with path.open('rb') as file:
        reader = partial(file.read1, DEFAULT_BUFFER_SIZE)
        file_iterator = iter(reader, bytes())
        for chunk in file_iterator:
            for byte in chunk:
                yield byte
                
def get_epoch_array(data):
    epoch_header = b'([~~]{2})([0-9a-zA-Z]{3})(.*)'
    match = next(re.finditer(epoch_header, data))
    epoch_start = match.start()

    records, count = [], 0

    idx = epoch_start
    while idx != len(data):
        # EOF check
        if idx == len(data)-1:
            #print('end of file reached')
            break

        # skip newline symbols
        while chr(data[idx]) in ['\n','\r']:
            idx += 1

        # get header
        id, length_raw = struct.unpack('2s3s', data[idx:idx+5])
        length = int(length_raw, 16)
        idx += 5

        # get body
        data_bytes = bytes(data[idx: idx+length])
        idx += length

        # make record
        record = {
            'id': id,
            'len': length,
            'data': data_bytes
        }  
        records.append(record)

    epoch_array, epoch = [], []
    for rec in records:
        if rec['id'] == b'~~':
            if len(epoch) > 0:
                epoch_array.append(epoch.copy())
                epoch.clear()
        epoch.append(rec)
    return epoch_array

def filter_epoch(req_ids, epoch):
    check_id = lambda record: record['id'] in req_ids
    return [*filter(check_id, epoch)]

def general_parser(record):
    id = record['id']
    len = record['len']
    if record['id'] in tp.fixed_masks.keys():
        if id == b'GE': 
            data = struct.unpack(tp.mask(id), record['data'][:123])
        elif id == b'NE':
            data = struct.unpack(tp.mask(id), record['data'][:80])
        else:
            data = struct.unpack(tp.mask(id), record['data'])
#    elif record['id'] == b'NE':
#        data = struct.unpack(tp.mask(id, len), record['data'])
    else:
        data = struct.unpack(tp.mask(id, len), record['data'])
    return (id, len, *data)

def map_rec(parsed_record):
    id = parsed_record[0]
    if id in dynamic_ids:
        return id_mapping[id](*parsed_record[:2],parsed_record[2:-1],parsed_record[-1])
    else:
        return id_mapping[id](*parsed_record)

def Uchet(X,Y,Z,x,y,z):
    c=299792458.
    omega3 = 7.2921151467e-5
    fR = lambda xr,yr,zr: np.sqrt((xr)**2+(yr)**2+(zr)**2)
    Rr = fR(X-x, Y-y, Z-z)
    tau = Rr / c
    alpha = omega3 * tau
    Xm = X + alpha*Y
    Ym = Y - alpha*X
    Zm = Z
    return Xm, Ym, Zm
