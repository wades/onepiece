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

# 配置文件根目录
CONFIG_PATH = generate_path(OP_PATH, 'config')

# 日志配置文件
LOG_CONFIG_PATH = generate_path(CONFIG_PATH, "log.cfg")

# OnePiece运行过程中产生的数据存放地址
OP_RUNTIME_PATH = generate_path(OP_PATH, '.onepiece')

# 日志文件根目录
LOG_PATH = generate_path(OP_RUNTIME_PATH, 'logs')

# 缓存文件根目录
CACHE_PATH = generate_path(OP_RUNTIME_PATH, 'caches')


def init_runtime_path():
    # 创建.onepiece目录
    os.makedirs(OP_RUNTIME_PATH, exist_ok=True)
    # 创建日志目录
    os.makedirs(LOG_PATH, exist_ok=True)
    # 创建缓存目录
    os.makedirs(CACHE_PATH, exist_ok=True)


if __name__ == '__main__':
    init_runtime_path()
