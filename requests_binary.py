import requests

response = requests.get('https://github.com/favicon.ico')
#print(type(response.text), type(response.content))
#print(response.text)
#print(response.content)

with open('favicon.ico','wb') as f:
    f.write(response.content)
    f.close()


