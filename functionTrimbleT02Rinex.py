# -*- coding:utf-8 -*-
"""
这里不用#-*- coding: utf-8 -*-
因为该编码对汉字不支持，会出现乱码
"""

# 功能：把天宝的T02数据转换为rinex 2.11数据，包括观测数据（GPS，glonass，北斗），导航文件，气象文件
# 系统需要预先安装teqc和RUNPKR00。
# python 2.7
# by zzh_my@163.com
# 2016-01-30
# update 2017-7-9
import os
import sys
import shutil
import platform


def trimbleT02Rinex(fileName='HLDR263bA.T02', input_year='2015', hi='0.075', antNum='5311360843',
                    antType='TRM59900.00     SCIS', recNumber='5247K53946', recType='TRIMBLE NETR9', MET='y'):
    # 判断输入文件是否存在，否则返回错误
    #   print "coding by zzh_my@163.com"
    #   print "2016-01-30\n"
    shortFileName = os.path.basename(fileName)

    # 判断平台系统，不同操作系统，准备工作不一样
    sysstr = platform.system()
    programHomeDir = os.path.split(os.path.realpath(sys.argv[0]))[0]  # 获取脚本所在目录
    if (sysstr=="Windows"):
        winDir = os.getenv("windir")  # get windows os directory
        teqcDir = winDir + "\\teqc.exe"  # 欲安装功能程序的目录
        runpkr00Dir = winDir + "\\runpkr00.exe"
        programHomeDir = os.getcwd()  # 获取脚本运行目录
        programHomeTeqcDir = programHomeDir + '\\teqc.exe'  # 随程序包发布的功能程序
        programHomeRunpkr00Dir = programHomeDir + '\\runpkr00.exe'
        if (not (os.path.exists(teqcDir)) or (not (os.path.exists(runpkr00Dir)))):
            if (os.path.exists(programHomeTeqcDir) and os.path.exists(programHomeRunpkr00Dir)):
                shutil.copyfile(programHomeRunpkr00Dir, runpkr00Dir)
                shutil.copyfile(programHomeTeqcDir, teqcDir)
            else:
                print "不存在teqc和runpkr00，程序将马上退出"
                raw_input("press <enter>")  # waiting your end this
                return 0  # 出现错误
                #print "复制teqc和runpkr00到windows目录下。"


    strdos = 'runpkr00 -g -d   ' + fileName
    # print "Runpkr00 is dealing---> " + fileName
    try:
        os.popen(strdos)
    except:
        print '系统可能未安装Runpkr00，程序将终止。'
        return 0

    if (not (os.path.exists(fileName[0:len(fileName) - 4] + '.tgd'))):  # 如果未生成tgd，则会生成dat文件，后续执行会出现错误，
        print "!!!aler:Runpkr00 deal " + fileName + " fail!!!"
        if ((os.path.exists(fileName[0:len(fileName) - 4] + '.dat'))):
            os.remove(fileName[0:len(fileName) - 4] + '.dat')
        if ((os.path.exists(fileName[0:len(fileName) - 4] + '.tg!'))):
            os.remove(fileName[0:len(fileName) - 4] + '.tg!')
        return 0  # 执行失败
    # ------------------------------------------------------------
    strdos = 'teqc +relax -tr d +obs ' + fileName[0:len(fileName) - 4] + '.' + input_year[2:4] + 'o +nav ' \
             + fileName[0:len(fileName) - 4] + '.' + input_year[2:4] + 'n,' \
             + fileName[0:len(fileName) - 4] + '.' + input_year[2:4] + 'g,del.listFile,del.listFile,' \
             + fileName[0:len(fileName) - 4] + '.' + input_year[2:4] \
             + 'c +met ' + fileName[0:len(fileName) - 4] + '.' + input_year[2:4] + 'm ' \
             + ' -O.pe ' + hi + ' 0 0 -O.mn ' + shortFileName[0:4] \
             + ' -O.mo ' + shortFileName[0:4] + ' -O.an ' + antNum \
             + ' -O.at ' + '\"' + antType + '\"' \
             + ' -O.rn ' + recNumber \
             + ' -O.rt ' + '\"' + recType + '\"' \
             + ' -O.o ZZH -O.ag GCEDD +C2  ' \
             + fileName[0:len(fileName) - 4] + '.tgd'
    print "Teqc is dealing--->" + fileName[0:len(fileName) - 4] + '.T02'
    try:
        os.popen(strdos)
    except:
        print '系统可能未安装TEQC，程序将终止。'
        return 0

    # ------------------------------------
    # 读取转换后文件的O文件中的经纬度，然后再运行一遍teqc
    teqcOfile = fileName[0:len(fileName) - 4] + '.' + input_year[2:4] + 'o'
    fTeqcO = open(teqcOfile, "r")
    findTextLat = ''
    flag = 1
    while (flag):
        text_to_line = fTeqcO.readline()
        flag = flag + 1
        if 'latitude' in text_to_line:
            flag = 0
            findTextLat = text_to_line  # find latitude line
        elif flag > 100:
            try:
                os.remove(fileName[0:len(fileName) - 4] + '.tgd')
                os.remove('del.listFile')
            except:
                print '删除del.listFile文件异常'
            # os.remove('del.listFile') #需要管理员权限删除
            return 1  # 循环读取100行，但还没有找到，则跳出函数，可能O文件自带XYZ
    # 接着读取经度行，和大地高行
    findTextLong = fTeqcO.readline()
    findTextEle = fTeqcO.readline()
    # 截取字串
    findTextLat = findTextLat[0:14]
    findTextLong = findTextLong[0:14]
    findTextEle = findTextEle[0:14]

    # 关闭打开的文件
    fTeqcO.close()

    strdos = 'teqc +relax -tr d +obs ' + fileName[0:len(fileName) - 4] + '.' + input_year[2:4] + 'o +nav ' \
             + fileName[0:len(fileName) - 4] + '.' + input_year[2:4] + 'n,' \
             + fileName[0:len(fileName) - 4] + '.' + input_year[2:4] + 'g,del.listFile,del.listFile,' \
             + fileName[0:len(fileName) - 4] + '.' + input_year[2:4] \
             + 'c +met ' + fileName[0:len(fileName) - 4] + '.' + input_year[2:4] + 'm ' \
             + ' -O.pe ' + hi + ' 0 0 -O.mn ' + shortFileName[0:4] \
             + ' -O.mo ' + shortFileName[0:4] + ' -O.an ' + antNum \
             + ' -O.at ' + '\"' + antType + '\"' \
             + ' -O.rn ' + recNumber \
             + ' -O.rt ' + '\"' + recType + '\"' \
             + ' -O.o ZZH -O.ag GCEDD +C2  ' \
             + ' -O.pg ' + findTextLat + ' ' + findTextLong + ' ' + findTextEle \
             + fileName[0:len(fileName) - 4] + '.tgd'
    os.popen(strdos)
    # -------------------------------

    try:
        os.remove(fileName[0:len(fileName) - 4] + '.tgd')
        os.remove('del.listFile')
    except:
        print '删除del.listFile文件异常'
    # os.remove('del.listFile')
    return 1
