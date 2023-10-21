# Exercise 2.10
line = """This is a python program. I learn it to be a good programmer in the future. 
For now I think it is the most enjoyable language I have ever had the opportunity to learn. 
I think that if I ever had the option to be a programmer I would do it in Python."""

splitWords = line.split()

length = len(splitWords)

print("Exercise 2.10: ")
print("This is our string: " + "\n" + line + "\nAnd this is the number of words in it: ")
print(length)

# Exercise 2.11
print(" \n Exercise 2.11:")
myString = 'word'
separatedString = '_'.join(myString)
print("This is the word whose letters will be separated: ")
print(myString)
print("This is our separated text: ")
print(separatedString)

# Exercise 2.12
print("\nExercise 2.12: ")
print("This is a word that contains the first letters from words from our string.")
firstLetters = [word[0] for word in splitWords]
firstWord = ''.join(firstLetters)
print(firstWord)
print("This is a word that contains the last letters from words from our string:")
#Here I delete all the punctuation:
deletedLetters = str.maketrans('', '', '.')
newLine = [word.translate(deletedLetters) for word in splitWords]
lastLetters = [word[-1] for word in newLine]
lastWord = ''.join(lastLetters)
print(lastWord)

# Exercise 2.13
print("\nExercise 2.13: ")
print("This is a whole sum of words in our string: ")
lengthOfAll = [len(word) for word in newLine]
sumOfLengths = sum(lengthOfAll)
print(sumOfLengths)

# Exercise 2.14
print("\nExercise 2.14: ")
print("This is the longest word in our string: ")
longestOfAll=max(splitWords, key=len)
print(longestOfAll)
print("That is the length of the longest word in our string: ")
print(max(lengthOfAll))

# Exercise 2.15
print("\nExercise 2.15: ")
print("This is our list that contains positive integers: ")
L_list = [132, 56, 7, 8, 905, 44, 124, 5, 78, 9, 34, 6, 24, 17, 22, 4, 500]
print("L_list = ", L_list)
numberString = ""
for number in L_list:
    numberString += str(number) #Here I make a string from our list
print("This is the string that is a sequence of digits of numbers from the list: ")
print(numberString)

# Exercise 2.16
print("\nExercise 2.16: ")
print("This is our new string: ")
changedLine = "GvR"
print(changedLine)
print("This is our new string after a change: ")
changedLine = changedLine.replace("GvR", "Guido van Rossum")
print(changedLine)

# Exercise 2.17
print("\nExercise 2.17: ")
print("Here is a string that contains words to sort: ")
lineToSort = "I think that if I ever had the option to be a programmer I would do it in Python"
print(lineToSort)
print("This is the string which is sorted alphabetically: ")
wordsToBeSorted = lineToSort.split()
sortedA = sorted(wordsToBeSorted, key=str.lower)
sortedAlphabetically = ' '.join(sortedA)
print(sortedAlphabetically)
print("This is the string which is sorted by length: ")
sortedB = sorted(wordsToBeSorted, key=len)
sortedByLength = ' '.join(sortedB)
print(sortedByLength)

# Exercise 2.18
print("\nExercise 2.18: ")
bigNumber = 20034576891200321
print("This is our big number from our exercise: ")
print(bigNumber)
stringNumber = str(bigNumber) #Here I make a string from our big number
howManyZeros = stringNumber.count("0")
print("This is how many zeros there are in our string: ")
print(howManyZeros)

# Exercise 2.19
print("\nExercise 2.19: ")
print("This is our list of numbers: ")
print(L_list)
threeParts = [str(number).zfill(3) for number in L_list]
numberOfThree = ','.join(threeParts)
print("This is our string of three blocks numbers: ")
print(numberOfThree)