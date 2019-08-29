#encoding: utf-8

# 中百供应商查询主页：http://gys.zon100.com/gyscxmain.jsp
import requests
from bs4 import BeautifulSoup
import mysql.connector
import re

rq1 = input("输入开始日期：")
rq2 = input("输入截止日期：")
conn = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='studentinfo')
cursor = conn.cursor()

sql = "delete from zbddjk"

cursor.execute(sql)
conn.commit()
#
payload = {'zh': '18864', 'pwd': '520520'}
r = requests.post('http://gys.zon100.com/login.do', data=payload)
# print(r.cookies.get_dict())
# print(r.cookies.get_dict().get('JSESSIONID'))
ck = "JSESSIONID=" + r.cookies.get_dict().get('JSESSIONID')
# print(ck)
#

url = "http://gys.zon100.com/djcx/DdHeadAction.do"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    'Cookie': ck
}
data = {
    'fgs': 'C',
    'gysh': '18864',
    'rq1': rq1,
    'rq2': rq2,
    'ddh': ''
}
response = requests.post(url=url, headers=headers, data=data)
response.encoding = 'gbk'

content = response.text
# print(content)

soup = BeautifulSoup(content, 'lxml')
for el in soup.find_all(id='demo'):
    # for item in el.find_all('a'):
    #     url = 'http://gys.zon100.com' + item.attrs['href']
    #     # print(url)
    #     ddbh = item.get_text()
    #     ddlb = item.parent.next_sibling.next_sibling.get_text()
    #     dhrq = item.parent.next_sibling.next_sibling.next_sibling.next_sibling.get_text()
    #     print(ddbh,ddlb,dhrq)
    for item in el.find_all('tbody'):
        for row in item.find_all('tr'):
            td = row.find_all('td')
            url = "http://gys.zon100.com"+td[2].find('a').attrs['href']
            ddh = td[2].get_text()
            ddlb = td[3].get_text()
            dhrq = td[4].get_text()
            jzrq = td[5].get_text()
            jyfs = td[6].get_text()
            mc = re.sub('\s', '', td[7].get_text())
            mcbm = mc[0:4]
            mcmc = mc[4:len(mc)]
            kq = re.sub('\s', '', td[8].get_text())
            kqbm = kq[0:6]
            kqmc = kq[6:len(kq)]
            ds = re.sub('\s', '', td[9].get_text())
            dsbm = ds[0:6]
            dsmc = ds[6:len(ds)]
            shzt = td[10].get_text()
            # print(url, ddh, ddlb, dhrq, jzrq, jyfs, mcbm, mcmc, kqbm, kqmc, dsbm, dsmc, shzt)
            data = {
                'fgs': 'C',
                'seqno': ddh
            }
            response = requests.get(url=url, headers=headers, data=data)
            response.encoding = 'gbk'

            content = response.text
            # print(content)
            soup = BeautifulSoup(content, 'lxml')
            for el in soup.find_all(id='demo'):
                for item in el.find_all('tbody'):
                    for row in item.find_all('tr'):
                        td = row.find_all('td')
                        spbm = td[1].get_text()
                        txm = td[2].get_text()
                        pm = td[3].get_text()
                        pp = td[4].get_text()
                        dw = td[5].get_text()
                        js = td[6].get_text()
                        bzsl = td[7].get_text()
                        xs = td[8].get_text()
                        jg = td[11].get_text()
                        je = td[12].get_text()
                        # print(url, ddh, ddlb, dhrq, jzrq, jyfs, mcbm, mcmc, kqbm, kqmc, dsbm, dsmc, shzt, spbm,
                        #       txm, pm, pp, dw, js, bzsl, xs, jg, je)
                        #sql
                        sql = "insert into zbddjk values('" + ddh + "','" + ddlb + "','" + dhrq + "','" + jzrq + \
                              "','" + jyfs + "','" + mcbm + "','" + mcmc + "','" + kqbm + "','" + kqmc + "','" + dsbm + \
                              "','" + dsmc + "','" + shzt + "','" + spbm + "','" + txm + "','" + pm + \
                              "','" + pp +"','" + dw +"'," + js +"," + bzsl +"," + xs + \
                              "," + jg +"," + je +")"

                        # print(sql)
                        cursor.execute(sql)
                        conn.commit()
    cursor.close()
    conn.close()





