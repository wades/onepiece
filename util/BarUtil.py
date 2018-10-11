#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author   : Wades
# @Time     : 2018/10/11 3:11 PM
#
# The MIT License (MIT)
#
# Copyright (c) 2018 - 2020

import pandas as pd

from constant.Frequency import FREQUENCY
from constant.MarketType import MARKET_TYPE
from constant.TradeTime import TRADE_TIME


def get_min_index(day, freq=FREQUENCY.FREQ_1_MIN, market=MARKET_TYPE.STOCK_CN):
    """获取股票分钟线的index
    """

    day = str(day)
    # if QA_util_if_trade(day) is True:
    return pd.date_range(day + ' ' + TRADE_TIME.CN_TRADE_AM_S_TIME,
                         day + ' ' + TRADE_TIME.CN_TRADE_AM_E_TIME, freq=freq, closed='right').append(
            pd.date_range(day + ' ' + TRADE_TIME.CN_TRADE_PM_S_TIME,
                          day + ' ' + TRADE_TIME.CN_TRADE_PM_E_TIME, freq=freq, closed='right'))
    # else:
    # return pd.DataFrame(['No trade'])
