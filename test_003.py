import xml.etree.ElementTree as ET
import pandas as pd
xml_data = open(r'C:\Users\seligenenko\port\gridnine.xml', 'r', encoding='UTF8').read()
root = ET.XML(xml_data)

data = []
cols = []
for i, child in enumerate(root):
    data.append([subchild.text for subchild in child])
    cols.append(child.tag)

df = pd.DataFrame(data).T  # Write in DF and transpose it
df.columns = cols  # Update column names
print(df)
