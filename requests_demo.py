import requests

response = requests.get('https://www.baidu.com/')
print(type(response))
print(response.status_code)
print(response.text)
print(response.cookies)
