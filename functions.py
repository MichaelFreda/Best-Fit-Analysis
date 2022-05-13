# Michael & Derek
import nltk
nltk.download('punkt')
nltk.download('stopwords')

def openPaper(num):
	"""Opens the text of num file"""
	# Guardian to make sure num is an integer
	assert isinstance(num, int), "num must be an integer"
	# Creates the in Object from the desired text file
	inObject = open("text_"+str(num)+".txt")
	return inObject

def getText(num):
	"""Returns a string for the num text file"""
	# Guardian to make sure num is an integer
	assert isinstance(num, int), "num must be an integer"
	# Calls the openPaper function to create a new textObject
	textObject = openPaper(num)
	# Creates a textString using the previously made textObject
	textString = textObject.read()
	# Closes the text file
	openPaper(num).close()
	return textString

def avgWLength(wordList):
	"""Returns the average word length in list"""
	# Guardian to make sure wordList is a list
	assert isinstance(wordList, list), "text must be a list"
	# Assigns default values
	tLetters = 0
	wordCount = 0
	# For loop using list
	for char in wordList:
		# Adds the letters from char to tLetters
		tLetters += len(char)
		# Goes up 1 for every word counted
		wordCount += 1
	# Computes average
	average = tLetters/wordCount
	return average

def tTR(text, textDict):
	"""Returns the Type-Token Ratio using the text string and the desired dict dictionary"""
	# Guardian to make sure text is a string
	assert isinstance(text, str), "text must be a string"
	# Guardian to make sure textDict is a dictionary
	assert isinstance(textDict, dict), "textDict must be a dictionary"
	# Assigns default values
	dWords = 0
	tWords = 0
	# For loop using dict
	for word in textDict:
		# Adds 1 for every distinct word in dict
		dWords += 1
		# Add the dict value of every word to tWords
		tWords += textDict[word]
	# Returns Type-Token Ratio
	return dWords / tWords

def hLR(text, textDict):
	"""Returns the Hapax Legomena Ratio using the text string and the desired dict dictionary"""
	# Guardian to make sure text is a string
	assert isinstance(text, str), "text must be a string"
	# Guardian to make sure textDict is a dictionary
	assert isinstance(textDict, dict), "textDict must be a dictionary"
	# Assigns default values
	sWords = 0
	tWords = 0
	# For loop using dict
	for word in textDict:
		# If the word only shows up once, add 1 to sWords
		if textDict[word] == 1:
			sWords += 1
		# Add the dict value of every word to tWords
		tWords += textDict[word]
	# Returns Hapax Legomena Ratio
	return sWords/tWords

def createDict(textList):
	"""Creates a dictionary using text"""
	# Guardian to make sure textList is a list
	assert isinstance(textList, list), "textList must be a list"
	# Assigns default values
	wordDict = {}
	# For loop using text
	for word in textList:
		# If word not found, assign a default value of 1
		if word not in wordDict:
		 wordDict[word] = 1 
		# If word already present, add 1
		else:
		 wordDict[word] += 1
	return wordDict

def delNonWord(textList):
	"""Deletes non-words from text"""
	# Guardian to make sure textList is a list
	assert isinstance(textList, list), "textList must be a list"
	# For loop using text
	for word in textList:
		# Determines what counts as a non-word
		if (word == ",") or (word == ".") or (word == "!") or (word == "?"):
			# Removes the non-word from text
			textList.remove(word)
	return textList

def avgSenLen(textList):
	"""Computes and returns the average sentence length in textList"""
	# Guardian to make sure textList is a list
	assert isinstance(textList, list), "textList must be a list"
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
	# Guardian to make sure textList is a list
	assert isinstance(textList, list), "textList must be a list"
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
	"""Computes a stylistic fingerprint for num text"""
	# Guardian to make sure num is an integer
	assert isinstance(num, int), "num must be an integer"
	# Assigns default value
	fpList = []
	# Uses getText function to get text value
	text = getText(num)
	# Uses split method to break text into a list of words
	list = text.split()
	# Uses text to create a dictionary dict
	dict = createDict(list)
	# Uses nltk sent_tokenize method to break text into sentences
	textList = nltk.sent_tokenize(text)
	# Appends all of the values into fpList
	fpList.append(avgWLength(list))
	fpList.append(tTR(text, dict))
	fpList.append(hLR(text, dict))
	fpList.append(avgSenLen(textList))
	fpList.append(avgPunMarks(textList))
	# Returns fpList
	return fpList

def multFP(numList):
	"""Returns a fingerprint that reflects the average of all the texts in numList"""
	# Guardian to make sure textList is a list
	assert isinstance(numList, list), "textList must be a list"
	# Assigns default value
	totFP = []
	totAvgWL = 0
	totTTR = 0
	totHLR = 0
	totAvgSenL = 0
	totAvgPM = 0
	# For loop using numList
	for num in numList:
		# Gets the fingerprint for that individual text
		singleFP = styFP(num)
		# Adds the values of each stat to a total
		totAvgWL += singleFP[0]
		totTTR += singleFP[1]
		totHLR += singleFP[2]
		totAvgSenL += singleFP[3]
		totAvgPM += singleFP[4]
	# Divides totals by 3 and appends it to a new list for an overall fingerprint
	totFP.append(totAvgWL/3)
	totFP.append(totTTR/3)
	totFP.append(totHLR/3)
	totFP.append(totAvgSenL/3)
	totFP.append(totAvgPM/3)
	# Returns totFP
	return totFP

def calcPE(speaker1, speaker2):
	"""Determines the sum of the percent error between each of the stylistic feature values in speaker1's and speaker2's averaged fingerprints"""
	# Guardian to make sure speaker1 and speaker2 are lists
	assert isinstance([speaker1, speaker2], list), "speaker1 and speaker2 must be lists"
	# Assigns default value
	totPE = 0
	# For in loop to go through the five values in a fingerprint
	for i in range(5):
		# Calculates the percent error for each fingerprint value and adds it to a total
		totPE += ((abs(speaker1[i] - speaker2[i])) / ((speaker1[i] + speaker2[i]) / 2)) * 100
	# Returns totPE
	return totPE

def bestFit(speaker1, speaker2, speaker3):
	"""Determines if speaker2 is most similar to speaker1 or speaker3 by comparing the sums of their percent errors from their fingerprints.  In this program, speaker1 will be Father Coughlin, speaker2 will be Trump, and speaker3 will be Martin Luther King Jr."""
	# Guardian to make sure speaker1, speaker2, and speaker3 are lists
	assert isinstance([speaker1, speaker2, speaker3], list), "speaker1, speaker2 and speaker3 must be lists"
	# Calculates the total percent error for each comparison
	compare1 = calcPE(speaker1, speaker2)
	compare2 = calcPE(speaker3, speaker2)
	# Whichever comparison had the lowest total is the most similar to speaker2
	if compare1 < compare2:
		conclusion = "Trump is most similar to Coughlin."
	elif compare1 > compare2:
		conclusion = "Trump is most similar to Martin Luther King Jr."
	# If the comparisons are equal, says it is unable to be determined
	else:
		conclusion = "They are too identical to tell."
	# Returns the result
	return conclusion