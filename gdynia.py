from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

link = "https://wyniki.datasport.pl/results3029/"

driver = webdriver.Firefox()
driver.get(link)


lastHeight = driver.execute_script("return document.body.scrollHeight")
#print(lastHeight)

pause = 0.5
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(pause)
    newHeight = driver.execute_script("return document.body.scrollHeight")
    if newHeight == lastHeight:
        break
    lastHeight = newHeight
    #print(lastHeight)

html = driver.page_source
soup = BeautifulSoup(html, "lxml")


# array
appended_data = []
table_body = soup.find('tbody')
# print(table_body)
rows = table_body.find_all('tr')
for row in rows:
    cols=row.find_all('td')
    cols=[x.text.strip() for x in cols]
    appended_data.append(cols)


# print(appended_data)
appended_data2 = pd.DataFrame.from_dict(appended_data)

appended_data2.columns = ['Pos', 'x',  'Name', 'Club' , 'Rocznik' , 'Cat' , 'Swim', 'T1', 'Bike', 'T2', 'Run', 'Time']

del appended_data2['x']
del appended_data2['Rocznik']
# del appended_data2.loc

x = appended_data2.drop([appended_data2.index[0] , appended_data2.index[10]], inplace=True)

appended_data2.to_csv('gdynia5.csv')
print('Job finished!')