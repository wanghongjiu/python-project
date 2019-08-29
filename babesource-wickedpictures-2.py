import requests
from bs4 import BeautifulSoup

response = requests.get('https://babesource.com/filter-content/?paysite=107')
response.encoding = 'utf-8'

content = response.text
# print(content)
basepath = "https://babesource.com/filter-content/"

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
        for el_1 in soup.find_all(class_='thumbs cf'):
            for item_1 in el_1.find_all('a'):
                url = item_1.attrs['href']
                # print(url)

response = requests.get('https://babesource.com/filter-content/?paysite=107')
response.encoding = 'utf-8'

content = response.text

soup = BeautifulSoup(content, 'lxml')
for ele in soup.find_all(class_='pagination cf'):
    for p_item in ele.find_all('a'):
        p_url = basepath + p_item.attrs['href']
        print(p_url)

        response = requests.get(p_url)
        response.encoding = 'utf-8'

        content = response.text
        # print(content)
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
                for el_1 in soup.find_all(class_='thumbs cf'):
                    for item_1 in el_1.find_all('a'):
                        url = item_1.attrs['href']
                        print(url)


