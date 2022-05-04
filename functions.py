# Michael & Derek


def openPaper(num):
	inObject = open("text_"+str(num)+".txt")
	return inObject

def closePaper(num):
	line = openPaper(num).read()
	return line
	