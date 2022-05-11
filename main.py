# Lab12
# Michael & Derek
# Average Word Length = Total Characters / Total Words
# Type- Token Ratio = (Distinct words/total words)
# Hapax Legomena Ratio = (Singularly appearing words/total words)

from functions import *

text = getText(1)
text2 = getText(2)
text3 = getText(3)
text4 = getText(4)
text5 = getText(5)

# print(avgSenLen(text))
# print(avgSenLen(text2))
# print(avgSenLen(text3))
# print(avgSenLen(text4))
# print(avgSenLen(text5))
assert avgSenLen(text2) == 2, "Wrong average"
assert avgSenLen(text3) == 10/3, "Wrong average"
assert avgSenLen(text4) == 9/5, "Wrong average"
assert avgSenLen(text5) == 7/5, "Wrong average"
print("Success!")