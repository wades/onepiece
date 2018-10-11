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
import os

from util import StringUtil
from util.PathUtil import LOG_PATH, LOG_CONFIG_PATH


def get_log_config():
    """获取日志配置文件
    """

    config = configparser.ConfigParser()
    # 判断是否存在日志的配置文件
    if os.path.exists(LOG_CONFIG_PATH):
        config.read(LOG_CONFIG_PATH)
        try:
            # 获取日志目录配置
            log_path = config.get('LOG', 'path')
            # 日志地址为空
            if StringUtil.is_empty(log_path):
                config.set('LOG', 'path', LOG_PATH)
                log_path = LOG_PATH
            return log_path
        except configparser.NoSectionError:
            config.add_section('LOG')
            config.set('LOG', 'path', LOG_PATH)
            return LOG_PATH
        except configparser.NoOptionError:
            config.set('LOG', 'path', LOG_PATH)
            return LOG_PATH
        finally:
            with open(LOG_CONFIG_PATH, 'w') as f:
                config.write(f)
    else:
        f = open(LOG_CONFIG_PATH, 'w')
        config.add_section('LOG')
        config.set('LOG', 'path', LOG_PATH)
        config.write(f)
        f.close()
        return LOG_PATH
