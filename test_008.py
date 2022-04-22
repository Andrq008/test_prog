import glob
from bs4 import BeautifulSoup
import plotly.graph_objects as go
su = 0.0
du = []
for i in glob.glob(r'C:\Users\seligenenko\port\*.xml'):
    print(i)
    with open(i, 'r', encoding='utf-8') as file:
        con = file.readlines()
        bs = BeautifulSoup(str(con), 'html.parser')
        bs1 = str(bs.find_all('value')[0]).replace("<value>", "").replace("</value>", "")
        su = su + float(bs1)
        du.append(su)
        print(su)
        print(bs1)
print(du)
fig = go.Figure(data=[go.Bar(y=du)])
fig.show()
