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
from util import DateUtil


def get_min_index(date, freq=FREQUENCY.FREQ_1_MIN, market=MARKET_TYPE.STOCK_CN):
    """获取不同市场股票分钟线的index
    """

    # 参数校验
    if market not in MARKET_TYPE.TUPLE_MARKET_TYPE or freq not in FREQUENCY.TUPLE_FREQ_MIN \
            or not DateUtil.is_valid_date(date):
        return None

    # if QA_util_if_trade(day) is True:
    if market == MARKET_TYPE.STOCK_CN:
        return __get_market_cn_index(date, freq)
    elif market == MARKET_TYPE.STOCK_HK:
        return __get_market_hk_index(date, freq)
    else:
        return None


def get_hour_index(date, freq=FREQUENCY.FREQ_1_HOUR, market=MARKET_TYPE.STOCK_CN):
    """获取不同市场股票小时线的index
    """

    # 参数校验
    if market not in MARKET_TYPE.TUPLE_MARKET_TYPE or freq not in FREQUENCY.TUPLE_FREQ_HOUR \
            or not DateUtil.is_valid_date(date):
        return None

    if market == MARKET_TYPE.STOCK_CN:
        return __get_market_cn_index(date, freq)
    elif market == MARKET_TYPE.STOCK_HK:
        return __get_market_hk_index(date, freq)
    else:
        return None


def __get_market_cn_index(d, freq):
    return pd.date_range('{} {}'.format(d, TRADE_TIME.CN_TRADE_AM_S_TIME),
                         '{} {}'.format(d, TRADE_TIME.CN_TRADE_AM_E_TIME), freq=freq, closed='right').append(
        pd.date_range('{} {}'.format(d, TRADE_TIME.CN_TRADE_PM_S_TIME),
                      '{} {}'.format(d, TRADE_TIME.CN_TRADE_PM_E_TIME), freq=freq, closed='right'))


def __get_market_hk_index(d, freq):
    return pd.date_range('{} {}'.format(d, TRADE_TIME.HK_TRADE_AM_S_TIME),
                         '{} {}'.format(d, TRADE_TIME.HK_TRADE_AM_E_TIME), freq=freq, closed='right').append(
        pd.date_range('{} {}'.format(d, TRADE_TIME.HK_TRADE_PM_S_TIME),
                      '{} {}'.format(d, TRADE_TIME.HK_TRADE_PM_E_TIME), freq=freq, closed='right'))