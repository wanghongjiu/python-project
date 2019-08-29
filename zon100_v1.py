#encoding: utf-8

# 中百供应商查询主页：http://gys.zon100.com/gyscxmain.jsp
import urllib
from urllib import request
from urllib.parse import urlparse

url = "http://gys.zon100.com/djcx/DdHeadAction.do"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    'Cookie': "Hm_lvt_3c8ecbfa472e76b0340d7a701a04197e=1550217881,1551490621,1551752854,1552649775; gysZh=000075; JSESSIONID=BB28FC3EBBCFC373278B1BB1C76E564D; Hm_lpvt_3c8ecbfa472e76b0340d7a701a04197e=1552661416"
}
values = {
    'fgs': 'C',
    'gysh': '10492',
    'rq1': '2019-03-15',
    'rq2': '2019-03-15',
    'ddh': ''
}

data = urllib.parse.urlencode(values)
data = data.encode('ascii')
re = request.Request(url=url, headers=headers, data=data)
response = request.urlopen(re)

with open('zon100_v1.html', 'w', encoding='gbk') as fp:
    fp.write(response.read().decode('gbk'))


# print(response.read().decode('gbk'))



