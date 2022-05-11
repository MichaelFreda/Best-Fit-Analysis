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
#print(text)

#print(avgPunMarks(text))
#print(avgPunMarks(text2))
#print(avgPunMarks(text3))
#print(avgPunMarks(text4))
#print(avgPunMarks(text5))
assert avgPunMarks(text2) == 10/7, "Wrong average"
assert avgPunMarks(text3) == 4/3, "Wrong average"
assert avgPunMarks(text4) == 1, "Wrong average"
assert avgPunMarks(text5) == 7/5, "Wrong average"
print("Success!")