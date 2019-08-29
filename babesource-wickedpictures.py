import requests
from bs4 import BeautifulSoup

response = requests.get('https://babesource.com/filter-content/?paysite=107')
response.encoding = 'utf-8'

content = response.text
# print(content)
basepath = "https://mnvg.com"

soup = BeautifulSoup(content, 'lxml')
for el in soup.find_all(class_='content'):
        for item in el.find_all('a'):
            url = item.attrs['href']
            # print(url)
            response = requests.get(url)
            response.encoding = 'utf-8'

            content = response.text
            # print(content)
            soup = BeautifulSoup(content, 'lxml')
            for el in soup.find_all(class_='thumbs cf'):
                for item in el.find_all('a'):
                    url = item.attrs['href']
                    print(url)
