def stringSwitcher(l, position, length):
    """input: a list of numbers, an indexing position, and a length of an integer
    output: a list of numbers, after starting in the input list at "position",
    then counting up to "length", and reversing that part of the list
    """
    newList = l.copy()
        
    reverseThis = []
    for i in range(length):
        reverseThis.append(l[(position + i) % len(l)])
    reversedBit = reverseThis[::-1]
        
    for i in range(len(reversedBit)):
        newList[(position + i) % len(l)] = reversedBit[i]
    
    return newList

def knot(lengths,datarange,iterations):
    """input: a list of integers lengths,
    a range of data, and # of iterations
    output: a list of digits that has been "knotted"
    """
    assert type(lengths) == list
    assert type(datarange) == int
    assert type(iterations) == int
        
    data = [i for i in range(datarange)] #create the plaintext

    position = 0
    skipSize = 0

    for iteration in range(iterations): #as many times as intructed
        for length in lengths:
            data = stringSwitcher(data,position,length)
            position = (position + length + skipSize) % len(data)
            skipSize += 1
    
    return data

def getLengths(s):
    """input: takes a string of any characters as instructions
    output: the ASCII representation of these characters, plus arbitrary suffix
    """
    assert type(s) == str
    lengths = []
    lengths.extend(ord(character) for character in s)
    while 10 in lengths:
        lengths.remove(10) #remove any there's a pesky \n character at the end of s
    lengths.extend([17, 31, 73, 47, 23])
    return lengths

def xorMaker(l):
    """input: a list of digits divisible by 16
    output: a list of digits, each digit is the result of 16 digits in serial XOR
    """
    assert len(l) % 16 == 0
    
    denseHash = []
    copy = l.copy()
    
    while len(copy) > 0:
        block = copy[:16]
        xorResult = 0
        for i in block:
            xorResult ^= i
        denseHash.append(xorResult)
        del copy[:16]
    
    return denseHash

def getHex(l):
    """input: a list of digits
    output: a string of the hex representation of input digits
    """
    hexString = ''
    for digit in l:
        hexString += hex(digit)[2:]
    return hexString

f = open('sethinput.txt', 'r')
reader = f.read()
reader = reader.split(',') #split the string on a comma
lengths = [] #this is my instructions
for i in reader:
    lengths.append(int(i)) #add the integer interpretation to lengths

answerA = knot(lengths,256,1)

print('answer to part a is', answerA[0] * answerA[1])

"""part B"""

f = open('sethinput.txt', 'r')
reader = f.read()

#convert instruction string to ASCII and add suffix

lengths = getLengths(reader)

#run 64 loops

sparseHash = knot(lengths,256,64)

#convert blocks of 16 characters, using serial XOR, for a list of 16 characters

denseHash = xorMaker(sparseHash)

#convert digits to hex characters, for 32 character string

hexString = getHex(denseHash)
    