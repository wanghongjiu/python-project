import requests
import re

response = requests.get('http://news.wtu.edu.cn/zhxw.htm')
response.encoding = 'utf-8'
#print(response.text)
content = response.text

pattern = re.compile('<div.*?single-project-item.*?href="(.*?)".*?title="(.*?)".*?</div>', re.S)
#pattern = re.compile('<div.*?single-project-item.*?href="(.*?)".*?</div>', re.S)
results = re.findall(pattern, content)
for result in results:
    url, title = result
    print(url, title)

