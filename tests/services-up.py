#!/usr/bin/env python

import sys
import subprocess
import time
import os


def ping(ip, port):
    cmd = "nc -z "+ip+" "+port
    response = os.system(cmd)
    return response


idx = 1
while idx < len(sys.argv) - 1:
    print "Waiting for "+sys.argv[idx]+" to launch..."

    while ping("localhost", sys.argv[idx+1]) != 0:
        time.sleep(1)

    print sys.argv[idx]+ " is up and running"
    print ""
        
    idx = idx + 2
