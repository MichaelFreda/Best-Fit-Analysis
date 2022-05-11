# Lab12
# Michael & Derek
# Average Word Length = Total Characters / Total Words
# Type- Token Ratio = (Distinct words/total words)
# Hapax Legomena Ratio = (Singularly appearing words/total words)

from functions import *

text1 = nltk.sent_tokenize(getText(1))
# text2 = nltk.sent_tokenize(getText(2))
# text3 = nltk.sent_tokenize(getText(3))
# text4 = nltk.sent_tokenize(getText(4))
# text5 = nltk.sent_tokenize(getText(5))


print(avgSenLen(text1))
print(avgPunMarks(text1))