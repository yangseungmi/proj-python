import re

p = re.compile("[a-z]+")
m = p.search("5 p")
print(m)
print(m.start())
print(m.end())
