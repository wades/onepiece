#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author   : Wades
# @Time     : 2018/10/11 3:11 PM
#
# The MIT License (MIT)
#
# Copyright (c) 2018 - 2020

import unittest

from constant import FreqConst
from util import BarUtil


class TestBarUtil(unittest.TestCase):

    def test_get_min_index(self):
        self.assertEquals(BarUtil.get_min_index('2018-10-11', FreqConst.FREQ_1_MIN).size, 240)
        self.assertEquals(BarUtil.get_min_index('2018-10-11', FreqConst.FREQ_3_MIN).size, 80)
        self.assertEquals(BarUtil.get_min_index('2018-10-11', FreqConst.FREQ_5_MIN).size, 48)
        self.assertEquals(BarUtil.get_min_index('2018-10-11', FreqConst.FREQ_10_MIN).size, 24)
        self.assertEquals(BarUtil.get_min_index('2018-10-11', FreqConst.FREQ_15_MIN).size, 16)
        self.assertEquals(BarUtil.get_min_index('2018-10-11', FreqConst.FREQ_30_MIN).size, 8)
        self.assertEquals(BarUtil.get_min_index('2018-10-11', FreqConst.FREQ_60_MIN).size, 4)


if __name__ == '__main__':
    unittest.main()