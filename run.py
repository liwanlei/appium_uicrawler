""" 
@author: lileilei
@file: run.py 
@time: 2018/5/6 17:32 
"""
from case.uicrawler import run
import  os,datetime
from common.log import LOG,logger
from common.execlog import run_adb_log
import multiprocessing
from common.Makecasenum import call_num
import  click
from common.apktools import get_apkname,get_apk_lanchactivity
basepth=os.getcwd()

def uicrawler():
    LOG.name = "基于Appium UI遍历测试"
    os.path.join(os.path.join(basepth, 'testlog'), 'UI-' + call_num + '.log')
    path=os.path.join(os.path.join(os.getcwd(),"installapk"),'autohome.apk')
    testapk = get_apkname(path)
    testapklanchactivity = get_apk_lanchactivity(
        path)
    path = os.path.join(os.path.join(os.getcwd(), 'testlog'), call_num)
    if os.path.exists(path) is False:
        os.mkdir(path)
    runlog = multiprocessing.Pool()
    runlog.apply_async(run_adb_log, ("RF8MC0GHRHR", path))
    run('RPG0218B26005034', testapk, '4723', 'Android', call_num,testapklanchactivity)
    runlog.close()
    runlog.terminate()

if __name__=="__main__":
    uicrawler()