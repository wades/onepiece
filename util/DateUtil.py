#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author   : Wades
# @Time     : 2018/10/11 7:11 PM
#
# The MIT License (MIT)
#
# Copyright (c) 2018 - 2020

import time


def is_valid_date(date):
    """判断是否是一个有效的日期字符串
    """

    try:
        time.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False
