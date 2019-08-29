html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dormouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>, 
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and 
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; 
and they lived at the bottom of a well.</p>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
#格式化代码
print(soup.prettify())
#取出title标签的内容
print(soup.title.string)

