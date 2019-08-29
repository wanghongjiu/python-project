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
print(soup.title)
print(type(soup.title))
print(soup.head)
print(soup.p)
#获取标记名称
print(soup.title.name)
#获取标记属性
print(soup.p.attrs['name'])
print(soup.p['name'])
#获取内容
print(soup.p.string)
#嵌套选择
print(soup.body.a['href'])
print(soup.body.a.string)

html = '''
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
        Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">
            <span>Elsie</span>
        </a> 
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
        and 
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a> 
        and they lived at the bottom of a well.
    </p>
    <p class="story">...</p>
'''
soup = BeautifulSoup(html, 'lxml')
#选择子节点
print(soup.p.contents)
print(soup.p.children)
for i, child in enumerate(soup.p.children):
    print(i, child)
#选择所有子孙节点
print(soup.body.descendants)
for i, child in enumerate(soup.body.descendants):
    print(i, child)
#选择父节点，输出整个父节点的内容
print(soup.a.parent)
#选择祖先节点，输出所有祖先节点
print(list(enumerate(soup.a.parents)))
#选择兄弟节点
print(list(enumerate(soup.a.next_siblings)))
print(list(enumerate(soup.a.previous_siblings)))













