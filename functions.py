# Michael & Derek
import nltk

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


