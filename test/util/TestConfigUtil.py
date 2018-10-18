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

from constant.Config import CONFIG
from util import ConfigUtil


class TestConfigUtil(unittest.TestCase):

    def test_get_log_config(self):
        print(ConfigUtil.get_log_config())

    def test_get_tdx_server_config(self):
        tdx_server_config = ConfigUtil.get_tdx_server_config()
        print(tdx_server_config)
        self.assertTrue(isinstance(tdx_server_config, dict))
        self.assertTrue(isinstance(tdx_server_config[CONFIG.TDX_STOCK_SERVER_LIST], list))


if __name__ == '__main__':
    unittest.main()
