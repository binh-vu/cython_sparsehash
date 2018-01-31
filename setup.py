#!/usr/bin/python
# -*- coding: utf-8 -*-

from distutils.core import setup, Extension
from Cython.Build import cythonize

ext = Extension(
    name="sparsehash.dense_hash_map",
    sources=["sparsehash/dense_hash_map.pyx"],
    language='c++',
    extra_compile_args=['-std=c++14', '-stdlib=libc++'])
ext_modules = cythonize(ext)

setup(
    name='sparsehash',
    version='0.0.1',
    description='A cython wrapped of google sparsehash library',
    author='Binh Vu',
    author_email='binhlvu@gmail.com',
    url='https://github.com/binh-vu/pyutils',
    ext_modules=ext_modules,
    packages=['sparsehash'])
