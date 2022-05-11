# Lab12
# Michael & Derek
# Average Word Length = Total Characters / Total Words
# Type- Token Ratio = (Distinct words/total words)
# Hapax Legomena Ratio = (Singularly appearing words/total words)

from functions import *

text = nltk.sent_tokenize(getText(1))
text2 = nltk.sent_tokenize(getText(2))
text3 = nltk.sent_tokenize(getText(3))
text4 = nltk.sent_tokenize(getText(4))
text5 = nltk.sent_tokenize(getText(5))
print(text)
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