#!/usr/bin/python
# -*- coding: utf-8 -*-

from distutils.core import setup, Extension
from setuptools import find_packages
from Cython.Build import cythonize

ext = Extension(name="sparsehash",
         sources=["sparsehash/dense_hash_map.pyx", "sparsehash/dense_hash_set.pyx"],
         language='c++',
         extra_compile_args=['-std=c++14', '-stdlib=libc++'])

setup(
    name='sparsehash',
    version='0.0.1',
    description='A cython wrapped of google sparsehash library',
    author='Binh Vu',
    author_email='binhlvu@gmail.com',
    url='https://github.com/binh-vu/pyutils',
    ext_modules=cythonize(ext),
    packages=find_packages(exclude=['tests.*', 'tests'])
)
