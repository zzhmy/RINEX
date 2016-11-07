# coding=gbk
"""
这里不用#-*- coding: utf-8 -*-
因为该编码对汉字不支持，会出现乱码
"""
# python 2.7
# by zzh_my@163.com

# import shutil
import glob
import os

# import functionTrimbleT02Rinex

# whether have teqc
print "coding by zzh_my@163.com"
print "2016-01-30\n"

# fileOut=open('tempRAW.txt','w+')
#                           I:\to龙江局LNCORS_30s数据\RINEX211_1H_30S\RefData.15\Month.Aug\Day.01
lastFile=""
for fileName in glob.glob(r"/mnt/doc2/RINEX211_1H_30S/RefData.16/*/*/*.16o"):  # linux:\
    #print fileName
    # ok = functionTrimbleT02Rinex.trimbleT02Rinex(name, '2016', '0.075', '5311360843', 'TRM59900.00     SCIS', '5247K53946', 'TRIMBLE NETR9', 'y')
    # print >>fileOut,name vv
    shortFileName = os.path.basename(fileName) # JLSL273E.15o
    pathName = os.path.dirname(fileName) #/mnt/doc2/RINEX211_1H_30S/RefData.15/Month.Sep/Day.16

    fileName4=shortFileName[0:4]
    if lastFile==fileName4:     #如果文件名相同，则下一个循环
        continue

    fileName7=shortFileName[0:7]+"[A-X].16o"
    beforeFile=pathName + '/' + fileName7
# /mnt/share/temp/teqctest
    afterDoc=r"/mnt/share/temp/teqctest"  #指定输出目录
    afterFile=afterDoc + '/' +shortFileName[0:7].lower()+"0.16o"

    #teqc
    teqcCMD="teqc "+beforeFile+" > "+afterFile
    #print teqcCMD
    os.popen(teqcCMD)


    #####
    # os.rename(fileName, hebingName)
    lastFile=fileName4

print "game is end"
a = raw_input('every key end')