#encoding: utf-8

# 中石化查询主页：http://gys.zon100.com/gyscxmain.jsp
import requests
from bs4 import BeautifulSoup
import mysql.connector
import re
import json

rq1 = input("输入开始日期：")
rq2 = input("输入截止日期：")

conn = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='studentinfo')
cursor = conn.cursor()
sql = "delete from zsh"
cursor.execute(sql)
conn.commit()
#
payload = {'userName': 'gyshb4200231', 'userPwd': 'NANbeihang123', 'XSSFLAG': -1193959466}
r = requests.post('http://ejoyscm.sinopec.com/system/login.action', data=payload)
print(r.cookies.get_dict())
ck = "JSESSIONID=" + r.cookies.get_dict().get('JSESSIONID')
# print(ck)

url = "http://ejoyscm.sinopec.com/purOrder/getOrderInfo.action"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    'Cookie': ck
}
data = {
    'page': 1,
    'rows': 100,
    'orgId': '9ca3d4bda4df492c90d541f199007037',
    'supplierConfirmStatus': 0,
    'orderStartTime': rq1,
    'orderEndTime': rq2
}
response = requests.post(url=url, headers=headers, data=data)
response.encoding = 'utf-8'
content = response.content
content = content.decode("utf-8")
# print(content)
start = content.find('[')
len_content = len(content)
content = content[start:len_content - 1]
json_content = json.loads(content)
for item in json_content:
    itemId = item['id']
    itemBillNo = item['billNo']
    dhrq = item['xdDate']
    jzrq = item['zdDate']
    mcbm = item['orgCode']
    mcmc = item['orgName']
    item_data = {
        'billId': itemId
    }
    item_url="http://ejoyscm.sinopec.com/purOrder/getOrderDetailInfo.action"
    item_response = requests.post(url=item_url, headers=headers, data=item_data)
    item_response.encoding = 'utf-8'
    item_content = item_response.content
    item_content = item_content.decode("utf-8")
    json_item_content = json.loads(item_content)
    # print(json_item_content)
    seq = 1
    for i in json_item_content:
        # print(json_item_content)
        spbm = i['spbmhx']
        txm = i['barCode']
        pm = i['pluName']
        dw = i['unit']
        js = i['sglCount']
        bzsl = i['packCount']
        xs = i['cgCount']
        jg = i['hjPrice']
        je = i['cgHCost']
        sql = "insert into zsh values(" + str(seq) + ",'" + itemBillNo + "','*','" + dhrq + "','" + jzrq + "','经销','" + mcbm + "','" \
              + mcmc + "','*','*','*','*','*','" + spbm + "','" + txm + "','" + pm + "" +"','*','" + dw \
              + "'," + str(js) + "," + str(bzsl) + "," + str(xs) + "," + str(jg) + "," + str(je) +")"
        cursor.execute(sql)
        conn.commit()
        seq = seq + 1
cursor.close()
conn.close()

