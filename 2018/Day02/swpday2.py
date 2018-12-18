import collections

with open("swpday2input.txt","r") as inputFile:
	inputArray = inputFile.readlines()

inputArray = [item.strip() for item in inputArray]


"""
Takes an array of alpha strings.
For each string, determines whether the string
has exactly two characters that repeat (1), 
AND whether the string has exactly three
characters that repeat (2).
Returns the product of (1) and (2).
"""
def partA(inputArray):
	stringsWithTwo = 0
	stringsWithThree = 0
	for string in inputArray:
		charCounts = collections.Counter()
		for char in string:
			charCounts[char] += 1
		if 2 in charCounts.values():
			stringsWithTwo += 1
		if 3 in charCounts.values():
			stringsWithThree += 1
	return stringsWithTwo * stringsWithThree

"""
Takes an array of alpha strings.
Attempts to find two strings who differ from
each other by a single character in one position.
For example: 'fghij' and 'fguij'.
Returns the letters that the two strings share
in common.
Returns false if no strings met the criteria.
"""
def partB(inputArray):
	for word in inputArray:
		for otherWord in inputArray:
			flag = compareStr(word, otherWord)
			if flag:
				return flag

"""
If two strings to see if they differ by a single
character, returns the letters they have in common.
False otherwise.
"""
def compareStr(strA, strB):
	result = ""
	for i in range(len(strA)):
		if strA[i] == strB[i]:
			result += strA[i]
	if len(result) == len(strA) - 1:
		print(strA,strB,result)
		return result
	else:
		return False

print(partB(inputArray))
