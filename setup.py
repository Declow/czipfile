#!/usr/bin/python
# vim: set expandtab tabstop=4 shiftwidth=4:

import os
from distutils.core import setup
from Cython.Distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

# Utility function to read the README file.  
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()

setup(
    name = 'czipfile',
    version = '1.0.1',
    author = 'Python distribution, modified by CJ Kucera',
    author_email = 'pez@apocalyptech.com',
    description = ('A replacement for the builtin zipfile module, with '
                   'fast, C-based zipfile decryption'),
    license = 'Python Software Foundation License',
    keywords = 'zipfile zip decryption',
    url = 'http://pypi.python.org/pypi/czipfile',
    long_description = read('README'),
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Python Software Foundation License',
        ],
    ext_modules = cythonize('czipfile.pyx', compiler_directives=dict(language_level=3), annotate=True),
    cmdclass = {'build_ext': build_ext},
)
