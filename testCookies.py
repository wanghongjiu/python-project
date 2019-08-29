import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import mysql.connector

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://whlgweb.oicp.net:8899/login.ASP')
# 不考虑验证码的情况
# driver.find_element_by_xpath('//button[@data-za-detail-view-id="2278"]').click() #点击登录进入登录界面
# driver.find_element_by_xpath('//input[@name="username"]').send_keys('account') #发送帐号名
# driver.find_element_by_xpath('//input[@name="password"]').send_keys('password',Keys.ENTER) #发送密码并回车
driver.find_element_by_name('IbtnEnter').click() #点击登录进入登录界面
driver.find_element_by_name('username').send_keys('1002A') #发送帐号名
driver.find_element_by_name('password').send_keys('1', Keys.ENTER) #发送密码并回车
time.sleep(10) # 等待cookie加载完成
cookies = driver.get_cookies()
# print(cookies)
ck = ""
for item in cookies:
    ck = ck + item['name'] + "=" + item['value']
# print(ck)

url = "http://whlgweb.oicp.net:8899/function/resultdd.asp?seqno=&lrrq1=2019-04-01&lrrq2=2019-05-11&jshj=&flag=Y&Submit=%CB%D1%CB%F7"
# url = "http://whlgweb.oicp.net:8899/index.asp"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    'Cookie': ck
}

response = requests.get(url=url, headers=headers)
response.encoding = 'gbk'

content = response.text
# print(content)

soup = BeautifulSoup(content, 'lxml')
index = 0
base_url = "http://whlgweb.oicp.net:8899"
for el in soup.find_all('table'):
    if index == 12:
        # print(el)
        for dd in el.find_all('a'):
            dd_url = base_url + dd.attrs['href']
            # print(dd_url)
            response = requests.get(url=dd_url, headers=headers)
            response.encoding = 'gbk'

            content = response.text
            print(content)
    index = index + 1

