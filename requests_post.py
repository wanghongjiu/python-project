import requests

data = {'name': 'germany','age': 22}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
}
response = requests.post('http://httpbin.org/post', data=data, headers=headers)
print(response.text)
