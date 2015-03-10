python-echoprint
================

A Python library for Echonest's [Echoprint](http://echoprint.me/) music identification service.

Unlike the [official library](http://code.google.com/p/pyechonest/), it does not need to save anything to disk -- a list of samples can be passed directly to the library.

Building
--------

First, you need to install the build dependencies. On Ubuntu/Debian, run:

    $ sudo apt-get install python-dev libboost-dev libtag1-dev ffmpeg

Ubuntu 14.04 users should note that `ffmpeg` is not available in the official
Ubuntu repositories. It can be retrieved from [Jon Severinsson's FFmpeg PPA](https://launchpad.net/~jon-severinsson/+archive/ubuntu/ffmpeg)

    sudo apt-add-repository ppa:jon-severinsson/ffmpeg
    sudo apt-get update
    sudo apt-get install ffmpeg

Ubuntu users who cannot install `ffmpeg` or are interested in more information on the subject should consult this [Askubuntu answer](http://askubuntu.com/a/432585/103738).

On OS X, you need to install [Homebrew](http://mxcl.github.com/homebrew/), and
run:

    $ brew install boost taglib

Then as root or in a virtualenv:

    python setup.py install

Usage
-----

    import echoprint
    import requests

    d = echoprint.codegen([0.0, 0.0, ...])
    d['api_key'] = YOUR_KEY
    print requests.get('http://developer.echonest.com/api/v4/song/identify', d).content

`echoprint.codegen()` takes a list of floating point PCM data sampled at 11025 Hz and mono. It optionally takes a second integer argument to hint the server on where the sample is taken from in the original file if known.

For a more complete example, see `examples/identify.py`. [requests](http://python-requests.org) is required:

    pip install requests

Test suite
----------

    $ pip install nose
    $ nosetests
