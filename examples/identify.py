#!/usr/bin/env python
import echoprint
import requests
import subprocess
import sys
import struct

if len(sys.argv) < 2:
    print "Usage: identify.py api_key filename"
    sys.exit(1)

api_key = sys.argv[1]
filename = sys.argv[2]

p = subprocess.Popen([
    'ffmpeg',
    '-i', filename,
    '-ac', '1',
    '-ar', '11025',
    '-f', 's16le',
    '-t', '30',
    '-ss', '0',
    '-',
], stdout=subprocess.PIPE)

samples = []

while True:
    sample = p.stdout.read(2)
    if sample == '':
        break
    samples.append(struct.unpack('h', sample)[0] / 32768.0)

d = echoprint.codegen(samples)

d['api_key'] = api_key
res = requests.get('http://developer.echonest.com/api/v4/song/identify', d)

print res.content

