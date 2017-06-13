#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/12 下午9:13
# @Author  : Bear Chao
# @Site    : http://blog.nickzy.com
# @File    : run_sender.py
# @Software: PyCharm
import sys

from common import LOGS
from common.file_sender import sendFile



def run(id):
    LOGS.info('开始任务：'+str(id))
    sendFile("ls")

if __name__ == '__main__':

    if len(sys.argv) > 1:
        id = int(sys.argv[1])
        run(id)
    else:
        LOGS.error('参数错误,未提供任务id' )
        exit(-1)