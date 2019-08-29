# 中商查询主页：http://www.cbqq.cn/program/html/main.php
import requests
from bs4 import BeautifulSoup
import mysql.connector
import re
import json

# conn = mysql.connector.connect(user='root', password='',
#                               host='127.0.0.1',
#                               database='studentinfo')
# cursor = conn.cursor()
#
# sql = "delete from zbdd"
#
# cursor.execute(sql)
# conn.commit()

url =
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    'Cookie': "Hm_lvt_3c8ecbfa472e76b0340d7a701a04197e=1555726672,1555987497,1556156923,1557823511; PHPSESSID=6135m3g3skleeld9t6qf4qrre0"
}
data = {
    'dealmode': 'QUERY',
    'supid': '0332M',
     'sqlwhere':  "AUDITDATE >= to_date('2019-04-01', 'YYYY-MM-DD')",
     "mywhere": "AUDITDATE >= str_to_date('2019-04-01', '%Y-%m-%d')",
     "page": 1,
     "start": 0,
     "limit": 100
}
response = requests.post(url=url, headers=headers, data=data)
response.encoding = 'utf-8'

content = response.content
# print(content)
content = content.decode("unicode-escape")
start = content.find('[')
end = len(content)
end = end - 3
content = content[start:end]
print(content)
dic_content = json.loads(content)
for item in dic_content:
    billno = item['BOHBILLNO']
    print(item['BOHBILLNO'])
    data1 = {
        'PHBILLNO': billno,
        'dealmode': 'MXQUERY',
        'page': 1,
        'start': 0,
        'limit': 25
    }
    item_response = requests.post(url=url, headers=headers, data=data1)
    item_response.encoding = 'utf-8'
    #
    item_content = item_response.content
    #
    item_content = item_content.decode("unicode-escape")
    print(item_content)
    start = item_content.find('[')
    end = len(item_content)
    end = end - 3
    item_content = item_content[start:end]
    print(item_content)



# soup = BeautifulSoup(content, 'lxml')
# for el in soup.find_all(id='demo'):
#     # for item in el.find_all('a'):
#     #     url = 'http://gys.zon100.com' + item.attrs['href']
#     #     # print(url)
#     #     ddbh = item.get_text()
#     #     ddlb = item.parent.next_sibling.next_sibling.get_text()
#     #     dhrq = item.parent.next_sibling.next_sibling.next_sibling.next_sibling.get_text()
#     #     print(ddbh,ddlb,dhrq)
#     for item in el.find_all('tbody'):
#         for row in item.find_all('tr'):
#             td = row.find_all('td')
#             url = "http://gys.zon100.com"+td[2].find('a').attrs['href']
#             ddh = td[2].get_text()
#             ddlb = td[3].get_text()
#             dhrq = td[4].get_text()
#             jzrq = td[5].get_text()
#             jyfs = td[6].get_text()
#             mc = re.sub('\s', '', td[7].get_text())
#             mcbm = mc[0:4]
#             mcmc = mc[4:len(mc)]
#             kq = re.sub('\s', '', td[8].get_text())
#             kqbm = kq[0:6]
#             kqmc = kq[6:len(kq)]
#             ds = re.sub('\s', '', td[9].get_text())
#             dsbm = ds[0:6]
#             dsmc = ds[6:len(ds)]
#             shzt = td[10].get_text()
#             # print(url, ddh, ddlb, dhrq, jzrq, jyfs, mcbm, mcmc, kqbm, kqmc, dsbm, dsmc, shzt)
#             data = {
#                 'fgs': 'C',
#                 'seqno': ddh
#             }
#             response = requests.get(url=url, headers=headers, data=data)
#             response.encoding = 'gbk'
#
#             content = response.text
#             # print(content)
#             soup = BeautifulSoup(content, 'lxml')
#             for el in soup.find_all(id='demo'):
#                 for item in el.find_all('tbody'):
#                     for row in item.find_all('tr'):
#                         td = row.find_all('td')
#                         spbm = td[1].get_text()
#                         txm = td[2].get_text()
#                         pm = td[3].get_text()
#                         pp = td[4].get_text()
#                         dw = td[5].get_text()
#                         js = td[6].get_text()
#                         bzsl = td[7].get_text()
#                         xs = td[8].get_text()
#                         jg = td[11].get_text()
#                         je = td[12].get_text()
#                         # print(url, ddh, ddlb, dhrq, jzrq, jyfs, mcbm, mcmc, kqbm, kqmc, dsbm, dsmc, shzt, spbm,
#                         #       txm, pm, pp, dw, js, bzsl, xs, jg, je)
#                         #sql
#                         sql = "insert into zbdd values('" + ddh + "','" + ddlb + "','" + dhrq + "','" + jzrq + \
#                               "','" + jyfs + "','" + mcbm + "','" + mcmc + "','" + kqbm + "','" + kqmc + "','" + dsbm + \
#                               "','" + dsmc + "','" + shzt + "','" + spbm + "','" + txm + "','" + pm + \
#                               "','" + pp +"','" + dw +"'," + js +"," + bzsl +"," + xs + \
#                               "," + jg +"," + je +")"
#
#                         # print(sql)
#                         cursor.execute(sql)
#                         conn.commit()
#     cursor.close()
#     conn.close()





