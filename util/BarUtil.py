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

from constant import FreqConst, TradeTimeConst


def get_min_index(day, type_=FreqConst.FREQ_1_MIN):
    """获取股票分钟线的index
    """
    day = str(day)
    # if QA_util_if_trade(day) is True:
    return pd.date_range(day + ' ' + TradeTimeConst.SS_TRADE_AM_S_TIME,
                         day + ' ' + TradeTimeConst.SS_TRADE_AM_E_TIME, freq=type_, closed='right').append(
            pd.date_range(day + ' ' + TradeTimeConst.SS_TRADE_PM_S_TIME,
                          day + ' ' + TradeTimeConst.SS_TRADE_PM_E_TIME, freq=type_, closed='right'))
    # else:
    # return pd.DataFrame(['No trade'])
