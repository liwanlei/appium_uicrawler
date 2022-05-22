# -*- coding: utf-8 -*-
"""
====================================
@File Name ：unitil.py
@Time ： 2022/5/1 21:27
@Create by Author ： lileilei
====================================
"""
import platform, os
import random
import re

from androguard.core.bytecodes.apk import APK

nativeKey = "Native Heap"
dalKey = "Dalvik Heap"
totalKey = "TOTAL"
fpskey = "FPS"
net = "net"


def checkPackeExit(uid, processname: str, isAndroid: bool = False):
    if processname is None or processname == "":
        return False
    processname = processname.lower()
    grep = isgrep()
    if isAndroid:
        cmd = 'adb -s {}'.format(uid) + " shell ps | " + grep + " " + processname
        pid_line = os.popen(cmd).readlines()
        if len(pid_line.__str__().lower().split("\n")) > 2:
            return False
        else:
            pid_line = [str(i).split("\n")[0] for i in pid_line]
            for item in pid_line:
                if processname in str(item).split(" "):
                    return True
            else:
                return False


def isgrep():
    '''
    判断系统
    '''
    if platform.system().lower().__contains__("wind"):

        grep = 'findstr'
    else:
        grep = 'grep'
    return grep


def perform_home(dev):
    '''
    实现home键操作
    '''
    cmd = 'adb -s {} shell input keyevent 3'.format(dev)
    os.system(cmd)


def perform_back(dev):
    '''
    实现返回键
    '''
    cmd = 'adb -s {}  shell input keyevent 4'.format(dev)
    os.system(cmd)

def perform_audio(dev):
    '''
    调整音量
    '''

    autocmd='adb -s {}  shell input keyevent '.format(dev)
    allaudio=[autocmd+str(i) for i in range(24,26)]
    weight=[1,1]
    result = random.choices(population=allaudio, weights=weight)[0]
    os.system(result)


def retonescreen(dev):
    '''旋转屏幕'''
    randstr = 'adb -s {} shell content insert --uri content://settings/system --bind name:s:user_rotation --bind value:i:'.format(
        dev)
    addlist = [randstr + str(i) for i in range(4)]
    choice = [1, 1, 1, 1]
    result = random.choices(population=addlist, weights=choice)[0]
    os.system(result)


def getMobileInfo(serial):
    '''
    获取设备信息
    '''
    all = {
        "HUAWEI": "ro.build.version.emui",
        "vivo": "ro.vivo.os.build.display.id",
        "samsung": "ro.build.version.release",
        "Xiaomi": "ro.build.version.incremental",
        "OPPO": "ro.build.version.opporom",
        "360": "ro.build.display.id",
        "LENOVO": "ro.build.display.id",
        "smartisan": "ro.build.display.id",
        "Sony": "ro.build.display.id",
        "K-TOUCH": "ro.build.display.id",
        "SHARP": "ro.build.display.id",
        "Amazon": "ro.build.display.id",
        "Google": "ro.build.display.id",
        "LGE": "ro.build.display.id",
        "YuLong": "ro.build.display.id",
        "lephone": "ro.build.display.id",
        "GiONEE": "ro.build.display.id",
        "Meizu": "ro.build.display.id",
        "motorola": "ro.build.display.id",
        "Letv": "ro.build.display.id",
    }
    model = os.popen('adb -s %s shell getprop ro.product.model' % serial).read().replace('\n', '')
    brand = os.popen('adb -s %s shell getprop ro.product.brand' % serial).read().replace('\n', '')
    version = os.popen('adb -s %s shell getprop  ro.tools.version.release' % serial).read().replace('\n', '')
    kernel = os.popen('adb -s %s shell cat /proc/version' % serial).read()
    serialno = os.popen('adb -s %s shell getprop  ro.serialno' % serial).read().replace('\n', '')
    sdk = os.popen('adb -s %s shell getprop  ro.tools.version.sdk' % serial).read().replace('\n', '')
    try:
        newKernel = re.findall("Linux version (.*?) \(", kernel)[0] + '#' + re.findall("#(.*)", kernel)[0]
    except:
        newKernel = ''
    try:
        rom = os.popen('adb -s %s shell getprop  %s' % (serial, all[brand])).read().replace('\n', '')
    except:
        rom = os.popen('adb -s %s shell getprop  ro.tools.display.id' % serial).read().replace('\n', '')
    if (str(brand).lower() == 'xiaomi'):
        rom_verison = os.popen('adb -s %s shell "getprop | grep ro.build.version.incremental"' % serial).read().strip()
        rom_verison = (re.match('\[ro.build.version.incremental\]: \[(.*)\]', rom_verison).group(1))
    else:
        rom_verison = 'unknown'
    return model, version, newKernel, serialno, brand, sdk, rom, rom_verison


def getversion(dev):
    '''
    获取系统版本
    '''
    devverions = os.popen('adb -s {}  shell getprop ro.build.version.release'.format(dev)).readlines()
    platform_version = (devverions[0].split('\n')[0])
    return platform_version


def getactivity(filepath, apkname):
    all_list_activity = []
    apk = APK(filepath)
    elements = apk.find_tags_from_xml('AndroidManifest.xml', 'activity')
    for item in elements:
        for key, value in item.attrib.items():
            if str(key).endswith("name") and str(value).startswith(apkname):
                all_list_activity.append(value)
    return all_list_activity
