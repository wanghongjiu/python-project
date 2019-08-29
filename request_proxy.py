import requests

proxies = {
    'http': 'http://127.0.0.1:1080',
    'https': 'https://127.0.0.1:1080',
}

response = requests.get('https://www.youtube.com', proxies=proxies)
print(response.status_code)
