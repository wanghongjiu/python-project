import requests
import shutil
import tesserocr
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import mysql.connector
import re
import time
res = requests.get("http://hgsm.oicp.net:88/CheckCode.aspx", stream=True, verify=False)
f = open('check.jpg', 'wb')
shutil.copyfileobj(res.raw, f)
f.close()
im = Image.open("check.jpg", "r")
code = tesserocr.image_to_text(im)
# while not(code.strip().isdigit()):
#     res = requests.get("http://hgsm.oicp.net:88/CheckCode.aspx", stream=True, verify=False)
#     f = open('check.jpg', 'wb')
#     shutil.copyfileobj(res.raw, f)
#     f.close()
#     im = Image.open("check.jpg", "r")
#     code = tesserocr.image_to_text(im)
code = code.strip()
print(code)
##############################################################
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://hgsm.oicp.net:88/login.aspx')
# driver.find_element_by_name('imgLogin').click() #点击登录进入登录界面
driver.find_element_by_name('txtUserName').send_keys('10002137') #发送帐号名
driver.find_element_by_name('txtPassword').send_keys('2137')
driver.find_element_by_name('txtCheckCode').send_keys(code, Keys.ENTER) #发送密码并回车
driver.find_element_by_name('imgLogin').click() #点击登录进入登录界面
time.sleep(10) # 等待cookie加载完成
cookies = driver.get_cookies()
# rq1 = input("输入开始日期：")
# rq2 = input("输入截止日期：")
# conn = mysql.connector.connect(user='root', password='',
#                               host='127.0.0.1',
#                               database='studentinfo')
# cursor = conn.cursor()
#
# sql = "delete from zbddjk"
#
# cursor.execute(sql)

# conn.commit()

# payload = {'txtUserName': '10002137',
#            'txtPassword': '2137',
#            'txtCheckCode': code
#            }
# r = requests.post('http://hgsm.oicp.net:88/login.aspx', data=payload, verify=False)
# ck = "ASP.NET_SessionId=" + r.cookies.get_dict().get('ASP.NET_SessionId')
# print(r.cookies.get_dict())
# url = "http://hgsm.oicp.net:88/Default.aspx"
# headers = {
#     'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
#     'Cookie': ck
# }
# data = {
#     '__EVENTTARGET': '',
#     '__EVENTARGUMENT': '',
#     '__VIEWSTATE': '/wEPDwUKMTIwMTg4OTUwMg9kFgJmD2QWAgIDD2QWAgIBD2QWCAIFDw8WBB4EVGV4dAUG6Zeo5bqXHgdWaXNpYmxlZ2RkAgYPEA8WCh4UQXBwZW5kRGF0YUJvdW5kSXRlbXNnHg1EYXRhVGV4dEZpZWxkBQticmFuY2hfbmFtZR4ORGF0YVZhbHVlRmllbGQFCWJyYW5jaF9ubx4LXyFEYXRhQm91bmRnHwFnZBAVEQblhajpg6gG5oC76YOoDOaVmeW3pei2heW4ggzopb/lrabotoXluIIM5Lic5a2m6LaF5biCDOWNl+Wtpui2heW4ggznmb7mg6DotoXluIIM57Ku5rK56LaF5biCDOmfteS4gOi2heW4ggzpn7XlrabotoXluIIM6Z+15pWZ6LaF5biCDOmfteS6jOi2heW4ggzpq5jlsYLotoXluIIM5Za75Zut6LaF5biCDOi0teWuvui2heW4ggzmlrDpm7bllK7pg6gS5qCh5Zut5paH5YyW55So5ZOBFREG5YWo6YOoBjAwICAgIAYwMSAgICAGMDIgICAgBjAzICAgIAYwNCAgICAGMDUgICAgBjA2ICAgIAYwNyAgICAGMDggICAgBjA5ICAgIAYxMSAgICAGMTIgICAgBjEzICAgIAYxNCAgICAGMTUgICAgBjE2ICAgIBQrAxFnZ2dnZ2dnZ2dnZ2dnZ2dnZ2RkAggPFgQfAAUSPGJyIC8+6K6i5Y2V5Y2V5Y+3HwFoZAIJDw8WAh8BaGRkGAEFIGN0bDAwJENvbnRlbnRQbGFjZSRncmlkT3JkZXJMaXN0DzwrAAoBCAIBZGIQkFjGdUMA+eSSnPqPJV80CAbo',
#     '__VIEWSTATEGENERATOR': '956AA505',
#     '__EVENTVALIDATION': '/wEWFgLR4tiQBgLF2aHdDALkw6DCDgLWtNmACgKO3teqCwKO3tPVCwKO3q/UCwKO3qvXCwKO3qfWCwKO3qPRCwKO3r/QCwKO3rvTCwKO3veiCwKO3vOtCwKx3tPVCwKx3q/UCwKx3qvXCwKx3qfWCwKx3qPRCwKx3r/QCwKTveTSDwLD09SWDEfy7k0HTst5FYHY3rC/LmqB77WZ',
#     'ctl00$ContentPlace$txtFromDate': '2019-05-08',
#     'ctl00$ContentPlace$txtToDate': '2019-05-13',
#     'ctl00$ContentPlace$dropBranch': '全部',
#     'ctl00$ContentPlace$txtSheetNo': '',
#     'ctl00$ContentPlace$btnFind': '查询'
# }
# response = requests.get(url=url, headers=headers)
# content = response.text
# print(content)
