""" 
@author: lileilei
@file: Makecasenum.py 
@time: 2018/5/13 16:43 
"""
import datetime
import hashlib


def make_md5(make_user):
    md5make = hashlib.new('md5', make_user.encode('utf-8')).hexdigest()
    return md5make
call_num = make_md5(datetime.datetime.now().strftime('%Y-%m-%d-%H:%M'))
