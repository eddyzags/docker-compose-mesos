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
retries = 5
while idx < len(sys.argv) - 1:
    print "Waiting for "+sys.argv[idx]+" to launch..."

    count = 0
    while count < retries and ping("localhost", sys.argv[idx+1]) != 0:
        print "Retrying for "+sys.argv[idx]+ " ..."
        time.sleep(1)
        count += 1
        

        
    if count == retries:
        print "Unable to reach "+sys.argv[idx]
        print ""
        idx = idx + 2
        continue

    print sys.argv[idx]+ " is up and running"
    print ""

    idx = idx + 2

