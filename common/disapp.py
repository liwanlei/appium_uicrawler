""" 
@author: lileilei
@file: disapp.py 
@time: 2018/1/19 11:10 
"""
'''
从配置文件获取相关的app测试配置信息
'''
from config import *


def make_dis(platformName, platformVersion, deviceName,package,activity):
    dis_app = {}
    dis_app['platformName'] = platformName
    dis_app['platformVersion'] = platformVersion
    dis_app['deviceName'] = deviceName
    dis_app['appPackage'] = package
    dis_app['appActivity'] = activity
    dis_app['androidDeviceReadyTimeout'] = TestandroidDeviceReadyTimeout
    dis_app['unicodeKeyboard'] = TestunicodeKeyboard
    dis_app['resetKeyboard'] = TestresetKeyboard
    dis_app['noReset'] = True
    return dis_app
