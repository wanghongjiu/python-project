#encoding: utf-8

# 访问人人网董成鹏主页：http://www.renren.com/880151247/profile
# 人人网登陆url: http://www.renren.com/SysHome.do; http://www.renren.com/PLogin.do

from urllib import request
# 1.不使用cookie
url = "http://www.renren.com/880151247/profile"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    'Cookie': "anonymid=jt9x87zm4mx35; depovince=GW; _r01_=1; ick_login=35e5613d-12b5-45da-be85-9157e3807824; ick=66d89caf-c601-4a1d-a5c0-57fc8cbfad15; XNESSESSIONID=019277dfa099; JSESSIONID=abcTzvJMGx7mt4lFs7aMw; jebe_key=331beb8b-938e-496f-9b32-951dc26e630e%7C823523f09f81eb5b0cf3c30069ff8f5f%7C1552646284939%7C1%7C1552646286399; wp_fold=0; Hm_lvt_3c8ecbfa472e76b0340d7a701a04197e=1552646289,1552646365; first_login_flag=1; ln_uact=13006134009; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebecookies=e2b0632e-655b-4a8b-abd2-7b6fb02116d5|||||; _de=657C948763A73B753A88ADB2F4EF9619; p=f8940921ce2b6ba7193829641d3fc6c30; t=91b44e397644d54f2716e1b21a076e850; societyguester=91b44e397644d54f2716e1b21a076e850; id=970076490; xnsid=7f03a646; ver=7.0; loginfrom=null; Hm_lpvt_3c8ecbfa472e76b0340d7a701a04197e=1552648967"
}
re = request.Request(url=url, headers=headers)
response = request.urlopen(re)
with open('renren.html', 'w', encoding='utf-8') as fp:
    # write()函数必须写入一个str的数据类型
    # read()函数读出来的是一个bytes数据类型
    # bytes -> decode -> str
    # str -> encode -> bytes
    fp.write(response.read().decode('utf-8'))



