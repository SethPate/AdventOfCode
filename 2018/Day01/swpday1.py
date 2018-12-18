with open("swpday1input.txt","r") as inputFile:
	inputArray = inputFile.readlines()

freqArray = []

for frequency in inputArray:
	frequency = frequency.strip()
	freqAmount = int(frequency[1:])
	if frequency[0] == "+":
		freqArray.append(freqAmount)
	else:
		freqArray.append(-freqAmount)

"""
Takes an array of integer values.
Adds each value together, finding a new sum.
Returns the first sum that is repeated--
that is, the first sum that has already been seen.
The sum begins with 0.
"""
def partB(inputArray):	
	currentSum = 0
	sumSet = set([currentSum])
	while True:
		for value in inputArray:
			currentSum += value
			if currentSum in sumSet:
				print("found match, returning",currentSum)
				return currentSum
			else:
				sumSet.add(currentSum)

print(partB(freqArray))
