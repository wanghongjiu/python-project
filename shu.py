import requests
from bs4 import BeautifulSoup as bs

headers ={
    'cookie': 'miid=32475322141625665; cna=uYr6E3bmXTACARsRejzpPIUu; tg=0; enc=9naFMJB7nA8qjYp0BgGhy6ZR6ojzvKOUwu8Hny43fpHkvjBLMfR8TbTjUiooumJ9ZIHm6KYd%2FjgkdaOoo1jNaQ%3D%3D; UM_distinctid=166c7c846b2ee-03cf0f87f77013-8383268-100200-166c7c846b454; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; t=7aac382c611515029ddb904ec9b5189a; cookie2=17ce8b90e1b599f20c60bf7485bce1f0; _tb_token_=39fe3991733ee; lc=VypTyUdOMp6nyy8QsKw%3D; _cc_=VT5L2FSpdA%3D%3D; mt=ci=0_0; XSRF-TOKEN=85c33c4b-3f0b-4b82-b0bf-ab23775ca9e8; v=0; Hm_lvt_3c8ecbfa472e76b0340d7a701a04197e=1552635779,1552636038; cookieCheck=27015; Hm_lpvt_3c8ecbfa472e76b0340d7a701a04197e=1552636058; l=bBPNiIyIvaAaMvFyBOfw5uI8as7OqIObzhVzw4_GjICPOeOM-2kPWZ1Mn-_HC3GVZ666-3yvyk5aB8T5syCV.; isg=BNvbqLOfA-mBKHjBRASi-XB2aj-FGO_axGD-D80Z-FrarP2OV4RVApRuRkyHp0eq',
    'origin': 'https://login.taobao.com',
    'referer': 'https://login.taobao.com/member/login.jhtml?redirectURL=http%3A%2F%2Fshu.taobao.com%2F',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
rs = requests.session()
res = rs.get('https://login.taobao.com/member/login.jhtml?redirectURL=http%3A%2F%2Fshu.taobao.com%2F&TPL_username=wangchowa&TPL_password=&ncoSig=&ncoSessionid=&ncoToken=2932c8aa9ea06a561ca00008510b1203754f7f11&slideCodeShow=false&useMobile=false&lang=zh_CN&loginsite=0&newlogin=0&TPL_redirect_url=http%3A%2F%2Fshu.taobao.com%2F&from=tb&fc=default&style=default&css_style=&keyLogin=false&qrLogin=true&newMini=false&newMini2=false&tid=&loginType=3&minititle=&minipara=&pstrong=&sign=&need_sign=&isIgnore=&full_redirect=&sub_jump=&popid=&callback=&guf=&not_duplite_str=&need_user_id=&poy=&gvfdcname=10&gvfdcre=&from_encoding=&sub=&TPL_password_2=8612e25b98a9d86efc9df96b98696fdd93fed36fcbb7df7c50b2d7f43e3af6906398e99b2046b80a588c722087c59bdfae9dec0a8f35a89b980b01ceffc23237383ad1d62541fa058abc4c274d403330c21460a15df47bac116f6646de7af96a5a9ca0eb6b6ec1f9283075aaa5f7d49d05b5d6a8b7e54cdf43194ce32892e2b5&loginASR=1&loginASRSuc=1&allp=&oslanguage=zh-CN&sr=1366*768&osVer=&naviVer=chrome%7C72.03626121&osACN=Mozilla&osAV=5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F72.0.3626.121+Safari%2F537.36&osPF=Win32&miserHardInfo=&appkey=00000000&nickLoginLink=&mobileLoginLink=https%3A%2F%2Flogin.taobao.com%2Fmember%2Flogin.jhtml%3FredirectURL%3Dhttp%3A%2F%2Fshu.taobao.com%2F%26useMobile%3Dtrue&showAssistantLink=&um_token=HV02PAAZ0b17463f1b121f6d5c8b589300fa1956999999&ua=115%231DQjd11O1TN3j3%2BTTCCU1CsoE562CpA11g2mOCXwvfCcAuB1zOzZCCtuFSg5y51CHsjNWKLyUBKQiLMJh1%2FTHMZhbTsbUCjQOSfyeKwYzMZQKbyJh11GAkdDaLBXyzFpvISSb9lNyWZQi%2FvShEz4vBN8%2B52AurrQ%2Fjfyet1hyWZQiQ%2BghZz8OkNDaTCqyzEQOWOoU1D6H3sDy1%2BXHjj91CvHv9NR7afFhaTntAY0zumZXKM5HaiGsBkOrP0eUfKvD%2BHS12MzpCiXUOyNlW8MOUM1rgiZJ6k5U7aEINy3czEyxEjrIqIqVU3JEi8VAzlcoqgI53A3MGJsbUpaG3xucK%2B3EC%2FVQDE2kYQrq6iZyVuZFBcv2GP2kCcAHkb9XcVVqNtB1lQk10YhCHMKmrP6gOp1Sust3mF%2BZBSC7NIUctijMTr0xXXFwY0cfvneH6zjmJZPw97pmnveQpu8uX9la%2F5W1UMqX5j5bACn3HbXEmSlbhjABOxX9mEs%2BWtwed4cit0KjwcaT3UFifm%2FOWZObdzUwi%2Bmm20r7Ck72RXGHuS8D2kOLDkPSFtnhCtpVu3dFnPGdxzsqyRL%2Fvyc7guKplTSwNTOQV6XcfGaL2PCTX2TZaBx%2BBKI39EWmc7qUFXrAp9D7PVGdUi7U12BPEtalYbcWW8d73ffJCH0m%2BzZiszxu3ILDj1hivmLBsyuij2D9fx0aSWhDWlFXMIr%2F44KfxJQyL%2BGs843%2BrQzpxlNi5UchUincuK1RUs6DurfEM2xWMfIyhKElk4dCV0YJCl7CaLeq%2FUtV3SMKf3FLGcQcbdJp%2BIWE4vh4kv3Xw6IHKetsrZ7BypRHCmAqzi3SxNkpW6VwE5uUXr9rSlQxP%2BbPYDOFuZBSFvQs1SDQU%2F678G%2B', headers=headers)

res.encoding = 'utf-8'

content = res.text
print(content)







