# Lab12
# Michael & Derek
# Average Word Length = Total Characters / Total Words
# Type- Token Ratio = (Distinct words/total words)
# Hapax Legomena Ratio = (Singularly appearing words/total words)

from functions import *

# list of Father Coughlin's speeches
fatherList = [1, 2, 3]
# list of Trump's speeches
trumpList = [4, 5, 6]
# list of MLK's speeches
mlkList = [7, 8, 9]
# average fingerprint of Father Coughlin's speeches
print("Father Coughlin's average fingerprint:")
print(multFP(fatherList))
# average fingerprint of Trump's speeches
print("Trump's average fingerprint:")
print(multFP(trumpList))
# average fingerprint of MLK's speeches
print("Martin Luther King Jr's average fingerprint:")
print(multFP(mlkList))

print(bestFit(multFP(fatherList), multFP(trumpList), multFP(mlkList)))