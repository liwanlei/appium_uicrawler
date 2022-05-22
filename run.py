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


@click.group()
def cli():
    pass


@click.command()
def uicrawler():
    LOG.name = "基于Appium UI遍历测试"
    log = os.path.join(os.path.join(basepth, 'testlog'), 'UI-' + call_num + '.log')
    testapk = get_apkname("/Users/lileilei/Desktop/testplan/pc_clicent_new/installapk/autohome.apk")
    testapklanchactivity = get_apk_lanchactivity(
        "/Users/lileilei/Desktop/testplan/pc_clicent_new/installapk/autohome.apk")
    path = os.path.join(os.path.join(os.getcwd(), 'testlog'), call_num)
    if os.path.exists(path) is False:
        os.mkdir(path)
    runlog = multiprocessing.Pool()
    runlog.apply_async(run_adb_log, ("RF8MC0GHRHR", path))
    run('RPG0218B26005034', testapk, '4723', 'Android', call_num,testapklanchactivity)
    runlog.close()
    runlog.terminate()
cli.add_command(uicrawler)

if __name__=="__main__":

    cli()