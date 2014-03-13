#!/usr/bin/env python

try:
    from setuptools import setup, Extension
except:
    from distutils.core import setup, Extension

def has_swig():
    import os
    import subprocess

    devnull = open(os.devnull, 'w')
    retcode = subprocess.call(['swig', '-version'], stdout=devnull)
    return retcode == 0

use_swig = has_swig()

if use_swig:
    ext_module = Extension(
        '_Mykytea',
        sources=['mykytea.i', 'mykytea.cpp'],
        libraries=["kytea"],
        swig_opts=['-Wall', '-shadow', '-c++', '-I/usr/local/include'],
        )

else:
    ext_module = Extension(
        '_Mykytea',
        sources=['mykytea_wrap.cxx', 'mykytea.cpp'],
        libraries=["kytea"],
        )

setup(name='kytea-python',
      version='0.1',
      author='chezou',
      author_email='chezou@gmail.com',
      ext_modules=[ext_module],
      py_modules=['Mykytea'],
      )
