import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$', content)
print(result)
print(result.group())
print(result.span())
#泛匹配
result = re.match('^Hello.*Demo$', content)
print(result)
print(result.group())
print(result.span())
#匹配目标
result = re.match('^Hello\s(\d+)\s(\d+)\s.*Demo$', content)
print(result)
print(result.group(1))
print(result.group(2))
print(result.span())
#贪婪匹配
result = re.match('^He.*(\d+).*Demo$', content)
print(result)
print(result.group(1))
#非贪婪匹配，多了？
result = re.match('He.*?(\d+).*Demo$', content)
print(result)
print(result.group(1))
#匹配模式
content = '''Hello 1234567 World_This
is a Regex Demo
'''
result = re.match('^He.*?(\d+).*Demo$', content, re.S)
print('1', result.group(1))
#转义
content = 'price is $5.00'
result = re.match('price is \$5\.00', content)
print(result)
#re.search
content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra strings'
result = re.match('Hello.*?(\d+).*?Demo', content)
print(result)
result = re.search('Hello.*?(\d+).*?Demo', content)
print(result)
print(result.group(1))









