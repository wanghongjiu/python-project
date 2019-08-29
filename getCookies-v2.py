from urllib import request
import http
from http import cookiejar

cookie = cookiejar.CookieJar()
        # 待填写的cookie对象
opener = request.build_opener(request.HTTPCookieProcessor(cookie))
resp = opener.open('http://gys.zon100.com/djcx/DdHeadAction.do')
        # opener open 的过程中，会将页面的 cookie 信息放入 cookie 对象中
for item in cookie:
    print(item.name + ":" + item.value)

