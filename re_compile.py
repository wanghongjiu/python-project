import re

content = '''Hello 1234567 World_This 
is a Regex Demo'''
pattern = re.compile('Hello.*Demo', re.S)
result = re.match(pattern, content)
print(pattern)
print(result)

