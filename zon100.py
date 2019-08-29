#encoding: utf-8

# 中百供应商查询主页：http://gys.zon100.com/gyscxmain.jsp

from urllib import request
# 1.不使用cookie
url = "http://gys.zon100.com/gyscxmain.jsp"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    'Cookie': "JSESSIONID=770FA21F5AD28B72BC49F3B8EB404668; Hm_lvt_3c8ecbfa472e76b0340d7a701a04197e=1550217881,1551490621,1551752854,1552649775; Hm_lpvt_3c8ecbfa472e76b0340d7a701a04197e=1552649775; gysZh=000075"
}
re = request.Request(url=url, headers=headers)
response = request.urlopen(re)

with open('zon100.html', 'w', encoding='gbk') as fp:
    fp.write(response.read().decode('gbk'))


# print(response.read().decode('gbk'))



