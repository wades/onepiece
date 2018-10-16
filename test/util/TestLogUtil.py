#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author   : Wades
# @Time     : 2018/10/16 22:37
#
# The MIT License (MIT)
#
# Copyright (c) 2018 - 2020

import unittest

from util import LogUtil


class TestLogUtil(unittest.TestCase):

    def test_log_debug(self):
        print(LogUtil.log_debug("debug"))


if __name__ == '__main__':
    unittest.main()
