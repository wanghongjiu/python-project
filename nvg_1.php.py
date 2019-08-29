import requests
from bs4 import BeautifulSoup

response = requests.get('https://mnvg.com/Winter/Tight_Pussy_Gets_Filled_With_Cum')
response.encoding = 'utf-8'

content = response.text
# print(content)
basepath = "https://mnvg.com"

soup = BeautifulSoup(content, 'lxml')
for el in soup.find_all(class_='gallery'):
    for item in el.find_all('a'):
        url = basepath + item.attrs['href']
        print(url)
