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

# from QUANTAXIS.QASetting.QALocalize import log_path, setting_path
#
CONFIGFILE_PATH = '{}{}{}'.format(setting_path, os.sep, 'config.ini')


def get_config():
    config = configparser.ConfigParser()
    if os.path.exists(CONFIGFILE_PATH):
        config.read(CONFIGFILE_PATH)
        try:
            return config.get('LOG', 'path')
        except configparser.NoSectionError:
            config.add_section('LOG')
            config.set('LOG', 'path', log_path)
            return log_path
        except configparser.NoOptionError:
            config.set('LOG', 'path', log_path)
            return log_path
        finally:

            with open(CONFIGFILE_PATH, 'w') as f:
                config.write(f)

    else:
        f = open(CONFIGFILE_PATH, 'w')
        config.add_section('LOG')
        config.set('LOG', 'path', log_path)
        config.write(f)
        f.close()
        return log_path


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s >>> %(message)s',
                    datefmt='%H:%M:%S',
                    filename='{}{}onepiece-{}-.log'.format(get_config(), os.sep, str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))),
                    filemode='w',
                    )
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# formatter = logging.Formatter('QUANTAXIS>> %(message)s')
# console.setFormatter(formatter)
# logging.getLogger('').addHandler(console)
#



def log_debug(logs, ui_log = None, ui_progress = None):
    """打印debug日志
    """

    logging.debug(logs)


def log_info(logs, ui_log = None, ui_progress = None, ui_progress_int_value = None):
    """打印info日志
    """

    logging.info(logs)

#     #给GUI使用，更新当前任务到日志和进度
#     if ui_log is not None:
#         if isinstance(logs, str) :
#             ui_log.emit(logs)
#         if isinstance(logs, list) :
#             for iStr in logs:
#                 ui_log.emit(iStr)
#
#     if ui_progress is not None and ui_progress_int_value is not None:
#         ui_progress.emit(ui_progress_int_value)


def log_expection(logs, ui_log = None, ui_progress = None):
    """打印异常日志
    """

    logging.exception(logs)
