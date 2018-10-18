#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author   : Wades
# @Time     : 2018/10/16 22:37
#
# The MIT License (MIT)
#
# Copyright (c) 2018 - 2020
import datetime
import unittest

from fetch import Tdx
from util import LogUtil


class TestTdx(unittest.TestCase):

    def test_fetch_stock_day(self):
        Tdx.fetch_stock_day('000001', '2018-10-15', '2018-10-16')


if __name__ == '__main__':
    unittest.main()
