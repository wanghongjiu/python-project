import requests
from bs4 import BeautifulSoup

response = requests.get('http://news.wtu.edu.cn/zhxw.htm')
response.encoding = 'utf-8'

content = response.text
#print(content)
soup = BeautifulSoup(content, 'lxml')
#print(soup.find_all(class_='single-project-item').find_all('title'))
for el in soup.find_all(class_='single-project-item'):
    for item in el.find_all('a'):
        if 'http' in item.attrs['href']:
            url = item.attrs['href']
        else:
            url = 'http://news.wtu.edu.cn/' + item.attrs['href']

        print(url, item.get_text())

s = soup.find(id='fanye205887').get_text()
start = s.find('/')
end = len(s)
pages = s[start+1:end]
#print(pages)
pages = int(pages) - 1
'''
for i in range(pages, 0, -1):
    url = 'http://news.wtu.edu.cn/zhxw/' + str(i) + '.htm'
    #print(url)
    response = requests.get(url)
    response.encoding = 'utf-8'

    content = response.text
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    for el in soup.find_all(class_='single-project-item'):
        for item in el.find_all('a'):
            if 'http' in item.attrs['href']:
                url = item.attrs['href']
            else:
                url = 'http://news.wtu.edu.cn/' + item.attrs['href']

            print(url, item.get_text())
'''








