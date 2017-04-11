#!/usr/bin/python
# modifies strap with typical timing improvements

import sys

strap = sys.argv[1]

if strap[4] == '0':
  print "Rx strap detected"
  RAS=24
else:
  print "R9 strap detected"
  RAS=16

print "Old, new RRD:", strap[RAS+4], ", 5"
strap = strap[:RAS+4] + '5' + strap[RAS+5:]

print "Old, new FAW:", strap[RAS+27], ", 0"
strap = strap[:RAS+27] + '0' + strap[RAS+28:]

t32AW = int(strap[RAS+28],16)/2 + int(strap[RAS+31])*8
print "Old, new 32AW:", t32AW, ", 0"
strap = strap[:RAS+28] + '0' + strap[RAS+29:RAS+31] + '0' + strap[RAS+32:]

print "Old, new ACTRD:", strap[80:82], ", 0x10"
strap = strap[:80] + '10' + strap[82:]

print sys.argv[1]
print strap
