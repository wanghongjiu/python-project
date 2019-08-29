# -*- coding: gbk -*-

# 武汉理工登陆页：http://whlgweb.oicp.net:8899/login.ASP
#武汉理工查询页：
import requests
from bs4 import BeautifulSoup
import mysql.connector
import re

# rq1 = input("输入开始日期：")
# rq2 = input("输入截止日期：")
# conn = mysql.connector.connect(user='root', password='',
#                               host='127.0.0.1',
#                               database='studentinfo')
# cursor = conn.cursor()
#
# sql = "delete from zbdd"
#
# cursor.execute(sql)
# conn.commit()

payload = {'username': '1002A', 'password': '1'}
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
}

r = requests.post('http://whlgweb.oicp.net:8899/login.ASP', headers=headers,  data=payload)

s=requests.session()
r.encoding = 'gb2312'

# content = r.text
# print(content)
# ck = "JSESSIONID=" + r.cookies.get_dict().get('JSESSIONID')
print(r.cookies.get_dict())


# ck = "JSESSIONID=" + r.cookies.get_dict().get('JSESSIONID')
# print(ck)

# url = "http://whlgweb.oicp.net:8899/function/resultdd.asp?seqno=&lrrq1=2019-04-01&lrrq2=2019-05-11&jshj=&flag=Y&Submit=%CB%D1%CB%F7"
# url = "http://whlgweb.oicp.net:8899/index.asp"
# print(url)
# headers = {
#     'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
#     'Cookie': ""
# }
#
# response = requests.get(url=url, headers=headers)
# response.encoding = 'gbk'
#
# content = response.text
# print(content)

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





