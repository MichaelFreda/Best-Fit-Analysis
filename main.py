# Lab12
# Michael & Derek
# Average Word Length = Total Characters / Total Words
# Type- Token Ratio = (Distinct words/total words)
# Hapax Legomena Ratio = (Singularly appearing words/total words)

from functions import *

text = nltk.word_tokenize(getText(1))
dict = createDict(text)
print(avgWLength(text))
print(tTR(text, dict))
print(hLR(text, dict))