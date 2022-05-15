# -*- coding: utf-8 -*-
"""
====================================
@File Name ：execlog.py
@Time ： 2022/5/3 22:06
@Create by Author ： lileilei
====================================
"""
import os


def run_adb_log(dev, path):
    '''
    执行adb 获取log
    '''
    cmd = 'adb -s {} shell logcat -c'.format(dev)
    os.system(cmd)
    filepath = os.path.join(path, dev)
    cmdlog = 'adb -s {} logcat -v threadtime >{}.log'.format(dev, filepath)
    os.system(cmdlog)
