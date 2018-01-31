#!/usr/bin/python
# -*- coding: utf-8 -*-

import timeit

setup = "from benchmark_c import test_build_dict_c, test_build_dict, test_access_dict_c, test_access_dict, test_build_set, test_build_set_c, test_access_set, test_access_set_c"
number = int(1e4)

print("== BUILD DICT ==")
print("DenseMap     :", timeit.timeit(stmt="test_build_dict_c(2000)", setup=setup, number=number))
print("DefaultDict  :", timeit.timeit(stmt="test_build_dict(2000)", setup=setup, number=number))

print("== ACCESS DICT ==")
print("DenseMap     :", timeit.timeit(stmt="test_access_dict_c(100, 2000)", setup=setup, number=number))
print("DefaultDict  :", timeit.timeit(stmt="test_access_dict(100, 2000)", setup=setup, number=number))

print("== BUILD SET ==")
print("DenseSet     :", timeit.timeit(stmt="test_build_set_c(2000)", setup=setup, number=number))
print("DefaultSet   :", timeit.timeit(stmt="test_build_set(2000)", setup=setup, number=number))

print("== ACCESS SET ==")
print("DenseSet     :", timeit.timeit(stmt="test_access_set_c(100, 2000)", setup=setup, number=number))
print("DefaultSet   :", timeit.timeit(stmt="test_access_set(100, 2000)", setup=setup, number=number))
