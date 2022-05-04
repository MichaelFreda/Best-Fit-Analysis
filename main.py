# Lab12
# Michael & Derek

from functions import *

print(avgWLength(["Hi", "my", "name", "is", "Derek"]))

assert avgWLength(["I","am","hungry"]) == 3, "Wrong average"
assert avgWLength(["Hi", "there", "pal"]) == 10/3, "Wrong average"
assert avgWLength(["Uh", "ohhh", "I", "am", "sad"]) == 12/5, "Wrong average"
assert avgWLength(["Last", "lab", "yes", "sir!"]) == 14/4, "Wrong average"
assert avgWLength(["This", "is", "a", "test"]) == 11/4, "Wrong average"
print("Success!")