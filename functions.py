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
