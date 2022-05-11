# Michael & Derek
import nltk
# nltk.download('punkt')
# nltk.download('stopwords')

def openPaper(num):
	"""Opens the text of num file"""
	# Creates the in Object from the desired text file
	inObject = open("text_"+str(num)+".txt")
	return inObject

def getText(num):
	"""Returns a string for the num text file"""
	# Calls the openPaper function to create a new textObject
	textObject = openPaper(num)
	# Creates a textString using the previously made textObject
	textString = textObject.read()
	# Closes the text file
	openPaper(num).close()
	return textString

def avgWLength(list):
	"""Returns the average word length in list"""
	# Assigns default values
	tLetters = 0
	wordCount = 0
	# For loop using list
	for char in list:
		# Adds the letters from char to tLetters
		tLetters += len(char)
		# Goes up 1 for every word counted
		wordCount += 1
	# Computes average
	average = tLetters/wordCount
	return average

def tTR(text, dict):
	"""Returns the Type-Token Ratio using the text string and the desired dict dictionary"""
	# Assigns default values
	dWords = 0
	tWords = 0
	# For loop using dict
	for word in dict:
		# Adds 1 for every distinct word in dict
		dWords += 1
		# Add the dict value of every word to tWords
		tWords += dict[word]
	# Returns Type-Token Ratio
	return dWords / tWords

def hLR(text, dict):
	"""Returns the Hapax Legomena Ratio using the text string and the desired dict dictionary"""
	# Assigns default values
	sWords = 0
	tWords = 0
	# For loop using dict
	for word in dict:
		# If the word only shows up once, add 1 to sWords
		if dict[word] == 1:
			sWords += 1
		# Add the dict value of every word to tWords
		tWords += dict[word]
	# Returns Hapax Legomena Ratio
	return sWords/tWords

def createDict(text):
	"""Creates a dictionary using text"""
	# Assigns default values
	wordDict = {}
	# For loop using text
	for word in text:
		# If word not found, assign a default value of 1
		if word not in wordDict:
		 wordDict[word] = 1 
		# If word already present, add 1
		else:
		 wordDict[word] += 1
	return wordDict

def delNonWord(text):
	"""Deletes non-words from text"""
	# For loop using text
	for word in text:
		# Determines what counts as a non-word
		if (word == ",") or (word == ".") or (word == "!") or (word == "?"):
			# Removes the non-word from text
			text.remove(word)
	return text

def avgSenLen(textList):
	"""Computes and returns the average sentence length in textList"""
	# Assigns default values
	tWords = 0
	sentNum = 0
	# For loop using textList
	for sent in textList:
		# Determines sentence length
		sentLen = len(delNonWord(nltk.word_tokenize(sent)))
		# Adds value of sentLen to tWords
		tWords += sentLen
		# Adds 1 to sentNum for every sentence
		sentNum += 1
	# Returns average sentence length
	return tWords/sentNum

def avgPunMarks(textList):
	"""Computes and returns the average punctuation marks used in textList"""
	# Assigns default values
	pMarks = 0
	sentNum = 0
	# For loop using textList
	for sent in textList:
		# Breaks sentence into a list
		sent = nltk.word_tokenize(sent)
		# Adds 1 to sentNum for every sentence
		sentNum += 1
		# For loop using sent
		for char in sent:
			# If char is any of these characters, add 1 to pMarks
			if (char == ".") or (char == "?") or (char == "!") or (char == ",") or (char == ":") or (char == ";") or (char == "-") or (char == "[") or (char == "]") or (char == "{") or (char == "}") or (char == "(") or (char == ")") or (char == "'") or (char == "--"):
				pMarks += 1
	# Returns average punctuation marks
	return pMarks/sentNum

def styFP(num):
	fpList = []
	text = getText(num)
	list =
	textList = nltk.sent_tokenize(text)
	avgWLength(list)
	tTR(text, dict)
	hLR(text, dict)
	avgSenLen(textList)
	avgPunMarks(textList)