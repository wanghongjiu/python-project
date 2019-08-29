import requests

data = {
    'name': 'germany',
    'age': 22
}
response = requests.get('http://httpbin.org/get',params=data)
print(response.text)

