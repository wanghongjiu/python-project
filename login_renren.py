from urllib import request
from urllib import parse
from http.cookiejar import CookieJar

headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }

def get_opener():
    # 1.登陆
    # 1.1 创建一个cookiejar对象
    cookiejar = CookieJar()
    # 1.2 使用cookiejar创建一个HTTPCookieProcess对象
    handler = request.HTTPCookieProcessor(cookiejar)
    # 1.3 使用上一步创建的Handler创建一个opener
    opener = request.build_opener(handler)
    return opener

def login_url(opener):
    # 1.4 使用opener发送登陆请求（提供用户名和密码）

    data = {
        'email' : "13006134009",
        'password' : "ahloha12345"
    }
    login_url = "http://www.renren.com/PLogin.do"
    req = request.Request(login_url, data=parse.urlencode(data).encode('utf-8'), headers = headers)
    opener.open(req)

def visit_profile(opener):
    # 2.访问个人主页
    dapeng_url = "http://www.renren.com/880151247/profile"
    # 获取个人主页的页面的时候，不要新建一个opener，而应该使用之前的opener
    req = request.Request(dapeng_url, headers = headers)

    response = opener.open(req)
    with open('renrenDapeng.html', 'w', encoding='utf-8') as fp:
        fp.write(response.read().decode('utf-8'))

if __name__ == '__main__':
    opener = get_opener()
    login_url(opener)
    visit_profile(opener)
