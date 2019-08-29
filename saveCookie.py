from urllib import request
from http.cookiejar import MozillaCookieJar

cookiejar = MozillaCookieJar('cookie.txt')
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

resp = opener.open('http://gys.zon100.com/djcx/DdHeadAction.do')

cookiejar.save(ignore_discard=True)

