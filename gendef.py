#!/usr/bin/python

# generate union def given a list of members and register name
def genunion(reg):
    name = reg.pop()
    print 'typedef union', '_' + name, '{'
    print '  u32 data;'
    print '  struct {' 
    for i in reg:
        print '    u32', i + ';'
    print '  } fields;' 
    print '}', name + ';' + '\n'

genunion(['tRCDW:5', 'tRCDWA:5', 'tRCDR:5', 'tRCDRA:5', 'tRRD:4', 'tRC:7', 'SEQ_RAS_TIMING'])
genunion(['tNOPW:2', 'tNOPR:2', 'tR2W:5', 'tCCDL:3', 'tR2R:4', 'tW2R:8', 'tCL:8', 'SEQ_CAS_TIMING'])
genunion(['tRP_WRA:7', 'tRP_RDA:7', 'tRP:6', 'tRFC:9', 'SEQ_MISC_TIMING'])
genunion(['PA2RDATA:4', 'PA2WDATA:4', 'FAW:5', 'tREDC:3', 'tWEDC:5', 't32AW:7', 'tWDATATR:4', 'SEQ_MISC_TIMING2'])
genunion(['tCKSRE:4', 'tCKSRX:4', 'tCKE_PULSE:4', 'tCKE:6', 'SEQ_IDLE:5', 'tCKE_PULSE_MSB:1', 'SEQ_IDLE_SS:8', 'SEQ_PMG_TIMING'])
genunion(['RAS2RAS:8', 'RP:8', 'WRPLUSRP:8', 'BUS_TURN:8', 'ARB_DRAM_TIMING2'])

