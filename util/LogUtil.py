#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author   : Wades
# @Time     : 2018/10/11 3:11 PM
#
# The MIT License (MIT)
#
# Copyright (c) 2018 - 2020

# import configparser
import datetime
import os

from zenlog import logging
from util import ConfigUtil


log_config = ConfigUtil.get_log_config()
logging.basicConfig(level=log_config['LEVEL'],
                    format='%(asctime)s >>> %(message)s',
                    datefmt='%H:%M:%S',
                    filename='{}{}onepiece-{}-.log'.format(log_config['PATH'], os.sep, str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))),
                    filemode='w',
                    )

console = logging.StreamHandler()
console.setLevel(log_config['LEVEL'])
formatter = logging.Formatter('OnePiece>> %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


def log_debug(logs):
    """打印debug日志"""

    logging.debug(logs)


def log_info(logs):
    """打印info日志"""

    logging.info(logs)


def log_warn(logs):
    """打印warn日志"""

    logging.warning(logs)


def log_error(logs):
    """打印异常日志"""

    logging.error(logs)
