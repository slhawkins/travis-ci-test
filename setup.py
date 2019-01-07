#!/usr/bin/env python

from distutils.core import setup
from glob import glob

from setuptools import find_packages

setup(name='PWV Travis CI Test',
      version='1.0',
      description='',
      author='PWV Consultants',
      packages=find_packages('pysrc'),
      package_dir={'': 'pysrc'},
      py_modules=[splitext(basename(path))[0] for path in glob('pysrc/*.py')],
     )