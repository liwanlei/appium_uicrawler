# -*- coding: utf-8 -*-
"""
====================================
@File Name ：pictools.py
@Time ： 2022/5/4 15:23
@Create by Author ： lileilei
====================================
"""
import os
import cv2
from PIL import Image


def opear(image_path, bound):
    '''
    操作图片，给图片画坐标，实现点击的位置
    '''
    image = cv2.imread(image_path)
    first_point = (str(bound)[1:-1].split("][")[0])
    last_point = (str(bound)[1:-1].split("][")[1])
    c1, c2 = (int(first_point.split(",")[0]), int(first_point.split(",")[1])), \
             (int(last_point.split(",")[0]), int(last_point.split(",")[1]))
    try:
        cv2.rectangle(image, c1, c2, (0, 255, 0), 2)
        cv2.imwrite(image_path, image)
    except:
        pass


def imagetovideo(filepath, videofile):
    '''
    图片转视频
    '''
    allfile = os.listdir(filepath)
    if len(allfile)>0:
        allfile.sort(key=lambda fn: os.path.getmtime(filepath + '//' + fn))
        fps = 5 #帧率
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 用于mp4格式的生成
        image = Image.open(os.path.join(filepath, allfile[0]))
        videowriter = cv2.VideoWriter(videofile, fourcc, fps, image.size)#设置
        for itemfile in allfile:

            path = os.path.join(filepath, str(itemfile))
            if os.path.isfile(path):
                frame = cv2.imread(path)
                videowriter.write(frame)
        videowriter.release()#释放
        cv2.destroyAllWindows()#销毁
