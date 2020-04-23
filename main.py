
# import requests
# import pandas as pd

# url = 'https://www.multisportaustralia.com.au/races/IM703-TAUPO-2019/events/1?page='
# html = requests.get(url).content

# link_arr = []
# for i in range(1,3):    
#     url = 'https://www.multisportaustralia.com.au/races/IM703-TAUPO-2019/events/1?page='
#     link_arr.append(url + str(i))

# data = [pd.read_html(i) for i in link_arr]

# print(data)

# df = pd.DataFrame(data)
# df.to_csv('iron123.csv')

# print('WORK DONE! :D')
import requests
import pandas as pd
from bs4 import BeautifulSoup


 
 
appended_data = []

url = "https://www.multisportaustralia.com.au/races/IM703-TAUPO-2019/events/1?page=1"
page = requests.get(url + str(i))
data = page.text
soup = BeautifulSoup(data, 'html.parser')
text = soup.find_all('td')

for i in text: 
    print(i)


appended_data2 = pd.DataFrame.from_dict(appended_data)
appended_data2.to_csv('appended.csv')




 
print('WORK DONE! :D')