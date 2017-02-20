# -*- coding: utf-8 -*-

# python 2.7
# by zzh_my@163.com
# 重新把rinex 文件进行采样，采样间隔默认30s


import glob
import os

# whether have teqc
print "coding by zzh_my@163.com"
print "2016-02-20\n"

documentSegment = os.path.sep  ##用于返回当前平台的目录分隔符，Windows是反斜杠(\)，Linux是斜杠(/)

rinexPath = r"/home/zzh/work/data/20161201shanDongProject/zaoZhuangSubsidence/对外20161226/*/*.16o"
destinationPath = r"/home/zzh/work/gnssWork/zaoZhuangSubsidence/sdCorsRinex"
intervalVaule = "30 "


cout = 1
for fileName in glob.glob(rinexPath):  # linux:\
    shortFileName = os.path.basename(fileName)  # JAAA273E.15o
    outFile = destinationPath + documentSegment + shortFileName

    #TEQC  teqc -O.dec 30 sdtz3190.16o >  aa.16o
    print str(cout) + " 正在处理:"+shortFileName
    teqcCMD = "teqc -O.dec "+intervalVaule + " " + fileName + " > " + outFile
    os.popen(teqcCMD)
    cout += 1

print "game is end"
a = raw_input('every key end')