# -*- coding: utf-8 -*-
"""
====================================
@File Name ：configuntil.py
@Time ： 2022/5/2 07:47
@Create by Author ： lileilei
====================================
"""
import yaml


class Parse(object):
    def __init__(self, filepath):
        self.filepath = filepath
        self.reslut = {}
        self.reslut = self.__init()

    def __init(self):
        file = open(self.filepath, 'r', encoding="utf-8")
        file_data = file.read()
        file.close()
        self.reslut = yaml.load(file_data)
        return self.reslut

    def getlogin(self):
        return self.reslut['LOGINELEMENT']

    def getgeneral(self):
        return self.reslut['GENERAL']

    def getlist(self):
        return self.reslut['LIST']

    def get_tar(self):
        return self.getlist()['ANDROID_BOTTOM_TAB_BAR_ID']

    def get_text_input(self):
        return self.getlist()['INPUT_CLASS_LIST']

    def get_sendText(self):
        return self.getlist()['INPUT_TEXT_LIST']

    def get_back(self):
        return self.getlist()['PRESS_BACK_TEXT_LIST']
    def get_back_packname(self):
        return self.getlist()['PRESS_BACK_PACKAGE_LIST']

    def get_activity(self):
        return self.getlist()['PRESS_BACK_ACTIVITY_LIST']

    def get_block(self):
        return self.getlist()['ITEM_BLACKLIST']

    def get_white(self):
        return self.getlist()['ITEM_WHITE_LIST']

    def get_not_click(self):
        return self.getlist()['ANDROID_EXCLUDE_TYPE']

    def get_ios_bar(self):
        return self.getlist()['IOS_EXCLUDE_BAR']

    def get_run_time(self):
        return self.getgeneral()['RUNNING_TIME']

    def get_ignor_crash(self):
        return self.getgeneral()['IGNORE_CRASH']

    def get_find_element_wait(self):
        return self.getgeneral()['INTERVAL_SEC']

    def get_find_element_timeout(self):
        return self.getgeneral()['DEFAULT_WAIT']

    def get_click_ccont(self):
        return self.getgeneral()['MAX_CLICK_COUNT']

    def get_max_deep(self):
        return self.getgeneral()['MAX_DEPTH']

    def crashPic(self):
        return self.getgeneral()['CRASH_PIC_COUNT']

    def screen(self):
        return self.getgeneral()['SCREENSHOT_COUNT']

    def vido(self):
        return self.getgeneral()['VIDEO']

    def issceern(self):
        return self.getgeneral()['SCREEN_SHOT']
    def opearlogin(self):
        all_login=[]
        reslut=self.getlogin()['LOGIN_ELEMENTS_ANDROID']
        for item in reslut:
            for key,value in item.items():
                all_login.append(value)
        return all_login

    def getmonkeyConfig(self):
        return self.reslut['MONKEYCONFIG']

    def auto_loggin(self):
        return  self.getlogin()['AUTOLOGIN']

    def  scoreauto(self):
        return  self.getgeneral()['SCPRE_AUTO']

    def autoscorecount(self):
        return  self.getgeneral()['SCPRE_NUM']
