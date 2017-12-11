f = open('sethinput.txt', 'r')
reader = f.read()
reader = reader.split(',')
lengths = [] #this will be a list of integers, and my input
for i in reader:
    lengths.append(int(i))

data = [i for i in range(256)]
print(data)
#lengths = [3,4,1,5]

position = 0
skipSize = 0

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
    
for i in lengths:
#    print('starting with', data, 'at position', position, 'length of', i)
    data = stringSwitcher(data,position,i)
#    print('ended with', data)
#    print('given length', i, 'and SS', skipSize, 'position now', (position + i + skipSize) % len(data))
    position = ((position + i + skipSize) % len(data)) #this should wrap around but it doesn't
    skipSize += 1
#    print('\n')

print(data)

print('answer to part a is', data[0] * data[1])