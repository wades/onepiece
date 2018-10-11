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

from constant.Frequency import FREQUENCY
from constant.MarketType import MARKET_TYPE
from util import BarUtil


class TestBarUtil(unittest.TestCase):

    def test_get_min_index(self):
        date = '2018-10-11'
        # A股市场
        self.assertEquals(BarUtil.get_min_index(date, FREQUENCY.FREQ_1_MIN, MARKET_TYPE.STOCK_CN).size, 240)
        self.assertEquals(BarUtil.get_min_index(date, FREQUENCY.FREQ_3_MIN, MARKET_TYPE.STOCK_CN).size, 80)
        self.assertEquals(BarUtil.get_min_index(date, FREQUENCY.FREQ_5_MIN, MARKET_TYPE.STOCK_CN).size, 48)
        self.assertEquals(BarUtil.get_min_index(date, FREQUENCY.FREQ_10_MIN, MARKET_TYPE.STOCK_CN).size, 24)
        self.assertEquals(BarUtil.get_min_index(date, FREQUENCY.FREQ_15_MIN, MARKET_TYPE.STOCK_CN).size, 16)
        self.assertEquals(BarUtil.get_min_index(date, FREQUENCY.FREQ_30_MIN, MARKET_TYPE.STOCK_CN).size, 8)
        self.assertEquals(BarUtil.get_min_index(date, FREQUENCY.FREQ_60_MIN, MARKET_TYPE.STOCK_CN).size, 4)
        # 港股市场
        self.assertEquals(BarUtil.get_min_index(date, FREQUENCY.FREQ_1_MIN, MARKET_TYPE.STOCK_HK).size, 330)
        self.assertEquals(BarUtil.get_min_index(date, FREQUENCY.FREQ_3_MIN, MARKET_TYPE.STOCK_HK).size, 110)
        self.assertEquals(BarUtil.get_min_index(date, FREQUENCY.FREQ_5_MIN, MARKET_TYPE.STOCK_HK).size, 66)
        self.assertEquals(BarUtil.get_min_index(date, FREQUENCY.FREQ_10_MIN, MARKET_TYPE.STOCK_HK).size, 33)
        self.assertEquals(BarUtil.get_min_index(date, FREQUENCY.FREQ_15_MIN, MARKET_TYPE.STOCK_HK).size, 22)
        self.assertEquals(BarUtil.get_min_index(date, FREQUENCY.FREQ_30_MIN, MARKET_TYPE.STOCK_HK).size, 11)
        self.assertEquals(BarUtil.get_min_index(date, FREQUENCY.FREQ_60_MIN, MARKET_TYPE.STOCK_HK).size, 5)

    def test_get_hour_index(self):
        date = '2018-10-11'
        # A股市场
        self.assertEquals(BarUtil.get_hour_index(date, FREQUENCY.FREQ_1_HOUR, MARKET_TYPE.STOCK_CN).size, 4)
        # 港股市场
        self.assertEquals(BarUtil.get_hour_index(date, FREQUENCY.FREQ_1_HOUR, MARKET_TYPE.STOCK_HK).size, 5)


if __name__ == '__main__':
    unittest.main()
