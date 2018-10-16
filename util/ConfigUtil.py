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

from constant.Log import LOG
from util import StringUtil
from util.PathUtil import DEF_LOG_PATH, LOG_CONFIG_PATH


def get_log_config():
    """获取日志配置文件
    """

    log_config = {
        'PATH': DEF_LOG_PATH,
        'LEVEL': logging.DEBUG
    }

    config = configparser.ConfigParser()
    # 判断是否存在日志的配置文件
    if os.path.exists(LOG_CONFIG_PATH):
        try:
            config.read(LOG_CONFIG_PATH)
            try:
                # 获取日志目录配置
                log_path = config.get('LOG', 'path')
                if StringUtil.is_not_empty(log_path):
                    log_config['PATH'] = log_path
            finally:
                pass

            try:
                # 获取日志等级
                log_level = config.get('LOG', 'level')
                if StringUtil.is_not_empty(log_level) and log_level in LOG.TUPLE_LOG_LEVEL:
                    if str(log_level).upper() == LOG.ERROR:
                        log_config['LEVEL'] = logging.ERROR
                    elif str(log_level).upper() == LOG.WARN:
                        log_config['LEVEL'] = logging.WARN
                    elif str(log_level).upper() == LOG.INFO:
                        log_config['LEVEL'] = logging.INFO
                    elif str(log_level).upper() == LOG.DEBUG:
                        log_config['LEVEL'] = logging.DEBUG
            finally:
                pass
        finally:
            with open(LOG_CONFIG_PATH, 'w') as f:
                config.write(f)
                f.close()

    return log_config
