# -*- coding:utf-8 -*-
"""
这里用#-*- coding: utf-8 -*-
否则pycharm输出对汉字不支持，会出现乱码
"""
# python 2.7
# by zzh_my@163.com
"""
功能：把RINEX文件头中的XYZ坐标信息进行标准化。
采用TEQC生成的S文件进行RINEX头坐标信息的替换。
"""
import os
import shutil
import glob
import sys
# whether have teqc
print "coding by zzh_my@163.com"
print "2016-01-30\n"

documentSegment=os.path.sep  ##用于返回当前平台的目录分隔符，Windows是反斜杠(\)，Linux是斜杠(/)
mydir = os.getcwd()  # check current directory
print "这是您当前的目录: " + mydir

# inquiry whether change directory
mydirAnswer = raw_input("你是否想改变这个目录??  n/y: ")  # beloew python 3.0,function is raw_input;above python 3.0,function is input.would you want to change directory
print mydirAnswer
mydirAnswer = mydirAnswer.lower()  # all change to lower-case
if mydirAnswer == 'y':
    mydir = raw_input("请输入您的全目录: ")  # please input your full direcorty
    print "您输入的目录是: " + mydir  # you input directory is
elif mydirAnswer == 'n':
    print "您输入的目录是 : " + mydir
# change directory is end

os.chdir(mydir)  # change directory
print "这是您的工作目录: " + os.getcwd()
# inqure whether quit,if input "y",quit
quit_inqure = raw_input("您打算退出程序吗? n/y: ")
if quit_inqure.lower() == 'y':
    print "您将会退出程序"
    raw_input("press <enter>")  # waiting your end this
    raise SystemExit

#判断是否存在TEQC
winDir = os.getenv("windir")  # get windows os directory
# programHomeDir=os.getcwd() #获取脚本运行目录
programHomeDir = os.path.split(os.path.realpath(sys.argv[0]))[0]  # 获取脚本所在目录
teqcDir = winDir + "\\teqc.exe"  # 欲安装功能程序的目录
programHomeTeqcDir = programHomeDir + '\\teqc.exe'  # 随程序包发布的功能程序

if (not (os.path.exists(teqcDir)) ):
    if (os.path.exists(programHomeTeqcDir) ):
        print "复制teqc和runpkr00到windows目录下。"
        #     (programHomeTeqcDir,teqcDdir)
        shutil.copyfile(programHomeTeqcDir, teqcDir)
    else:
        print "不存在teqc，程序将马上退出"
        raw_input("press <enter>")  # waiting your end this
        raise SystemExit  # 出现错误

for fileName in glob.glob(r"D:\temp\teqcS\*.16o"):  #win10:\
    shortFileName = os.path.basename(fileName)
    filePathDIR=os.path.dirname(fileName)
    #生成S文件
    strdos =' teqc +qc '+fileName
    print "Teqc is dealing--->" + shortFileName
    os.popen(strdos)
    #提取S文件XYZ坐标
    teqcSfile =filePathDIR + documentSegment + shortFileName[0:len(shortFileName) - 1] + 'S'
    fTeqcS = open(teqcSfile, "r")
    findTextXYZ = ''
    flag = 1
    while (flag):
        text_to_line = fTeqcS.readline()
        flag = flag + 1
        if 'antenna WGS 84 (xyz)' in text_to_line:
            flag = 0
            findTextXYZ = text_to_line  # find xyz line
        elif flag > 100:
            print '在'+teqcSfile+'文件中未找到坐标，请核对'
            raise SystemExit  # 出现错误
    # 关闭打开的文件
    fTeqcS.close()
    findTextXYZ = findTextXYZ[25:66]
    #利用提取的XYZ生成新的临时O文件
    FileNameTEMP=filePathDIR + documentSegment +shortFileName+'.tmp'
    strdos='teqc -O.px '+findTextXYZ+' ' +fileName +' > '+FileNameTEMP
    os.popen(strdos)
    #删除原O文件，把临时文件改名
    os.remove(fileName)
    os.remove(teqcSfile)
    os.rename(FileNameTEMP, fileName)

print "程序运行完毕！！"
a = raw_input('按任意键结束程序！')