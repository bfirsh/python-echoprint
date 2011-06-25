#!/usr/bin/env python
from distutils.core import setup, Extension

echoprint_ext = Extension(
    'echoprint', 
    [
        'libcodegen/AudioBufferInput.cxx',
        'libcodegen/AudioStreamInput.cxx',
        'libcodegen/Base64.cxx',
        'libcodegen/Codegen.cxx',
        'libcodegen/Fingerprint.cxx',
        'libcodegen/MatrixUtility.cxx',
        'libcodegen/Metadata.cxx',
        'libcodegen/SubbandAnalysis.cxx',
        'libcodegen/Whitening.cxx',
        'echoprint.cpp',
    ],
    include_dirs=['libcodegen'],
    libraries=['tag', 'z', 'pthread'],
)

setup(
    name='python-echoprint',
    version='0.1',
    description="A Python library for Echonest's Echoprint music identification service",
    author='Ben Firshman',
    author_email='ben@firshman.co.uk',
    url='https://github.com/bfirsh/python-echoprint',
    ext_modules=[echoprint_ext],
)

