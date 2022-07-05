import re

txt = "We went to the Wien last month. Wien is magnificent, though I like Prague more."

print(re.search('^W.*more.$', txt))
print(re.findall('Wien', txt))
print(re.split('\s', txt)) # -> split by \s where \s -> white space ...
print(re.sub('\s', '_', txt)) # -> replace spaces with _ ...
