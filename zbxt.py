import requests
from bs4 import BeautifulSoup
import mysql.connector

# conn = mysql.connector.connect(user='root', password='',
#                               host='127.0.0.1',
#                               database='studentinfo')
# cursor = conn.cursor()

response = requests.get('http://gys.zon100.com/gyscxmain.jsp')
response.encoding = 'utf-8'

content = response.text
print(content)
# soup = BeautifulSoup(content, 'lxml')
# for el in soup.find_all(class_='single-project-item'):
#     for item in el.find_all('a'):
#         if 'http' in item.attrs['href']:
#             url = item.attrs['href']
#         else:
#             url = 'http://news.wtu.edu.cn/' + item.attrs['href']
#         # print(item.parent.parent.parent.previous_sibling.previous_sibling.find('span').get_text())
#         pubdate = item.parent.parent.parent.previous_sibling.previous_sibling.find('span').get_text() + \
#         '-' + item.parent.parent.parent.previous_sibling.previous_sibling.find('h4').get_text()
#
#         response = requests.get(url)
#         response.encoding = 'utf-8'
#
#         content = response.text
#         soup = BeautifulSoup(content, 'lxml')
#         if soup.find(id='vsb_content') == None:
#             details = soup.find(id='vsb_content_2').get_text().replace('\n', '')
#         else:
#             details = soup.find(id='vsb_content').get_text().replace('\n', '')
#
#         # print(pubdate)
#         # print(rq, url, item.get_text())
#         title = item.get_text()
#         sql = "insert into news(pub_date,url,title,content) values('" + pubdate + "','" + url + "','" + title + \
#               "','" + details + "')"
#         # print(sql)
#         cursor.execute(sql)
#         conn.commit()

#获取所有的综合新闻
'''
s = soup.find(id='fanye205887').get_text()
start = s.find('/')
end = len(s)
pages = s[start+1:end]
#print(pages)
pages = int(pages) - 1

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
# cursor.close()
# conn.close()







