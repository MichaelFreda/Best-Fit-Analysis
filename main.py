# Lab12
# Michael & Derek

from functions import *

myStr = nltk.word_tokenize(getText(1))
print(myStr[:50])
newStr = delNonWord(myStr[:50])
print(newStr)


assert delNonWord(nltk.word_tokenize("Hello?")) == ["Hello"], "Didn't work"
assert delNonWord(nltk.word_tokenize("Hello!")) == ["Hello"], "Didn't work"
assert delNonWord(nltk.word_tokenize("I can not think right now.")) == ["I","can","not","think","right","now"], "Didn't work"
print("Sucess!")