#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author   : Wades
# @Time     : 2018/10/12 00:15
#
# The MIT License (MIT)
#
# Copyright (c) 2018 - 2020

import unittest

from util import ConfigUtil


class TestConfigUtil(unittest.TestCase):

    def test_get_log_config(self):
        print(ConfigUtil.get_log_config())


if __name__ == '__main__':
    unittest.main()
