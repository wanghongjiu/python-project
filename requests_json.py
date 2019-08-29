import requests

response = requests.get('http://httpbin.org/get')
print(response.text)
print(type(response.text))
print(response.json())
print(type(response.json()))

