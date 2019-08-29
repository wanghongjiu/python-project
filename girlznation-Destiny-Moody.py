import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.girlznation.com/sites/destiny_moody/')
response.encoding = 'utf-8'

content = response.text
# print(content)

soup = BeautifulSoup(content, 'lxml')
filename = __file__
pos = filename.find('.')
filename = filename[0:pos] + '.txt'
print(filename)
fp = open(filename, 'w', encoding='utf-8')
for el in soup.find_all(class_='pic_list'):
    for item in el.find_all('a'):
        url = item.attrs['href']
        # print(url)
        response = requests.get(url)
        response.encoding = 'utf-8'

        content = response.text
        # print(content)
        soup = BeautifulSoup(content, 'lxml')
        for el_1 in soup.find_all(class_='pic_list'):
            for item_1 in el_1.find_all('a'):
                url_1 = item_1.attrs['href']
                url_1 = url + url_1 + '\n'
                # print(url_1)
                fp.write(url_1)

