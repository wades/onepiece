#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author   : Wades
# @Time     : 2018/10/12 00:21
#
# The MIT License (MIT)
#
# Copyright (c) 2018 - 2020


def is_empty(string):
    """"判断字符串是否为空"""
    return True if (string is None or not str(string).strip()) else False
