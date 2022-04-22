#!/bin/python
import xml.etree.cElementTree as ET
from bs4 import BeautifulSoup
from array import *
import re
import glob
import matplotlib
import matplotlib.pyplot as plt
su = 0.0
du =[]
for i in glob.glob("/Региональный_центр_бронирования/*"):
 with open(i, 'r', encoding='utf-8') as file:
  con = file.readlines()
  bs = BeautifulSoup(str(con), 'html.parser')
  bs1 = str(bs.find_all('value')[1]).replace("<value>", "").replace("</value>", "")
  try:
   su = su + float(bs1)
  except:
   print('sorry')
  du.append(su)
  print(su)
  print(bs.find_all('value')[1])
plt.bar('prtb', du)
plt.title("prtb")
plt.xlabel("mony")
plt.ylabel("day")
plt.show()
