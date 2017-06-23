import  re

text="共 64 页"

n= re.findall(r'(\w*[0-9]+)\w*',text)[0]
print(n)

