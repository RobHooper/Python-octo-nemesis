#!/usr/bin/python2.7

## Open config from local dir
#from config import *

## Open config from home dir

mydir = "~/"
from os.path import expanduser
from sys import path

# Expand tilde to /home/wibble
mydir = expanduser(mydir)
# Insert new path into sys.path
path.insert(0, mydir)

from config import *

print x
