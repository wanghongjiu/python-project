from urllib.parse import urlparse

#result = urlparse('http://www.baidu.com/index.html;user?Id=5#comment')
#制定协议类型
result = urlparse('www.baidu.com/index.html;user?Id=5#comment', scheme='https')
print(type(result), result)

