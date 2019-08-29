#encoding: utf-8

# 中石化查询主页：http://gys.zon100.com/gyscxmain.jsp
import requests
from bs4 import BeautifulSoup
import mysql.connector
import re
import json
import shutil

# rq1 = input("输入开始日期：")
# rq2 = input("输入截止日期：")
#
# conn = mysql.connector.connect(user='root', password='',
#                               host='127.0.0.1',
#                               database='studentinfo')
# cursor = conn.cursor()
# sql = "delete from zsh"
# cursor.execute(sql)d
# conn.commit()
res = requests.get("https://supplier.rt-mart.com.cn/code.php", stream=True, verify=False)
f = open('check.jpg', 'wb')
shutil.copyfileobj(res.raw, f)
f.close()
checkcode = input("请输入校验码：")
payload = {'area': '4', 'userid': 'rt6393', 'passw': 'Drf6393', 'checkstr': checkcode }
r = requests.post('https://https://supplier.rt-mart.com.cn/php/scm_login_check.php', data=payload)
print(r.cookies.get_dict())
#ck = "JSESSIONID=" + r.cookies.get_dict().get('JSESSIONID')
# print(ck)

# url = "https://supplier.rt-mart.com.cn/php/scm_main_top.php"
# headers = {
#     'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
#     'Cookie': ck
#}




