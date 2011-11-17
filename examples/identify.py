#!/usr/bin/env python
import echoprint
import urllib
import subprocess
import sys
import struct

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

d['api_key'] = api_key
res = urllib.urlopen('http://developer.echonest.com/api/v4/song/identify?' + urllib.urlencode(d)).read()

print res

