#!/usr/bin/python
# modifies strap with typical timing improvements

import sys

strap = sys.argv[1]
print "Old, new RRD:", strap[28], ", 5"
strap = strap[:28] + '5' + strap[29:]
print "Old, new ACTRD:", strap[80:82], ", 0x10"
strap = strap[:80] + '10' + strap[82:]
print "Old, new FAW:", strap[51], ", 0"
strap = strap[:51] + '0' + strap[52:]
print sys.argv[1]
print strap
