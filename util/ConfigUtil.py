#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author   : Wades
# @Time     : 2018/10/11 23:51
#
# The MIT License (MIT)
#
# Copyright (c) 2018 - 2020

import configparser
import logging
import os

from constant.Config import CONFIG
from constant.Log import LOG
from util import StringUtil
from util.PathUtil import DEF_LOG_PATH, CONFIG_PATH


def get_log_config():
    """获取日志配置文件"""

    log_config = {
        CONFIG.LOG_PATH: DEF_LOG_PATH,
        CONFIG.LOG_LEVEL: logging.DEBUG
    }

    config = configparser.ConfigParser()
    # 判断是否存在配置文件
    if os.path.exists(CONFIG_PATH):
        try:
            config.read(CONFIG_PATH)
            try:
                # 获取日志目录配置
                log_path = config.get(CONFIG.LOG, CONFIG.LOG_PATH)
                if StringUtil.is_not_empty(log_path):
                    log_config[CONFIG.LOG_PATH] = log_path
            finally:
                pass

            try:
                # 获取日志等级
                log_level = config.get(CONFIG.LOG, CONFIG.LOG_LEVEL)
                if StringUtil.is_not_empty(log_level) and log_level in LOG.TUPLE_LOG_LEVEL:
                    if str(log_level).upper() == LOG.ERROR:
                        log_config[CONFIG.LOG_LEVEL] = logging.ERROR
                    elif str(log_level).upper() == LOG.WARN:
                        log_config[CONFIG.LOG_LEVEL] = logging.WARN
                    elif str(log_level).upper() == LOG.INFO:
                        log_config[CONFIG.LOG_LEVEL] = logging.INFO
                    elif str(log_level).upper() == LOG.DEBUG:
                        log_config[CONFIG.LOG_LEVEL] = logging.DEBUG
            finally:
                pass
        finally:
            pass

    return log_config


def get_tdx_server_config():
    """"获取TDX服务器配置信息"""

    tdx_stock_server_config = {
        CONFIG.TDX_BEST_STOCK_SERVER: {},
        CONFIG.TDX_STOCK_SERVER_LIST: []
    }
    config = configparser.ConfigParser()
    # 判断是否存在配置文件
    if os.path.exists(CONFIG_PATH):
        try:
            config.read(CONFIG_PATH)
            try:
                # 获取服务器配置
                server_list = config.get(CONFIG.TDX_STOCK_SERVER, CONFIG.TDX_STOCK_SERVER_LIST)
                if StringUtil.is_not_empty(server_list):
                    tdx_stock_server_config[CONFIG.TDX_STOCK_SERVER_LIST] = eval(server_list)
            finally:
                pass

            try:
                # 获取默认服务器
                best_stock_server = config.get(CONFIG.TDX_STOCK_SERVER, CONFIG.TDX_BEST_STOCK_SERVER)
                if StringUtil.is_not_empty(best_stock_server):
                    tdx_stock_server_config[CONFIG.TDX_BEST_STOCK_SERVER] = eval(best_stock_server)
            finally:
                pass
        finally:
            pass

    return tdx_stock_server_config


def set_tdx_best_server_info(value):
    """设置TDX服务器配置信息"""

    config = configparser.ConfigParser()
    f = open(CONFIG_PATH, 'w')
    config.set(CONFIG.TDX_STOCK_SERVER, CONFIG.TDX_BEST_STOCK_SERVER, value)
    config.write(f)
    f.close()
