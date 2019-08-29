import re

content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra strings'
content1 = re.sub('\d+', '', content)
print(content1)
content2 = re.sub('\d+', 'Replacement', content)
print(content2)

html = '''<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
    经典老歌列表
</p>
<ul id="list" class="list-group">
    <li data-view="2">一路有你</li>
    <li data-view="7">
        <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
    </li>
    <li data-view="4" class="active">
        <a href="/3.mp3" singer="齐秦">往事如风</a>
    </li>
    <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
    <li data-view="5"><a href="/5.MP3" singer="陈慧琳">记事本</a></li>
    <li data-view="5">
        <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
    </li>
</ul>
<div>'''
html = re.sub('<a.*?>|</a>', '', html)
print(html)
results = re.findall('<li.*?>(.*?)</li>', html, re.S)
print(results)
for result in results:
    print(result.strip())
    






