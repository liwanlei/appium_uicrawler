# -*- coding: utf-8 -*-
"""
====================================
@File Name ：uicrawler.py
@Time ： 2022/5/1 18:11
@Create by Author ： lileilei
====================================
"""
import os.path
from appium import webdriver
from common.Parsexml import Excuption
from common.disapp import make_dis
import time

from common.webdriverencapsulation import deriver_encapsulation
from common.log import LOG
from common.unitil import getversion


def run(dev, apknamne, port, Testplatform, call_num,activity):
    path = os.path.join(os.path.join(os.path.join(os.getcwd(), "testreport"), call_num), dev)
    if os.path.exists(path) is False:
        os.makedirs(path)
    file = os.path.join(os.path.join(os.getcwd(), 'file'), 'config.yaml')
    LOG.name = "基于Appium UI遍历测试"
    platform_version = getversion(dev)
    starttime = time.time()
    dis_app = make_dis(Testplatform, platform_version, dev,apknamne,activity)
    LOG.info(dis_app)
    deriver = webdriver.Remote('http://localhost:{}/wd/hub'.format(str(port)), dis_app)
    time.sleep(10)
    derivernew = deriver_new(deriver)
    excuptionUICrawler = Excuption(file, dev, path)
    excuptionUICrawler.run(derivernew, starttime, True, apknamne, 0)
    excuptionUICrawler.createreport()
