import re
word="Simple regular expression example"
result=re.findall("gula",word)
print(result)

import re
word="Simple regular expression example regular"
result=re.findall("gula",word)
print(result)

import re
word="Simple regular expression example regular"
result=re.findall("gula",word)
print(result)

space=re.search("\s",word)
print("\n The first space is at : ",space.start())

