#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author   : Wades
# @Time     : 2018/10/11 3:11 PM
#
# The MIT License (MIT)
#
# Copyright (c) 2018 - 2020
#

import unittest

from util import BarUtil


class TestBarUtil(unittest.TestCase):

    def test_get_min_index(self):
        min_bar = BarUtil.get_min_index('2018-10-11')


if __name__ == '__main__':
    unittest.main()
