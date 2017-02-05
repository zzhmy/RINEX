# -*- coding: utf-8 -*-
"""
这里不用#-*- coding: utf-8 -*-
因为该编码对汉字不支持，会出现乱码
"""
# python 2.7
# by zzh_my@163.com
# cteate at 2017-2-5
"""
功能：把不规整的RINEX文件名进行统一规整，8.3形式，例如dqdm1500.16o：
说明：
1、本程序目前仅完成dqdm150aa.16o形式的文件名规整。
2、规整后的文件替换原文件
程序输入参数：
        fileFromCatalog:要规整的文件所在根目录 r"I:\data\lncors\2016"
"""
import glob
import shutil
import os
import sys

print "coding by zzh_my@163.com"
print "2017-2-5\n"

fileFromCatalog = r"/home/zzh/work/data/CORS/HLJCORS/rinex/2016"  # 要规整的目录

documentSegment = os.path.sep  # 用于返回当前平台的目录分隔符，Windows是反斜杠(\)，Linux是斜杠(/)

iCount = 0
for fileName in glob.glob(fileFromCatalog+documentSegment+"*"+documentSegment+"*.??[oO]"):
    iCount += 1  # 循环计数
    fileDir = os.path.dirname(fileName)
    shortFileName = os.path.basename(fileName).lower()  # zhao2920.16o
    name4 = shortFileName[0:4].lower()  # zhao  站名
    lengthName = int(len(shortFileName))  # 文件名长度
    # 新的文件名
    nameNew = shortFileName[0:lengthName-6]+"0"+shortFileName[lengthName-4:lengthName]
    # os.rename(dir+os.sep+filenames[a],dir+os.sep+str(a)+'.bmp')
    fileNew = fileDir+os.sep+nameNew
    os.rename(fileName, fileNew)
    print str(iCount) + " 正在处理:" + shortFileName

print "程序运行完毕！！"
a = raw_input('按任意键结束程序！')
