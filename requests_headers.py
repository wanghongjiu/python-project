import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'
}

response = requests.get('https://www.zhihu.com/explore', headers=headers)
print(response.text)


