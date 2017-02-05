# -*- coding: utf-8 -*-
"""
这里不用#-*- coding: utf-8 -*-
因为该编码对汉字不支持，会出现乱码
"""
# python 2.7
# by zzh_my@163.com
"""
功能：把不规整的CORS站RINEX文件进行统一规整，最终如下：
根目录rootCatalg    
    2003
       cas1
           cas10010.03o
说明：
程序分为两部分，（1）获取要规整的RINEX文件，
                            （2）读取RINEX年，站名，根据这些信息，建立目录（如果没有的话），然后把文件放入。
程序输入参数：
        fileFromCatalog:要规整的文件根目录 r"I:\data\lncors\2016"
        yearF2:整理文件的年份前2位，后两位通过文件获得

程序输出参数：
        fileOutCatalog:整理后存放数据的更目录  I:\data\lncors\rootcatalog
"""
import glob
import shutil
import os
import sys

print "coding by zzh_my@163.com"
print "2016-11-12\n"

# 参数准备
fileFromCatalog=r"/home/zzh/work/data/CORS/HLJCORS/history/2016"  # 要整理的目录
fileOutCatalog=r"/home/zzh/work/data/CORS/HLJCORS/rinex"  # 整理后的根目录
yearF2="20"

documentSegment=os.path.sep  ##用于返回当前平台的目录分隔符，Windows是反斜杠(\)，Linux是斜杠(/)
for fileName in glob.glob(fileFromCatalog+documentSegment+"*"+documentSegment+"*"+documentSegment+"*.??[oO]"):  #win10:\,fileName= I:\data\lkcors\2016\zhao2880.16o *.??[oO]
    shortFileName=os.path.basename(fileName).lower()  #zhao2920.16o
    name4=shortFileName[0:4].lower()            #zhao  站名
    lengthName=int(len(shortFileName)) #文件名长度
    year4=yearF2+shortFileName[lengthName-3:lengthName-1] #组装4字符年份
    
    #根据站名  年份 判断文件夹是否存在，如果不存在，则 建立文件夹，
    
    if not os.path.exists(fileOutCatalog): #判断文件是否存在，返回布尔值
        print "未指定整理后的目录"
        sys.exit() #程序退出
    
    year4Catalog=fileOutCatalog+documentSegment+year4  #判断年文件夹，不存在则创建
    if not os.path.exists(year4Catalog):
        os.makedirs(year4Catalog)
    
    fileOutNameCatalog=year4Catalog+documentSegment+name4 #判断站名文件夹，不存在则创建
    if not os.path.exists(fileOutNameCatalog):
        os.makedirs(fileOutNameCatalog)    
    
    #复制文件到指定的规整目录中去
    fileRinexOutFullPath=fileOutNameCatalog+documentSegment+shortFileName  #最终的文件全地址
    shutil.copy(fileName, fileRinexOutFullPath)  #复制完成
    print  "已经规整完成：" +shortFileName


print "程序运行完毕！！"
a = raw_input('按任意键结束程序！')
