from urllib import request
from urllib import parse
from http.cookiejar import CookieJar

# 1. 登陆
# 1.1 创建一个cookiejar对象
cookiejar = CookieJar()
# 1.2 使用cookiejar创建一个HTTPCookieProcess对象
handler = request.HTTPCookieProcessor(cookiejar)
# 1.3 使用上一步的handler创建一个opener
opener = request.build_opener(handler)
# 1.4 使用opener发送登陆请求（传递用户名和密码）
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}
data = {
    "gysZh": "000075",
    "pwd": "520520"
}
login_url = "http://gys.zon100.com/gys_login.htm"
req = request.Request(login_url,data=parse.urlencode(data).encode('utf-8'),headers=headers)
response = request.urlopen(req)
print(response.read())
# 2. 访问页面
main_url = 'http://gys.zon100.com/djcx/DdHeadAction.do'
resp = opener.open(main_url)
print(resp.read())
# with open('zon100.html','w',encoding='utf-8') as fp:
#     fp.write(resp.read().decode("gbk"))
