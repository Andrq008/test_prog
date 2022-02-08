#!/bin/python
import ftplib
import os
import glob
for i in glob.glob("/mnt/c/Users/*"):
    print(i)
d = dict(ira="ftp://specit:13508@192.168.0.54:2100", b='4', c='5')
for i in d:
    print(i + ' -- ' + d[i])
#    os.system("echo put /mnt/c/Users/seligenenko/port/2022-02-04.zip | lftp %s" % d[i])
#session = ftplib.FTP('192.168.0.54', 26, 'specit', '13508')
#file = open('kitten.jpg','rb')                  # file to send
#session.storbinary('STOR kitten.jpg', file)     # send the file
#file.close()                                    # close file and FTP
#session.quit()
FTP_HOST = "192.168.0.54"
port = 2100
FTP_USER = "specit"
FTP_PASS = "13508"
#ftp = ftplib.FTP(FTP_HOST, port, FTP_USER, FTP_PASS)
#ftp = ftplib.FTP()
#ftp.connect(FTP_HOST, port)
#ftp.login(FTP_USER, FTP_PASS)
#ftp.encoding = "utf-8"
#data = ftp.retrlines('LIST')
#print(data)
#print (ftp.getwelcome())
ftp = ftplib.FTP()
ftp.connect("192.168.0.54", 2100)
ftp.login("specit", "13508")
ftp.encoding = "utf-8"
data = ftp.retrlines('LIST')
print(data)
print (ftp.getwelcome())