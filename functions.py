# Michael & Derek
import nltk
#nltk.download('punkt')
#nltk.download('stopwords')

def openPaper(num):
	inObject = open("text_"+str(num)+".txt")
	return inObject

def getText(num):
	textObject = openPaper(num)
	textString = textObject.read()
	openPaper(num).close()
	return textString

def avgWLength(list):
	tLetters = 0
	wordCount = 0
	for char in list:
		tLetters += len(char)
		wordCount += 1
	average = tLetters/wordCount
	return average

def tTR(text, dict):
	dWords = 0
	tWords = 0
	for word in dict:
		dWords += 1
		tWords += dict[word]
	ratio = dWords / tWords
	return ratio

def hLR(text, dict):
	sWords = 0
	tWords = 0
	for word in dict:
		if dict[word] == 1:
			sWords += 1
		tWords += dict[word]
	ratio = sWords / tWords
	return ratio

def createDict(text):
	wordDict = {}
	for word in text:
		if word not in wordDict:
		 wordDict[word] = 1 
		else:
		 wordDict[word] += 1
	return wordDict

def delNonWord(text):
	for word in text:
		if (word == ",") or (word == ".") or (word == "!") or (word == "?"):
			text.remove(word)
	return text

def avgSenLen(text):
	tWords = 0
	sentNum = 0
	text = nltk.sent_tokenize(text)
	for sent in text:
		sentLen = len(delNonWord(nltk.word_tokenize(sent)))
		tWords += sentLen
		sentNum += 1
	return tWords/sentNum