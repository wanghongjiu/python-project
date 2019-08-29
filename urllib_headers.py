from urllib import request, parse

url='http://httpbin.org/post'
headers = {'User-Agent': 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',	'Host': 'Httpbin.org'}
dict = {'name': 'Germany'}

data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
result = response.read().decode('utf-8')
print(result)

