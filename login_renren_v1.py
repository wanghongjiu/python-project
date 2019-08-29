import requests

session = requests.session()
# post_url = "http://www.renren.com/PLogin.do"
post_url = "http://gys.zon100.com/gys_login.htm"
# post_data = {"email": "13006134009", "password": "ahloha12345"}
post_data = {"zh": "000075", "pwd": "1314"}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}

session.post(post_url, data=post_data, headers=headers)
# get_url = "http://gys.zon100.com/djcx/DdHeadAction.do"

get_url = "http://gys.zon100.com/gyscxmain.jsp"
r = session.get(get_url)

with open("renren1.html", "w", encoding="gbk") as f:
    f.write(r.content.decode('gbk'))
