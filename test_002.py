#!/bin/python3.8
# -*- coding: utf-8 -*-
import ftplib
import os
import glob
import shutil
# pip install hazm  --  zipfile
# apt install liblzma-dev -- for compression
import zipfile
from datetime import datetime
from os.path import basename
cur_date = datetime.now().date()
d = dict(	Ираэросервис_ООО="ira", 
			Региональный_центр_бронирования='rcb',
			Регион24="r24")
for i in glob.glob("/mnt/c/Users/seligenenko/port/*.xml"):
    print(i)
    for q in d:
        with open(i, 'r') as f:
            if q.replace("_", " ") in f.read():
                try:
                    if d[q] == 'r24':
                        with open(i, 'rb') as f:
                            with ftplib.FTP() as ftp:
                                ftp.connect("192.168.0.54", 210)
                                ftp.login("specit", "13508")
                                ftp.encoding = "utf-8"
#                                ftp.storlines("STOR %s" % os.path.basename(i), f)
                                ftp.storbinary("STOR %s" % os.path.basename(i), f)
                    elif d[q] == 'ira':
                        with open(i, 'rb') as f:
                            with ftplib.FTP() as ftp:
                                ftp.connect("192.168.0.54", 2100)
                                ftp.login("specit", "13508")
                                ftp.encoding = "utf-8"
                                ftp.cwd('/agent')
#                                ftp.storlines("STOR %s" % basename(i), f)
#                                ftp.storbinary("STOR %s" % os.path.basename(i), f)
                                ftp.storbinary(f"STOR {basename(i)}", f)
                    elif d[q] == 'rcb':
                        with open(i, 'rb') as f:
                            with ftplib.FTP() as ftp:
                                ftp.connect("192.168.0.54", 2100)
                                ftp.login("specit", "13508")
                                ftp.encoding = "utf-8"
                                ftp.cwd('/mount')
#                                ftp.storlines("STOR %s" % basename(i), f)
                                ftp.storbinary("STOR %s" % os.path.basename(i), f)
                                ftp.quit()
                except:
                        print('sorry, bad connect')
                        shutil.copy(i, '/mnt/c/Users/seligenenko/port/send/')
                if q in os.listdir('/mnt/c/Users/seligenenko/port/'):
                    if "%s.zip" % cur_date in os.listdir('/mnt/c/Users/seligenenko/port/%s/' % q):
                        with zipfile.ZipFile('/mnt/c/Users/seligenenko/port/%s/%s.zip' % (q,cur_date), 'a', compression=zipfile.ZIP_LZMA) as myzip:
                            myzip.write(i, basename(i))
                    else:
                        with zipfile.ZipFile('/mnt/c/Users/seligenenko/port/%s/%s.zip' % (q,cur_date), 'w', compression=zipfile.ZIP_LZMA) as myzip:
                            myzip.write(i, basename(i))
                    break
                else:
                    os.makedirs("/mnt/c/Users/seligenenko/port/%s" % q)
                    if "%s.zip" % cur_date in os.listdir('/mnt/c/Users/seligenenko/port/%s/' % q):
                        with zipfile.ZipFile('/mnt/c/Users/seligenenko/port/%s/%s.zip' % (q,cur_date), 'a', compression=zipfile.ZIP_LZMA) as myzip:
                            myzip.write(i, basename(i))
                    else:
                        with zipfile.ZipFile('/mnt/c/Users/seligenenko/port/%s/%s.zip' % (q,cur_date), 'w', compression=zipfile.ZIP_LZMA) as myzip:
                            myzip.write(i, os.path.basename(i))
                    break
    os.remove(i)
#session = ftplib.FTP(host='192.168.0.54', user='specit', passwd='13508')
#print (session.getwelcome())