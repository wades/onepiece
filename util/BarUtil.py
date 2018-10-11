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

import pandas as pd


def get_min_index(day, type_='1min'):
    """创建股票分钟线的index

    Arguments:
        day {[type]} -- [description]

    Returns:
        [type] -- [description]
    """

    # if QA_util_if_trade(day) is True:
    return pd.date_range(str(day) + ' 09:30:00', str(day) + ' 11:30:00', freq=type_, closed='right').append(
            pd.date_range(str(day) + ' 13:00:00', str(day) + ' 15:00:00', freq=type_, closed='right'))
    # else:
    # return pd.DataFrame(['No trade'])
