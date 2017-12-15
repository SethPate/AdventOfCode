def knotHash(s):
    #takes an arbitrary string; returns a 32 hex character hash string
    lengths = getLengths(s)
    sparseHash = knot(lengths,256,64)
    denseHash = xorMaker(sparseHash)
    hexString = getHex(denseHash)
    return hexString
    
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
        hexString += hex(digit)[2:].zfill(2)
    return hexString
    
def hashToBinary(s):
    #input: a knot hash of 32 hex characters
    #ouput: a 128 character binary string
    return bin(int(s,16))[2:].zfill(len(s)*4)

def diskBuilder(seed, rows):
    #input: takes a seed and a number of rows to generate
    #output: a list of strings of 1s and 0s
    disk = []
    for i in range(rows):
        rowSeed = seed + '-' + str(i)
        thisRow = hashToBinary(knotHash(rowSeed))
        rowList = []
        for i in thisRow:
            rowList.append(int(i))
        disk.append(rowList)
    return disk

def shader(l, row, col, mask):
    #shades a cell and any call itself on any adjacent positive, unshaded cell
    #returns the updated mask
    print('calling shader on row', row, 'col', col)
    assert mask[row][col] == 0 #confirm that this cell is unshaded
    assert l[row][col] == 1 #confrim that this cell is positive
    mask[row][col] = 1 #shade this cell
    if not col + 1 == len(mask[row]):
        if l[row][col+1] == 1 and mask[row][col+1] == 0: #look right
            shader(l,row,col+1, mask)
    if not col - 1 < 0: #if it's not the end
        if l[row][col-1] == 1 and mask[row][col-1] == 0: #look left
            shader(l,row,col-1, mask)
    if not row - 1 < 0: #if it's not the end
        if l[row-1][col] == 1 and mask[row-1][col] == 0: #look up
            shader(l,row-1,col, mask)
    if not row + 1 == len(mask): #if it's not the end
        if l[row+1][col] == 1 and mask[row+1][col] == 0: #look down
            shader(l,row+1,col, mask)
    return mask

def countRegions(l):
    """input: a list of lists of integers, only 1s and 0s
    output: a count of the 'regions' of adjacent 1s
    """
    mask = copy.deepcopy(disk) #create a mask to search against
    for i in range(len(mask)):
        for j in range(len(mask[i])):
            mask[i][j] = 0
        
    regions = 0 #count these for your answer
    for row in range(len(l)):
        for col in range(len(l[row])):
            if l[row][col] == 1 and mask[row][col] != 1:
                regions += 1
                print('found 1 at row', row, 'col', col)
                print('region count now', regions)
                mask = shader(l,row,col,mask)
                print(mask)
            else:
                mask[row][col] = 1
    print(mask)
            
    return regions

seed = 'ffayrhll'

disk = diskBuilder(seed,128)

totalUsed = 0

for row in disk:
    totalUsed += row.count('1')

print('part A answer is', totalUsed)

print('part B answer is', countRegions)