import re

str = str()
dict = dict()
dict['a'] = 1

str += dict.__str__()

str = str.replace('{', '').replace('}','').replace("'", "").replace(':', ' ::')

print(str)