#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/12 下午9:25
# @Author  : Bear Chao
# @Site    : http://blog.nickzy.com
# @File    : dict_json.py
# @Software: PyCharm
import json
import common

#config要求为一个列表，列表中为config项
from model.Config import Config, DATATYPE


def saveConfig(data):
    with open(common.CONFIGFILE,'w') as f:
        json.dump(data,f)

def loadConfig():
    with open(common.CONFIGFILE,'r') as f:
        j = json.load(f)
        n = len(j)
        return j,n

if __name__ == '__main__':

    c = Config('任务名称呦',DATATYPE.mysql)
    saveConfig(c.to_dict())
    j,n = loadConfig()
    for i in j:
        print(i,j[i])

