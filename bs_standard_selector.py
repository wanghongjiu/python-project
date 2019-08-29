html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
'''
print(soup.find_all('ul'))
print(type(soup.find_all('ul')[0]))
print(soup.find_all('ul')[0])
'''
#遍历输出标签下的内容
for ul in soup.find_all('ul'):
    print(ul.find_all('li'))

print("attrs:")
print(soup.find_all(attrs={'id': 'list-1'}))
print(soup.find_all(attrs={'class': 'element'}))
for el in soup.find_all(attrs={'class': 'element'}):
    print(el)
print(soup.find_all(id='list-1'))
print('class属性(加下划线):')
print(soup.find_all(class_='element'))
#根据文本内容选择，text
print('text:', soup.find_all(text='Foo'))
#find方法
print('find:\n', soup.find('ul'))
print('-----------------------\n', type(soup.find('ul')))
print('-----------------------\n', soup.find('page'))
#CSS选择器
print()



