# -*- coding: utf-8 -*-
"""
====================================
@File Name ：findnewfile.py
@Time ： 2022/5/2 20:05
@Create by Author ： lileilei
====================================
"""
import os
import shutil


def new_file(testdir):
    #列出目录下所有的文件
    file_list = os.listdir(testdir)
    #对文件修改时间进行升序排列
    file_list.sort(key=lambda fn:os.path.getmtime(testdir+'//'+fn))
    return file_list[-10:-1]

def copy_file(time,path):
    new_path=os.path.join(path,time)
    if os.path.exists(new_path) is False:
        os.makedirs(new_path)
    all_file=new_file(testdir=path)
    for itemfile in all_file:
        paths=os.path.join(path,itemfile)
        try:
            shutil.copyfile(paths,os.path.join(new_path,itemfile))
        except:
            pass