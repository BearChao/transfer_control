#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/12 下午10:22
# @Author  : Bear Chao
# @Site    : http://blog.nickzy.com
# @File    : Config.py
# @Software: PyCharm
from enum import Enum
import time


class DATATYPE(Enum):
    file = 1
    ftp = 2
    webDav = 3
    #>10则为数据库类型
    mysql = 11
    oracle = 12
    #todo 枚举中添加其他类型


class Config():
    """
    id:任务id
    name:任务名称
    dataType:数据来源
    dir:数据目录或者连接字符串
    username:登录用户
    password：登录密码

    """
    def __init__(self,name='',dataType=DATATYPE.file,dir='',username='',password=''):
        self.id = int(time.strftime("%Y%m%d%H%M%S", time.localtime()))
        self.name = name
        self.dataType = dataType
        self.dir = dir
        self.username = username
        self.password = password


    def isDatabase(self):
        if self.dataType >10:
            return True
        else:
            return False

    def to_dict(self):
        d = dict(
            id = self.id,
            name = self.name,
            dataType = self.dataType.value,
            dir = self.dir,
            username = self.username,
            password = self.password
        )
        return d



if __name__ == '__main__':
    conf = Config()
    print(conf.id)