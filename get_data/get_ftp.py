#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/13 下午8:04
# @Author  : Bear Chao
# @Site    : http://blog.nickzy.com
# @File    : get_ftp.py
# @Software: PyCharm
import ftplib

def ftp_down(filename = "20120904.rar"):
    ftp=FTP()
    ftp.set_debuglevel(2)
    ftp.connect('192.168.0.1','21')
    ftp.login('admin','admin')
    #print ftp.getwelcome()#显示ftp服务器欢迎信息
    #ftp.cwd('xxx/xxx/') #选择操作目录
    bufsize = 1024
    filename = "20120904.rar"
    file_handler = open(filename,'wb').write #以写模式在本地打开文件
    ftp.retrbinary('RETR %s' % os.path.basename(filename),file_handler,bufsize)#接收服务器上文件并写入本地文件
    ftp.set_debuglevel(0)
    file_handler.close()
    ftp.quit()
    print("ftp down OK")