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
    
#    print(reversedBit)
    
    for i in range(len(reversedBit)):
#        print('adding reversal to list', newList, 'character of', reversedBit[i], 'at position', (position + i) % len(l))
        newList[(position + i) % len(l)] = reversedBit[i]
    
    return newList

f = open('sethinput.txt', 'r')
reader = f.read()
reader = reader.split(',')
lengths = [] #this will be a list of integers, and my input
for i in reader:
    lengths.append(int(i))

data = [i for i in range(256)]

position = 0
skipSize = 0

for i in lengths:
#    print('starting with', data, 'at position', position, 'length of', i)
    data = stringSwitcher(data,position,i)
#    print('ended with', data)
#    print('given length', i, 'and SS', skipSize, 'position now', (position + i + skipSize) % len(data))
    position = ((position + i + skipSize) % len(data)) #this should wrap around but it doesn't
    skipSize += 1
#    print('\n')

#print(data)

print('answer to part a is', data[0] * data[1])

"""part B"""

f = open('sethinput.txt', 'r')
reader = f.read()
print('input reader is', reader)
lengths = [] #this will be a list of integers, and my input
print('now adding the ASCII value for each character', [ord(i) for i in reader])
lengths.extend([ord(i) for i in reader]) #add the ASCII value for each char in reader

print('now adding from the puzzle prompt, 17, 31, 73, 47, 23')
lengths.extend([17, 31, 73, 47, 23]) #adding these in directly from puzzle prompt
print('lengths are', lengths)

data = [i for i in range(256)]
print('data is', data)

position = 0
skipSize = 0

for i in range(64): #loop 64 times
#    print('running loop time number', i)
    for j in lengths: #using the new ASCII inputs
        data = stringSwitcher(data,position,j)
        position = ((position + j + skipSize) % len(data))
        skipSize += 1 #maintain skipSize across 64 loops, and position, too
#        print('position of', position, 'skipsize of', skipSize)
#    print('new data after loop', i, 'is', data)
        
xorList = [] #this will be the result of 16 different XOR lists

dataCopy = data.copy()

def xorMaker(l):
#    print('starting xorMaker with list', l)
    answer = 0
    for i in range(len(l)):
        answer ^= l[i]
#    print('xorMaker is crunching list', l, 'and giving answer', answer)
    return answer

while len(dataCopy) > 15: #do this until you delete the whole list here
    xorList.append(xorMaker(dataCopy[:16])) #take 16 chars from list, give to function, add to answer
    del dataCopy[:16] #delete those 16 chars
    
print('xorList is', xorList) #should now be 16 digits long

hexList = [] #god willing, this will be a list of 32 hex characters

for i in xorList:
    hexList.extend(hex(i)[2:])

hexString = ''

for i in hexList:
    hexString += i
    
print('answer to part b is', hexString)