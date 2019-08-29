#encoding: utf-8
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import mysql.connector

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://202.114.105.116:434/wdzq/Login.aspx')

driver.find_element_by_name('Id').send_keys('sup1300A') #发送帐号名
driver.find_element_by_name('password').send_keys('1', Keys.ENTER) #发送密码
# driver.find_element_by_name('submit1').click() #点击登录进入登录界面
time.sleep(10) # 等待cookie加载完成
cookies = driver.get_cookies()
print(cookies)
ck = ""
for item in cookies:
    ck = ck + item['name'] + "=" + item['value'] + ";"
print(ck)
url = "http://202.114.105.116:434/wdzq/MainPage/Index.aspx?oper_no=sup1300A"
url = "http://202.114.105.116:434/wdzq/Logistic/PurchaseOrderList.aspx?sheet_type=PO&page_type=PO"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    'Cookie': ck
}
data = {
    'GenericListAscx$ctl01$tb_operDateFrom': '2019-08-01',
    'GenericListAscx$ctl01$tb_operDateTo': '2019-08-23',
}
response = requests.post(url=url, headers=headers, data=data)
# response.encoding = 'gbk'

content = response.text
# print(content)
start = content.find('var keys')
content_len = len(content)
# print(start, content_len)
s = content[start:content_len - 1]
start = s.find('[')
end = s.find(']')
s1 = s[start + 1:end]
# print(s1)
arr = s1.split(',')
for item in arr:
    # print(item[1:len(item) - 2])
    ddh = item[1:len(item) - 3]
    dd_req = "http://202.114.105.116:434/wdzq/AjaxServ.aspx?Action=SetKeyValue&KeyValue=" + ddh
    # print(dd_req)
    response1 = requests.get(url=dd_req, headers=headers)
    content1 = response1.text
    # print(content1)
    content2 = content1[18:len(content1) - 4]
    # print(content2)
    dd_url = "http://202.114.105.116:434/wdzq/Logistic/PurchaseOrderInfo.aspx?&DialogMode=Modaless&Key=" + content2
    print(dd_url)
    response3 = requests.get(url=dd_url, headers=headers)
    content3 = response3.text
    print(content3)





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





