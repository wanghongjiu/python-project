import urllib.request
import urllib.error
try:
    headers = {'User_Agent': 'Mozilla/5.0 (X11; Ubuntu;Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'}
    response = urllib.request.Request('http://www.wtu.edu.cn/', headers=headers)
    html = urllib.request.urlopen(response)
    result = html.read().decode('utf-8')
except urllib.error.URLError as e:
    if hasattr(e, 'reason'):
        print('错误原因是' + str(e.reason))
except urllib.error.HTTPError as e:
    if hasattr(e, 'code'):
        print('错误状态码是' + str(e.code))
else:
    print('请求成功通过。')
    print(result)
