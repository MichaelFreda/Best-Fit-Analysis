# Lab12
# Michael & Derek

from functions import *
#AlWAYS NEED THIS!
text = getText(1).split()
# print(text)

print(hLR(text))

text2 = getText(2).split()
text3 = getText(3).split()
text4 = getText(4).split()
text5 = getText(5).split()

assert hLR(text2) == 0.25, "Wrong ratio"
assert hLR(text3) == 1, "Wrong ratio"
assert hLR(text4) == 2/6, "Wrong ratio"
assert hLR(text5) == 1/5, "Wrong ratio"
print("Success")


