#Pobeda process
import pandas as pd
import re
import zipfile
#import regex

ord = pd.read_excel('C:\\Users\\seligenenko\\Desktop\\AgencyReport.xls')
#print(ord.columns)
bbb = []
for i in ord['Unnamed: 4']:
    if re.search('[a-zA-Z0-9]{6}', str(i)):
        bbb.append(i)
        print(i)
print(bbb)

myz = zipfile.ZipFile('C:\\Users\\seligenenko\\Desktop\\Krasnodar.zip', 'r')
#myz.printdir()
for i in myz.namelist():
    if re.search('key$', str(i)):
        print(i)
