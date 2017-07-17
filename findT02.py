# -*- coding: utf-8 -*-
# python 2.7
# by zzh_my@163.com
# create at 2017-3-31
"""
功能：把需要查找的天宝原始文件或标准RINEX文件复制到指定文件夹；
程序输入参数：
        site_list_file：站名列表；
        find_type:要查找的文件类型；
        doy_start:开始年积日
        doy_end:结束年积日
        find_name_is_up_case:要查找的文件名是否为大写；
        file_from_catalog:要查找的文件所在目录 ；
        file_out_catalog：存放找到的文件目录；
"""
import os
import functionFindGetFile

print "coding by zzh_my@163.com"
print "2017-03-31\n"

siteListFile = r"/home/zzh/work/data/data/CORS/HLJCORS/toSeismicSiteNameList86.txt"
findType = "*.16d.gz"  # "*.16o"  "*.T02"
doy_start = '001'
doy_end = '366'
name_up = 'n'
fileFromCatalog = r"/home/zzh/work/data/data/CORS/HLJCORS/rinexD/2016"  # 要查找的目录
fileOutCatalog = r"/home/zzh/temp/test"  # 存放找到的文件目录

# findPath = fileFromCatalog    # 0 level
findPath = fileFromCatalog + os.sep + '*'   # 1 level
# findPath = fileFromCatalog + os.sep + '*' + os.sep + '*'   # 2 level

ok = functionFindGetFile.find_get_trimble_or_rinex_file(siteListFile, findType, doy_start, doy_end, name_up, findPath,
                                                        fileOutCatalog)


