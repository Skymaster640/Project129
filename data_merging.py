import csv
import pandas as pd

df = pd.read_csv("dwarf_stars.csv")

print(df.columns)

data1=[]
data2=[]


df= df.notna()
    
df['Radius'] = 0.102763 * df['Radius']

#df['Mass']=df['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
df["Mass"] = 0.000954588 * df["Mass"]


df.drop(['Unnamed: 0'],axis=1,inplace=True)

df.reset_index(drop=True,inplace=True)

df.to_csv("dwarf_stars_converted.csv")

with open("dwarf_stars_converted.csv","r")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data2.append(row)

with open("bright_stars.csv","r")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data1.append(row)

headers_1=data1[0]
star_data_1=data1[1:]
headers_2=data2[0]
star_data_2=data2[1:]

header = headers_1 + headers_2
star_data = []


for i in star_data_1:
    star_data.append(i)
for j in star_data_2:
    star_data.append(j)

#for index,data in enumerate(star_data_1):
    #star_data.append(star_data_1[index]+star_data_2[index])

with open("total_stars.csv","a+")as f:
    csvwriter= csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(star_data)
