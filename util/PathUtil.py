#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author   : Wades
# @Time     : 2018/10/11 23:07
#
# The MIT License (MIT)
#
# Copyright (c) 2018 - 2020

import os


def generate_path(base_path, sub_path):
    return '{}{}{}'.format(base_path, os.sep, sub_path)


# OP项目所在目录
OP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件
CONFIG_PATH = generate_path(generate_path(OP_PATH, 'config'), "config.ini")

# OnePiece运行过程中产生的数据存放地址
OP_RUNTIME_PATH = generate_path(OP_PATH, '.onepiece')

# 默认日志文件根目录
DEF_LOG_PATH = generate_path(OP_RUNTIME_PATH, 'logs')

# 默认缓存文件根目录
DEF_CACHE_PATH = generate_path(OP_RUNTIME_PATH, 'caches')


def init_runtime_path():
    # 创建.onepiece目录
    os.makedirs(OP_RUNTIME_PATH, exist_ok=True)
    # 创建日志目录
    os.makedirs(DEF_LOG_PATH, exist_ok=True)
    # 创建缓存目录
    os.makedirs(DEF_CACHE_PATH, exist_ok=True)


if __name__ == '__main__':
    init_runtime_path()
