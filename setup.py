#!/usr/bin/env python

try:
    from setuptools import setup, Extension
    has_setuptools = True
except:
    from distutils.core import setup, Extension
    has_setuptools = False

# Subclass the build commands to run build_ext before build_py so that
# build_py can find Mykytea.py.
# ref. http://stackoverflow.com/questions/12491328/python-distutils-not-include-the-swig-generated-module

cmdclass = {}

def patch_command(name, base_class):
    class CustomCommand(base_class):
        def run(self):
            self.run_command('build_ext')
            base_class.run(self)
    cmdclass[name] = CustomCommand

from distutils.command.build import build
patch_command('build', build)

if has_setuptools:
    from setuptools.command.install import install
    from setuptools.command.bdist_egg import bdist_egg
    patch_command('install', install)
    patch_command('bdist_egg', bdist_egg)

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
      cmdclass=cmdclass,
      py_modules=['Mykytea'],
      ext_modules=[ext_module],
      )
