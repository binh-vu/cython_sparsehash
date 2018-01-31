#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyximport; pyximport.install()
from tests.hash_map import *


def test():
    test_access_func()
    test_build_func()
    test_del_func()
    test_has_func()
