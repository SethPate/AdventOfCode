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

def knot(s,datarange,iterations):
    """input: a string of digit instructions separated by ',',
    a range of data, and # of iterations
    output: a list of digits that has been "knotted"
    """
    assert type(s) == str
    assert type(datarange) == int
    assert type(iterations) == int
    
    lengths = [] #this is my instructions
    s = s.split(',') #split the string on a comma
    for i in s:
        lengths.append(int(i)) #add the integer interpretation to lengths
        
    data = [i for i in range(datarange)] #create the plaintext

    position = 0
    skipSize = 0

    for iteration in range(iterations): #as many times as intructed
        for length in lengths:
            data = stringSwitcher(data,position,length)
            position = (position + length + skipSize) % len(data)
            skipSize += 1
    
    return data

f = open('sethinput.txt', 'r')
reader = f.read()

answerA = knot(reader,256,1)

print('answer to part a is', answerA[0] * answerA[1])