#!/usr/bin/python
# -*- coding: utf-8 -*-

from distutils.core import setup
from setuptools import find_packages

setup(
    name='sparsehash',
    version='0.0.1',
    description='A cython wrapped of google sparsehash library',
    author='Binh Vu',
    author_email='binhlvu@gmail.com',
    url='https://github.com/binh-vu/pyutils',
    packages=find_packages(exclude=['tests.*', 'tests'])
)
