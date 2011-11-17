#!/usr/bin/env python
import echoprint
import requests
import subprocess
import sys
import struct
import os
import json

if len(sys.argv) < 4:
    print "Usage: identify.py api_key filename start duration"
    sys.exit(1)

api_key = sys.argv[1]
filename = sys.argv[2]
start = sys.argv[3]
duration = sys.argv[4]

p = subprocess.Popen([
    'ffmpeg',
    '-i', filename,
    '-ac', '1',
    '-ar', '11025',
    '-f', 's16le',
    '-t', duration,
    '-ss', start,
    '-',
], stdout=subprocess.PIPE)

samples = []

while True:
    sample = p.stdout.read(2)
    if sample == '':
        break
    samples.append(struct.unpack('h', sample)[0] / 32768.0)

d = echoprint.codegen(samples, int(start))

if os.environ.has_key('HTTP_PROXY'):
    proxy = os.environ['HTTP_PROXY']
else:
    proxy = None

r = requests.post(
    'http://developer.echonest.com/api/v4/song/identify', 
    data={'query': json.dumps(d), 'api_key': api_key, 'version': d['version']}, 
    headers={'content-type': 'application/x-www-form-urlencoded'}, 
    proxies={'http': proxy}
)
print r.content
