a1,i1,i2,i4,u1,u2,u4,f4,f8 = 's','b','h','i','B','H','I','f','d'

fixed_types = {
    b'~~': [u4, u1],
    b'||': [u1],
    b'ET': [u4, u1],
    b'RD': [u2, u1, u1, u1, u1],
    b'TO': [f8, f8, u1],
    b'DO': [f4, f4, u1],
    b'BP': [f4, u1],
    b'GT': [u4, u2, u1],
    b'GO': [f8, f8, u1],
    b'NT': [u4, u2, u1],
    b'NO': [f8, f8, u1],
    b'EO': [f8, f8, u1],
    b'WO': [f8, f8, u1],
    b'QO': [f8, f8, u1],
    b'CO': [f8, f8, u1],
    b'Io': [f8, f8, u1],
    b'UO': [f8, f4, u4, u2, i1, i1, u2, i1, u1],
    b'WU': [f8, f4, u4, u2, i1, i1, u2, i1, i1, u4, u2, u1, u1],
    b'EU': [f8, f4, u4, u2, i1, i1, u2, i1, f4, f4, u4, u2, u2, u1],
    b'QU': [f8, f4, u4, u2, i1, i1, u2, i1, u1],
    b'CU': [f8, f4, u4, u2, i1, i1, u2, i1, u1],
    b'IU': [f8, f4, u4, u2, i1, i1, u2, i1, u1],
    b'NU': [f8, f4, f4, f4, u1, u1, i2, i2, u1],

    b'ST': [u4, u1, u1],
    b'PO': [f8, f8, f8, f4, u1, u1],
    b'Po': [f8, f8, f8, f4, u1, u1, a1, a1, a1, a1, a1, u1],
    b'VE': [f4, f4, f4, f4, u1, u1],
    b'PV': [f8, f8 ,f8 ,f4, f4, f4, f4, f4, u1, u1],
    b'PG': [f8, f8, f8, f4, u1, u1],
    b'Pg': [f8, f8, f8, f4, u1, u1, a1, a1, a1, a1, a1, u1],
    b'VG': [f4, f4, f4, f4, u1, u1],
    b'SG': [f4, f4, f4, f4, u1, u1],
    b'mp': [f8, f8, f8, f8, f4, u1, u1, u1, u2, u1],
    b'bp': [f8, f8, f8, f8, f4, u1, u1, u1, u2, u1],
    b'DP': [f4, f4, f4, u1, f4, u1],
    b'SP': [f4, f4, f4, f4, f4, f4, f4, f4, f4, f4, u1, u1],
    b'SV': [f4, f4, f4, f4, f4, f4, f4, f4, f4, f4, u1, u1],
    b'BL': [f8, f8, f8, f4, u1, i4, u1],
    b'bL': [f4, f4, f4, f4, f4, f4, f4, f4, f4, f4, f4, f4, u1, u1, u1, u1],
    b'mR': [f4, f4, f4, f4, f4, f4, f4, f4, f4, u1],
    b'PS': [u1, u1, u1, u1, u1, u1, u1, u1, u1],
    b'PT': [u4, u1],
    b'UO': [f8, f4, u4, u2, i1, u1, u2, i1, u1],

    b'GA': [ u1, i2, i4, u1, u1, u1, f4, f4, f4, f4, f4, f4, f4, f4, f4, u1 ],
    b'EA': [ u1, i2, i4, u1, u1, u1, f4, f4, f4, f4, f4, f4, f4, f4, f4, i2, u1 ],
    b'QA': [ u1, i2, i4, u1, u1, u1, f4, f4, f4, f4, f4, f4, f4, f4, f4, u1 ],
    b'CA': [ u1, i2, i4, u1, u1, u1, f4, f4, f4, f4, f4, f4, f4, f4, f4, u1 ],
    b'IA': [ u1, i2, i4, u1, u1, u1, f4, f4, f4, f4, f4, f4, f4, f4, f4, u1 ],
    b'NA': [ u1, i1, i2, f4, u1, f4, f8, f4, f4, f4, f4, f4, f4, u1, u1, f4, u1],#47
    b'NA': [ u1, i1, i2, f4, u1, f4, f8, f4, f4, f4, f4, f4, f4, u1, u1],#52
    b'WA': [ u1, u1, u1, u1, u4, f8, f8, f8, f4, f4, f4, u4, u2, u1],
    b'GE': [ u1,u4,u1,i2,i4,i1,u1,i2,
      f4,f4,f4,f4,i4,i2,
      f8,f8,f8,f8,f8,f8,
      f4,f4,f4,f4,f4,f4,
      f4,f4,f4, u1],
    b'GE168': [ u1,u4,u1,i2,i4,i1,u1,i2,
      f4,f4,f4,f4,i4,i2,
      f8,f8,f8,f8,f8,f8,
      f4,f4,f4,f4,f4,f4,
      f4,f4,f4,     u1,i4,i4,f8,f4,
    i1,i1,i1,i1,  f4,f4,f4,f4,  f4, u1],
    b'NE': [ u1, i1, i2, i4, i4, u1, u1, u1, 
                            f8, f8, f8, f4, f4, f4, f4, f4, f4, f8, f4, f4, u1 ],
    b'EN': [ u1, u4, u1, i2, i4, i1, u1, i2, f4, f4, f4, f4, i4, i2, f8, f8, f8, f8, f8, f8, f4, f4, f4, f4, f4, f4, f4, f4, f4, f4, f4, f4, f4, f4, u1, u1, f4, u1 ],
    b'QE': [ u1, u4, u1, i2, i4, i1, u1, i2, f4, f4, f4, f4, i4, i2, f8, f8, f8, f8, f8, f8, f4, f4, f4, f4, f4, f4, f4, f4, f4, u1],
    b'CN': [ u1, u4, u1, i2, i4, i1, u1, i2, f4, f4, f4, f4, i4, i2, f8, f8, f8, f8, f8, f8, f4, f4, f4, f4, f4, f4, f4, f4, f4, f4, u1, f4, u1],
    b'WE': [ u1, u1, u1, u1, u4, f8, f8, f8, f4, f4, f4, f4, f4, f4, f4, f4, u4, u2, u2, u1 ],
    b'IE': [ u1, u4, u1, i2, i4, i1, u1, i2, f4, f4, f4, f4, i4, i2, f8, f8, f8, f8, f8, f8, f4, f4, f4, f4, f4, f4, f4, f4, f4, u1, u1],
}
fixed_masks = {key: '<'+''.join(value) for key,value in fixed_types.items()}

