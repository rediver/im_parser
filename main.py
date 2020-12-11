import requests
import pandas as pd
from bs4 import BeautifulSoup

appended_data = []
url = 'https://www.multisportaustralia.com.au/races/IM703-TAUPO-2019/events/1?page='   
links = []
for i in range(1,30):
	x = url + str(i)
	links.append(x)

print(links)
results = []

for link in links:
  webpage = requests.get(link)
  data = webpage.text 
  bs=BeautifulSoup(data, "lxml")
  table_body=bs.find('tbody')
  rows = table_body.find_all('tr')
  for row in rows:
    	cols=row.find_all('td')
    	cols=[x.text.strip() for x in cols]
    	results.append(cols)


# print(results)

appended_data2 = pd.DataFrame.from_dict(results)
print(appended_data2)


appended_data2.to_csv("im.csv")

