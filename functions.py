# Michael & Derek


def openPaper(num):
	inObject = open("text_"+str(num)+".txt")
	return inObject

def getText(num):
	line = openPaper(num).read()
	openPaper(num).close()
	return line

def avgWLength(list):
	tLetters = 0
	wordCount = 0
	for char in list:
		tLetters += len(char)
		wordCount += 1
	average = tLetters/wordCount
	return average

def tTR(text):
	wordDict = {}
	dWords = 0
	tWords = 0
	for word in text:
		if word not in wordDict:
		 wordDict[word] = 1 
		else:
		 wordDict[word] += 1
	for word in wordDict:
		dWords += 1
		tWords += wordDict[word]
	ratio = dWords / tWords
	return ratio

def hLR(text):
	wordDict = {}
	sWords = 0
	tWords = 0
	for word in text:
		if word not in wordDict:
		 wordDict[word] = 1 
		else:
		 wordDict[word] += 1
	for word in wordDict:
		if wordDict[word] == 1:
			sWords += 1
		tWords += wordDict[word]
	ratio = sWords / tWords
	return ratio




