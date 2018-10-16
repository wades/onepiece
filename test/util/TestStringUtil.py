#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author   : Wades
# @Time     : 2018/10/12 00:26
#
# The MIT License (MIT)
#
# Copyright (c) 2018 - 2020

import unittest

from util import StringUtil


class TestStringUtil(unittest.TestCase):

    def test_is_empty(self):
        self.assertEquals(StringUtil.is_empty(""), True)
        self.assertEquals(StringUtil.is_empty(None), True)
        self.assertEquals(StringUtil.is_empty("test"), False)


if __name__ == '__main__':
    unittest.main()
