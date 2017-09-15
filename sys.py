#!/usr/bin/python2.7
import sys

if (len(sys.argv) < 3) or (len(sys.argv) > 3):
    print('Usage : sys.py arg1 arg2')
    sys.exit()

print sys.argv[0]
print sys.argv[1]
print sys.argv[2]


sys.exit()
