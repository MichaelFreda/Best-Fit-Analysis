# Lab12
# Michael & Derek

from functions import *

text = getText(1).split()
text2 = getText(2).split()
text3 = getText(3).split()
text4 = getText(4).split()
text5 = getText(5).split()
dict = createDict(text)
dict2 = createDict(text2)
dict3 = createDict(text3)
dict4 = createDict(text4)
dict5 = createDict(text5)

print(hLR(text, dict))

assert hLR(text2, dict2) == 0.25, "Wrong ratio"
assert hLR(text3, dict3) == 1, "Wrong ratio"
assert hLR(text4,dict4) == 2/6, "Wrong ratio"
assert hLR(text5,dict5) == 1/5, "Wrong ratio"
print("Success")


