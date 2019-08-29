from pyquery import PyQuery as pq

html = '''
<div class="wrap">
<div id="container">
    <ul class="list">
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">forth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a</li>
    </ul>
</div>
<div class="footer"></div>
</div>
'''
doc = pq(html)
items = doc('.list')
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)
print('children:')
lis = items.children()
print(type(lis))
print(lis)
lis = items.children('.active')
print(lis)
print('parent:')
items = doc('.list')
print(items)
container = items.parent()
print(container)
parents = items.parents()
print(parents)




