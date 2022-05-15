# -*- coding: utf-8 -*-
"""
====================================
@File Name ：apktools.py
@Time ： 2022/5/4 20:29
@Create by Author ： lileilei
====================================
"""


from androguard.core.bytecodes.apk import APK


def get_apkname(apk):
    a = APK(apk, False, "r")
    return a.get_package()


def get_apk_lanchactivity(apk):
    a = APK(apk, False, "r")
    return a.get_main_activity()