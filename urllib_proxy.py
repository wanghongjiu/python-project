import urllib.request

proxy_handler = urllib.request.ProxyHandler(
    {'http': 'http://127.0.0.1:1080',
     'https': 'https://127.0.0.1:1080'})

opener = urllib.request.build_opener(proxy_handler)
response = opener.open('http://www.baidu.com')
print(response.read())