#!/usr/bin/env python

import requests
import json

API_URL="http://localhost:8080"

APP = {
    'id': 'healthy',
    'cmd': 'healthy --ip localhost --port 4242',
    'cpus': 0.5,
    'mem': 16.0,
    'instances': 1,
    'container': {
        'type': 'DOCKER',
        'docker': {
            'image': 'eddyzags/healthy:latest',
            'network': 'HOST',
        }
    },
    'healthChecks': [
        {
            'protocol': 'COMMAND',
            'command': { 'value': 'curl -f -X GET http://localhost:4242/' },
            'maxConsecutiveFailures': 3,
        },
    ],
}


headers = {'Accept': 'application/json',
           'Content-Type': 'application/json; charset=utf-8'}

r = requests.post(API_URL+"/v2/apps", headers=headers, data=json.dumps(APP))

if r.status_code >= 400:
    print("An unexpected error occured: ", r.json())
else:
    print "The app has been deploy successfully"