id_byte_len = {
    b'AN': 1,
    b'SX': 1,
    b'SI': 1,
    b'RC': 8,
    b'rc': 4,
    b'PC': 8,
    b'pc': 4,
    b'NN': 1,
    b'EL': 1,
    b'AZ': 1,
}

def dynamic_masks(nSats):
    dynamic_types = {
        b'AN': [a1 for i in range(nSats)]+[u1],
        b'SX': [u1 for i in range(nSats*2)]+[u1],
        b'SI': [u1 for i in range(nSats)]+[u1],
        b'RC': [f8 for i in range(nSats)]+[u1],
        b'rc': [i4 for i in range(nSats)]+[u1],
        b'PC': [f8 for i in range(nSats)]+[u1],
        b'pc': [u4 for i in range(nSats)]+[u1],
        b'NN': [u1 for i in range(nSats)]+[u1],
        b'EL': [i1 for i in range(nSats)]+[u1],
        b'AZ': [u1 for i in range(nSats)]+[u1],
    }
    return {key: '<'+''.join(value) for key,value in dynamic_types.items()}

def NE_mask(len):
    if len == 80:
        NE_types = {b'NE': [ u1, i1, i2, i4, i4, u1, u1, u1, 
                            f8, f8, f8, f4, f4, f4, f4, f4, f4, f8, f4, f4, u1 ]}
    elif len == 88:
        NE_types = {b'NE': [ u1, i1, i2, i4, i4, u1, u1, u1, 
                            f8, f8, f8, f4, f4, f4, f4, f4, f4, f8, f4, f4, f4, 
                            u1, u1, u2, u1 ]}
    elif len == 103:
        NE_types = {b'NE': [ u1, i1, i2, i4, i4, u1, u1, u1, 
                            f8, f8, f8, f4, f4, f4, f4, f4, f4, f8, f4, f4, f4, 
                            u1, u1, u2, u1, f4, f4, u1, u1, i1, i1, u2, u1 ]}
    return {key: '<'+''.join(value) for key,value in NE_types.items()}

def mask(id, bytelen = 0):
    if bytelen == 0:
        return fixed_masks[id]
#    elif id == b'NE':
#        return NE_mask(bytelen)[id]
    else:
        nSats = int((bytelen - 1)/id_byte_len[id])
        d_mask = dynamic_masks(nSats)
        return d_mask[id]


# nSats
# SatelliteMeasurements = {
#     'SI': [u1 for i in range(nSats+1)],
#     'AN': [a1 for i in range(nSats)]+[u1],
#     'NN': [u1 for i in range(nSats+1)],
#     'EL': [i1 for i in range(nSats)]+[u1],
#     'AZ': [u1 for i in range(nSats+1)],

#     'CR': [i4 for i in range(nSats)]+[u1],
#     '1R': [i4 for i in range(nSats)]+[u1],
#     '2R': [i4 for i in range(nSats)]+[u1],
#     '3R': [i4 for i in range(nSats)]+[u1],
#     '5R': [i4 for i in range(nSats)]+[u1],
#     'IR': [i4 for i in range(nSats)]+[u1],
# }

#PR = {key: [f8 for i in range(10)]+[u1] for key in ['RX','RC','R1','R2','R3','R5','RI']}
#SPR = {key: [i4 for i in range(10)]+[u1] for key in ['rx','rc','r1','r2','r3','r5','rI']}
#RPR = {key: [f4 for i in range(10)]+[u1] for key in ['CR','1R','2R','3R','5R','IR']}
#SRPR = {key: [i2 for i in range(10)]+[u1] for key in ['cr','1r','2r','3r','5r','Ir']}
#PrCorr = {key: [i2 for i in range(10)]+[u1, u1] for key in ['cm','1m','2m','3m','5m','Im']}
#PrCorr = {key: [i2 for i in range(10)]+[u1, u1] for key in ['cm','1m','2m','3m','5m','Im']}

#mes_mask = {key: '<'+''.join(value) for key,value in Types.items()}
#mask = lambda type_: {key: '<'+''.join(value) for key,value in type_.items()}