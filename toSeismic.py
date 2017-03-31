# -*- coding: utf-8 -*-
# python 2.7
# by zzh_my@163.com
# cteate at 2017-3-31
"""
功能：传送HLJCORS数据给地震局FTP服务器
说明：
1、本程序目前针对dqdm1500.yro形式的文件名。
2、首先把原始T02数据进行转化，压缩，按目录存放
2、把目录数据推送给地震局
程序输入参数：
        siteList：站名列表
        fileFromCatalog:要规整的文件所在根目录 r"I:\data\lncors\2016"
"""

import os
import glob
import sys
import shutil

print "coding by zzh_my@163.com"
print "2017-03-31\n"

siteListFile = r"/home/zzh/work/data/toSeismicSiteNameList.txt"
fileFromCatalog = r"/home/zzh/work/data/CORS/HLJCORS/T02_30S_24H-raw/RefData.17"  # 要整理的目录
fileOutCatalog = r"/home/zzh/temp/toSeismic"  # 整理后的根目录
yearF2 = "20"
yearF4 = "2017"

documentSegment = os.path.sep  # 用于返回当前平台的目录分隔符，Windows是反斜杠(\)，Linux是斜杠(/)
iCount = 1

for siteName4 in open(siteListFile):
    siteName4 = siteName4.strip()
    print '正在处理第' + str(iCount) + '个站:' + siteName4
    for fileName in glob.glob(fileFromCatalog + documentSegment + "*" + documentSegment + "*" + documentSegment + siteName4 + "*.T02"):   # DQLD0610.T02
        print fileName
        shortFileName = os.path.basename(fileName).lower()  # dqld0610.t02
        lengthName = int(len(shortFileName))  # 文件名长度
        year4 = yearF4  # 组装4字符年份
        doy = shortFileName[4:7]  # 组装3字符年积日

        if not os.path.exists(fileOutCatalog):  # 判断文件是否存在，返回布尔值
            print "未指定整理后的目录"
            sys.exit()  # 程序退出

        year4Catalog = fileOutCatalog + documentSegment + year4  # 判断年文件夹，不存在则创建
        if not os.path.exists(year4Catalog):
            os.makedirs(year4Catalog)

        fileOutNameCatalog = year4Catalog + documentSegment + doy  # 判断年级日文件夹，不存在则创建
        if not os.path.exists(fileOutNameCatalog):
            os.makedirs(fileOutNameCatalog)

        # 复制文件到指定的规整目录中去
        fileRinexOutFullPath = fileOutNameCatalog + documentSegment + shortFileName  # 最终的文件全地址
        shutil.copy(fileName, fileRinexOutFullPath)  # 复制完成

        # 文件转换为RINEX
        ok = functionTrimbleT02Rinex.trimbleT02Rinex(shortFileName, '2017', '0.075', '5150360403', 'TRM59900.00     SCIS', '5247K53946', 'TRIMBLE NETR9', 'y')

    iCount += 1
