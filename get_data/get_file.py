#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/13 下午8:48
# @Author  : Bear Chao
# @Site    : http://blog.nickzy.com
# @File    : get_file.py
# @Software: PyCharm
import os
import shutil
from common import LOGS, file_sender
from distutils.dir_util import copy_tree


def isFolder(dir):
    return os.path.isdir(dir)

def getFileNames(rootDir):
    list = []
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for f in files:
            file = os.path.join(root, f)
            list.append(file)
    return list

def getFile(item):
    '''
    复制指定文件
    :param item: item.dir要求必须为绝对路径
    :return: 已复制文件的相对路径
    '''
    files = []
    if isFolder(item.dir):
        copy_tree(item.dir, 'temp/' ) # 目录的复制
        orgFiles = getFileNames(item.dir)
        rootLen = len(item.dir)
        files = list(map(lambda x:'temp/'+x[rootLen:],orgFiles))
        file_sender.rename(files,item.id)

    else:
        shutil.copy(item.dir, 'temp')  # 文件拷贝，src必须是一个文件，dst可以是一个文件或者目录
        files.append('temp/'+os.path.basename(item.dir))
        file_sender.rename(files,item.id)
    LOGS.info("文件复制完成："+item.dir)
    return files

