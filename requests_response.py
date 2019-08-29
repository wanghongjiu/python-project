import requests

response = requests.get('http://www.baidu.com')
print('status_code:', type(response.status_code), response.status_code)
print('headers:', type(response.headers), response.headers)
print('cookies:', type(response.cookies), response.cookies)
print('url:', type(response.url), response.url)
print('history:', type(response.history), response.history)
print(response.text)
