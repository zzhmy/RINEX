# coding=gbk
"""
���ﲻ��#-*- coding: utf-8 -*-
��Ϊ�ñ���Ժ��ֲ�֧�֣����������
"""
# python 2.7
# by zzh_my@163.com
"""
���ܣ��Ѳ�������CORSվRINEX�ļ�����ͳһ�������������£�
��Ŀ¼rootCatalg    
    2003
       cas1
           cas10010.03o
˵����
�����Ϊ�����֣���1����ȡҪ������RINEX�ļ���
                            ��2����ȡRINEX�꣬վ����������Щ��Ϣ������Ŀ¼�����û�еĻ�����Ȼ����ļ����롣
�������������
        fileFromCatalog:Ҫ�������ļ���Ŀ¼ r"I:\data\lncors\2016"
        yearF2:�����ļ������ǰ2λ������λͨ���ļ����

�������������
        fileOutCatalog:����������ݵĸ�Ŀ¼  I:\data\lncors\rootcatalog
"""
import glob
import shutil
import os
import sys

print "coding by zzh_my@163.com"
print "2016-11-12\n"

#����׼��
fileFromCatalog=r"/home/data/data/corsRinex/cmonoc/lncors/2016"  #Ҫ�����Ŀ¼
fileOutCatalog=r"/home/data/data/corsRinex/cmonoc"  #�����ĸ�Ŀ¼
yearF2="20"

documentSegment=os.path.sep  ##���ڷ��ص�ǰƽ̨��Ŀ¼�ָ�����Windows�Ƿ�б��(\)��Linux��б��(/)
for fileName in glob.glob(fileFromCatalog+documentSegment+"*.??[oO]"):  #win10:\,fileName= I:\data\lkcors\2016\zhao2880.16o *.??[oO]
    shortFileName=os.path.basename(fileName).lower()  #zhao2920.16o
    name4=shortFileName[0:4].lower()            #zhao  վ��
    lengthName=int(len(shortFileName)) #�ļ�������
    year4=yearF2+shortFileName[lengthName-3:lengthName-1] #��װ4�ַ����
    
    #����վ��  ��� �ж��ļ����Ƿ���ڣ���������ڣ��� �����ļ��У�
    
    if not os.path.exists(fileOutCatalog): #�ж��ļ��Ƿ���ڣ����ز���ֵ
        print "δָ��������Ŀ¼"
        sys.exit() #�����˳�
    
    year4Catalog=fileOutCatalog+documentSegment+year4  #�ж����ļ��У��������򴴽�
    if not os.path.exists(year4Catalog):
        os.makedirs(year4Catalog)
    
    fileOutNameCatalog=year4Catalog+documentSegment+name4 #�ж�վ���ļ��У��������򴴽�
    if not os.path.exists(fileOutNameCatalog):
        os.makedirs(fileOutNameCatalog)    
    
    #�����ļ���ָ���Ĺ���Ŀ¼��ȥ
    fileRinexOutFullPath=fileOutNameCatalog+documentSegment+shortFileName  #���յ��ļ�ȫ��ַ
    shutil.copy(fileName, fileRinexOutFullPath)  #�������
    print  "�Ѿ�������ɣ�" +shortFileName


print "����������ϣ���"
a = raw_input('���������������')
