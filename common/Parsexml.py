# -*- coding: utf-8 -*-
"""
====================================
@File Name ：Parsexml.py
@Time ： 2022/5/1 18:12
@Create by Author ： lileilei
====================================
"""
import difflib
import os
import time
from datetime import datetime, timedelta
from time import sleep

from selenium.common.exceptions import StaleElementReferenceException
from common.unitil import perform_back
from common.pictools import imagetovideo
from common.configuntil import *
from lxml import etree

from common.findnewfile import copy_file
from common.htmlreport import title
from common.log import LOG
import random

from common.unitil import getMobileInfo

'''
解析页面元素，并且执行
'''


class Excuption(object):
    def __init__(self, filepath, dev, path, activity):
        self.click_activity_dict = {}
        self.packname = []
        self.userLoginCount = 0
        self.currentDepth = 0
        self.parse = Parse(filepath)
        self.get_find_element_timeout = self.parse.get_find_element_timeout()
        self.runtime = self.parse.get_run_time()
        self.stop = False
        self.pressBackActivityList = self.parse.get_activity()
        self.pressBackPackageList = self.parse.get_back_packname()
        self.get_block = self.parse.get_block()
        self.get_back = self.parse.get_back()
        self.maxDepth = self.parse.get_max_deep()
        self.ignoreCrash = self.parse.get_ignor_crash()
        self.timewait = self.parse.get_find_element_wait()
        self.not_click = self.parse.get_not_click()
        self.tabbarxpath = []
        self.whitelist = self.parse.get_white()
        self.creatvideo = self.parse.vido()
        self.scoreauto = self.parse.scoreauto()
        self.scoreautonum = self.parse.autoscorecount()
        self.scorealready = 0
        self.dev = dev
        self.path = path
        self.not_link = 0
        self.activity = activity

    def run(self, deriver, starttime, andriod, apckane, curents):
        LOG.name = "UI遍历测试"
        '''
        1.获取所有的元素xpath
        2.进行遍历，如果元素是input，进行输入
        3.遍历到新的页面，在新的页面进行遍历
        4.遍历后，添加点击的xpath
        '''
        LOG.info("遍历开始")
        self.currentDepth = curents
        login = self.parse.auto_loggin()
        currntxml = deriver.page_soucre()
        if login is True:
            if (self.userLoginCount == 0):
                self.login(deriver)
            elif (self.userLoginCount < 5):
                self.login(deriver)
        self.showTabBarElement(xml_str=currntxml)
        endtime = time.time()
        if ((endtime - starttime) > self.runtime * 60):
            LOG.info("即将测试结束")
            self.stop = True

        allnode = self.xpath_list(currntxml, apckane)
        length = len(allnode) - 1
        LOG.info("当前节点的长度{}".format(str(length)))
        paege = deriver.get_wiow_size()
        width_wind = paege['width']
        heigth_wind = paege['height']
        if self.stop:
            return
        activity = deriver.current_activity()
        LOG.info("当前activity：{}".format(str(activity)))
        if len(self.pressBackActivityList) > 0:
            if activity in self.pressBackActivityList:
                deriver.take_screen(self.path)
                self.back(andriod, self.dev,width_wind,heigth_wind,True)
        packname = self.get_xml_packagename(xml_str=currntxml, andrioid=andriod)
        if apckane != packname:
            if apckane in self.pressBackPackageList:
                self.back(andriod, self.dev,width_wind,heigth_wind,True)
            else:
                # 如果当前的包名不是在返回的apk，这里应该认为崩溃
                #   整理这里的图片
                LOG.info("崩溃了，需要截图")
                deriver.take_screen(self.path)
                copy_file((datetime.now() + timedelta()).strftime("%Y_%m_%d_%H_%S_%M"), self.path)
                deriver.launch_app()
                sleep(10)
                self.run(deriver, starttime, andriod, apckane, self.currentDepth)
        self.currentDepth += 1
        if (self.currentDepth > self.maxDepth):
            LOG.info("遍历深度过预期")
            self.stop = True
            return
        while length < 1 or self.stop is False:
            activity = deriver.current_activity()
            if activity in self.pressBackActivityList:
                self.back(andriod, self.dev, deriver, width_wind, heigth_wind, True)
            if ((endtime - starttime) > self.runtime * 60):
                self.stop = True
            try:
                xpath_all = allnode[length]
            except:
                break
            update = self.updateactivy(activity, xpath_all['xpath'])
            if self.not_link > 10:
                self.back(andriod, self.dev, deriver, width_wind, heigth_wind, True)
                self.not_link = 0
            if update is False:
                length -= 1
                allnode.remove(xpath_all)
            else:
                if len(self.get_back) > 0:
                    for key in self.get_back:
                        if str(xpath_all['xpath']).__contains__(key):
                            LOG.info(self.get_back)
                            deriver.take_screen(self.path)
                            self.back(andriod, self.dev, deriver, width_wind, heigth_wind, True)
                            allnode.remove(xpath_all)
                            break
                sleep(self.timewait)
                if xpath_all['xpath'] != "":
                    LOG.info(xpath_all['xpath'])
                    element = deriver.find_ele('xpath', xpath_all['xpath'], self.get_find_element_timeout)
                    if element is not None:
                        for key in self.parse.get_text_input():
                            if xpath_all['xpath'].__contains__(key):
                                text = self.parse.get_sendText()
                                send = random.choices(text, k=1)
                                deriver.sendkeys(element, send)
                        else:
                            try:
                                deriver.take_screen(self.path)
                                element.click()
                            except StaleElementReferenceException as e:
                                self.not_link += 1
                            deriver.take_screen(self.path, xpath_all['bound'])
                            after = deriver.page_soucre()
                            if self.is_same_page(currntxml, after) is False:
                                self.run(deriver, starttime, andriod, apckane, self.currentDepth)
                length -= 1
                try:
                    allnode.remove(xpath_all)
                except:
                    pass
        if length < 0:
            if len(self.tabbarxpath) > 0:
                self.tabbarxpath.remove(self.tabbarxpath[0])
            if self.scoreauto and self.scorealready < self.scoreautonum:
                deriver.socrae()
                self.scorealready += 1
                after = deriver.page_soucre()
                if self.is_same_page(currntxml, after) is False:
                    self.run(deriver, starttime, andriod, apckane, self.currentDepth)
                else:
                    if len(self.tabbarxpath) > 0:
                        weights = [1 for x in range(len(self.tabbarxpath))]
                        xpath_tar = random.choices(self.tabbarxpath, weights=weights, k=1)[0]
                        element = deriver.find_ele('xpath', xpath_tar['xpath'], self.get_find_element_timeout)
                        if element is not None:
                            element.click()
                            deriver.take_screen(self.path, xpath_tar['bound'])
                            after = deriver.page_soucre()
                            if self.is_same_page(currntxml, after) is False:
                                self.run(deriver, starttime, andriod, apckane, self.currentDepth)

    def back(self, adnriod, dev, deriver, width, height, left):

        if adnriod:
            perform_back(dev)
        else:
            startx = 0
            endx = width / 2
            if left:
                startx = width / 2
                endx = 0
            starty = height / 2
            endy = starty
            if not adnriod:
                if left:
                    startx = 0
                    endx = 750
                else:
                    startx = 750
                    endx = -750

                starty = 50
                endy = 0
            deriver.swpape(startx, starty, endx, endy)

    def updateactivy(self, activity, xpath):
        for key in self.whitelist:
            if xpath.__contains__(key):
                return True
        if activity in self.click_activity_dict.keys():
            if xpath in self.click_activity_dict[activity]:
                return False
            else:
                self.click_activity_dict[activity].append(xpath)
                return True
        else:
            self.click_activity_dict[activity] = [xpath]
            return True

    def login(self, deriver):
        login = self.parse.opearlogin()
        for item in login:
            element = deriver.find_ele('xpath', item['XPATH'], self.get_find_element_timeout)
            if item['ACTION'] == "input":
                element.clear()
                element.send_keys(item['VALUE'])
            elif item['ACTION'] == 'click':
                element.click()
            sleep(self.parse.get_find_element_wait())
        self.userLoginCount += 1

    def xpath_list(self, xml_str, apckane):
        allxpath = []
        mytree = etree.HTML(xml_str.split("<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>")[1])
        xpath = ""
        for j in mytree.xpath('//*[@package="{}"]'.format(apckane)):
            if j.attrib.get("class") not in self.not_click:
                xpath += "//" + j.attrib.get("class") + "["
                stringbound = j.attrib.get('bounds')
                for key, value in j.attrib.items():
                    if key not in ['selected', 'bounds', 'class', 'checked', 'checkable', 'focusable', 'enabled',
                                   'long-clickable', 'scrollable', 'displayed', 'clickable', 'focused', 'password']:
                        xpath += "@" + key + "=\"" + value + "\"" + ' and '
                xpath = xpath[:-5]
                xpath += ']'
                temp_list = {"xpath": xpath, "bound": stringbound}
                if temp_list not in self.tabbarxpath:
                    allxpath.append(temp_list)
                xpath = ""
        return allxpath

    def get_xml_packagename(self, xml_str, andrioid):
        mytree = etree.HTML(xml_str.split("<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>")[1])
        if andrioid:
            appNameXpath = "(//*[@package!=''])[1]"
        else:
            appNameXpath = "//*[contains(@type,\"Application\")]"
        return mytree.xpath(appNameXpath)[0].get("package")

    def is_same_page(self, before, after):
        seq = difflib.SequenceMatcher(None, before, after)
        ratio = seq.quick_ratio()
        if ratio > 0.9:
            return True
        return False

    def showTabBarElement(self, xml_str):
        tabBarElemnt = self.parse.get_tar()
        mytree = etree.HTML(xml_str.split("<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>")[1])
        for j in mytree.xpath('//*[%s]' % (tabBarElemnt)):
            xpath = ''
            if j.attrib.get("class") not in self.not_click:
                xpath += "//" + j.attrib.get("class") + "["
                stringbound = j.attrib.get('bounds')
                for key, value in j.attrib.items():
                    if key != 'class' or key != 'bounds' or key != 'selected':
                        xpath += "@" + key + "=\"" + value + "\"" + ' and '
                xpath = xpath[:-5]
                xpath += ']'
                temp_list = {"xpath": xpath, "bound": stringbound}
                self.tabbarxpath.append(temp_list)

    def createreport(self):
        model, version, newKernel, serialno, brand, sdk, rom, rom_verison = getMobileInfo(self.dev)
        self.reslut = ""
        self.reslut = ""
        run_count = 0
        for key, value in self.click_activity_dict.items():
            self.reslut += "<p>操作的：activity {} 点击次数:{}".format(key, len(value))
            run_count += len(value)
            self.reslut += "</p>"
        titles = title("基于Appium UI遍历测试")
        conect = '''<div class="row " style="margin:60px">
                        <div style='    margin-top: 5%;' >
                         <table class="table table-hover table-condensed table-bordered" style="word-wrap:break-word;">
                    <tr > <td><strong>设备</strong></td><td>{}</td></tr>
                <td><strong>厂商</strong></td><td>{}</td></tr>
                   <tr > <td><strong>系统版本</strong></td><td>{}</td></tr>
                   <tr > <td><strong>测试apk</strong></td><td>{}</td></tr>
                   <tr > <td><strong>启动activty：</strong></td><td>{}</td></tr>
                   <tr >  <td><strong>测试时间：</strong></td><td>{}</td></tr>
             <tr >  <td><strong>操作次数：</strong></td><td>{}</td></tr>
                    <tr >  <td><strong>操作详情：</strong></td><td>{}</td></tr>
                        '''.format(self.dev, brand, rom,
                                   self.packname, self.activity, self.runtime, str(run_count), self.reslut)
        reslut = titles + conect
        file = self.reportfile()
        with open(file, 'a+', encoding='utf-8') as f:
            f.write(reslut)
        if self.creatvideo:
            self.video()

    def reportfile(self):
        self.repost_html = os.path.join(self.path, self.dev + ".html")
        return self.repost_html

    def video(self):
        for item in os.listdir(self.path):
            if os.path.isdir(item):
                path = os.path.join(self.path, item)
                runitem = os.path.join(self.path, item + "_crash.mp4")
                imagetovideo(path, runitem)
        run = os.path.join(self.path, self.dev + "_all.mp4")
        imagetovideo(self.path, run)
