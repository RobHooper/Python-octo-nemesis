#!/usr/bin/python2.7

import os
lockFile = './wibble'

def fileLock():
    if os.path.isfile(lockFile):
        for pid in lockFile:
            try:
                os.kill(pid, 0)
                return(True)
            except:
                os.remove(lockFile)
                print('Lock file was not removed by previous process, removing this now!')
                return(False)
    else:
        l = open(lockFile, 'w')
        l.write(str(os.getpid()))
        l.close()
        return(False)
    

print fileLock()


