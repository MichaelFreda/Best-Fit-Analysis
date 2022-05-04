# Michael & Derek


def openPaper(num):
	inObject = open("text_"+str(num)+".txt")
	return inObject

def closePaper(num):
	line = openPaper(num).read()
	return line

def avgWLength(list):
	tLetters = 0
	wordCount = 0
	for char in list:
		tLetters += len(char)
		wordCount += 1
	average = tLetters/wordCount
	return average

def tTR(num):
	wordDict = {}
	dWords = 0
	tWords = 0
	for word in closePaper(num).split():
		if word not in wordDict:
		 wordDict[word] = 1 
		else:
		 wordDict[word] += 1
	for word in wordDict:
		dWords += 1
		tWords += wordDict[word]
	# print("Distinct Words: ",dWords)
	# print("Total words: ",tWords)
	# print(dWords/tWords)
	ratio = dWords / tWords
	# print("tTR: ",ratio)
	return ratio




# len of the dictionary
# OVER
# sum the values of the dictionary together
