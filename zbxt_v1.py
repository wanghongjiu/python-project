import requests
from bs4 import BeautifulSoup
import mysql.connector

# data = {'zh': '000075', 'pwd': '1314'}
# r = requests.post('http://gys.zon100.com/login.do', data=data)
# print(r.text)
# print(r.cookies.get_dict())
# r = requests.get('http://gys.zon100.com/gyscxmain.jsp', cookies = r.cookies)
# print(r.text)

data = {'fg2': 'C', 'gysh': '10492', 'rq1': '2019-03-05', 'rq2': '2019-03-05'}
r = requests.post('http://gys.zon100.com/djcx/ShdHeadAction.do', data=data)
print(r.text)
