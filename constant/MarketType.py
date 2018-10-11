#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author   : Wades
# @Time     : 2018/10/11 5:45 PM
#
# The MIT License (MIT)
#
# Copyright (c) 2018 - 2020


class MARKET_TYPE:
    """市场类型常量
    """

    # 沪深A股
    STOCK_CN = 'stock_cn'
    # 港股
    STOCK_HK = 'stock_hk'
    # 中国B股
    # STOCK_CN_B = 'stock_cn_b'
    # 中国D股 沪伦通
    # STOCK_CN_D = 'stock_cn_d'
    # 美股
    # STOCK_US = 'stock_us'
    # 国内期货
    # FUTURE_CN = 'future_cn'
    # 国内期权
    # OPTION_CN = 'option_cn'
    # 个股期权
    # STOCKOPTION_CN = 'stockoption_cn'
    # 比特币
    # BITCOIN = 'bitcoin'
    # 加密货币(衍生货币)
    # CRYPTO_CURRENCY = 'crypto_currency'
    # 中国指数
    # INDEX_CN = 'index_cn'
    # 中国基金
    # FUND_CN = 'fund_cn'
    # 中国债券
    # BOND_CN = 'bond_cn'

    # 市场元组
    TUPLE_MARKET_TYPE = (STOCK_CN, STOCK_HK)
