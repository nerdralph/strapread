#!/usr/bin/python

# swap bytes in little-endian hex string to big endian
def swapb(hex8):
    return hex8[6:8] + hex8[4:6] + hex8[2:4] + hex8[0:2]

# generate dump function 
def gendump(reg, data):
    name = reg.pop()
    print '    ' + name, name + '_d = {0x' + swapb(data) + '};' 
    print '    printf("' + name + '\\n");'
    for i in reg:
        i = i[0:-2]
        print '    printf("' + i + ':%d ",' + name + '_d.fields.' + i + ');'
    print '    printf("\\n");' 

# Rx470 Samsung
strap = '555000000000000022CC1C00CE596B44D0570F1531CB2409004AE7000B0314207A8900A003000000170F2E36922A3217'
# Rx470 Hynix
#strap = '777000000000000022339D00CE516A3D9055111230CB4409004AE600740114206A8900A002003120150F292F94273116'
# unknown Hynix
#strap = 'BBB000000000000022889D0073EE8D53805515133ECF560C004E26017E0514206A8900A0020031201C143840C5303F17'

gendump(['tCKSRE:4', 'tCKSRX:4', 'tCKE_PULSE:4', 'tCKE:6', 'SEQ_IDLE:5', 'tCKE_PULSE_MSB:1', 'SEQ_IDLE_SS:8', 'SEQ_PMG_TIMING'], strap[16:24])
gendump(['tRCDW:5', 'tRCDWA:5', 'tRCDR:5', 'tRCDRA:5', 'tRRD:4', 'tRC:7', 'SEQ_RAS_TIMING'], strap[24:32])
gendump(['tNOPW:2', 'tNOPR:2', 'tR2W:5', 'tCCDL:3', 'tR2R:4', 'tW2R:8', 'tCL:8', 'SEQ_CAS_TIMING'], strap[32:40])
gendump(['tRP_WRA:8', 'tRP_RDA:7', 'tRP:5', 'tRFC:9', 'SEQ_MISC_TIMING'], strap[40:48])
gendump(['PA2RDATA:4', 'PA2WDATA:4', 'FAW:5', 'tREDC:3', 'tWEDC:5', 't32AW:7', 'tWDATATR:4', 'SEQ_MISC_TIMING2'], strap[48:64])
gendump(['RAS2RAS:8', 'RP:8', 'WRPLUSRP:8', 'BUS_TURN:8', 'ARB_DRAM_TIMING2'], strap[88:96])

