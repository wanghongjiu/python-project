import requests
from bs4 import BeautifulSoup

response = requests.get('https://mnvg.com')
response.encoding = 'utf-8'

content = response.text
# print(content)
basepath = "https://mnvg.com"

soup = BeautifulSoup(content, 'lxml')
for el in soup.find_all(class_='update group'):
    for mi in el.find_all(class_='mainImage'):
        for item in mi.find_all('a'):
            url = basepath + item.attrs['href']
            response = requests.get(url)
            response.encoding = 'utf-8'

            content = response.text
            soup = BeautifulSoup(content, 'lxml')
            for el in soup.find_all(class_='gallery'):
                for item in el.find_all('a'):
                    url = basepath + item.attrs['href']
                    print(url)
