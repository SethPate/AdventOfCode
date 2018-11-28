f = open('sethinput.txt', 'r')
data = f.read()
dataList = []

#data = '{{{},{},{{}}}}'

print(data)

#rid data of all cancelled characters

def removeCancelled(l,s):
    """input: a list of single characters, and a character to "cancel" the next character
    output: a list without "cancelled" characters
    """
    position = 0
    outputList = []
    while position < len(l):
        if l[position] == '!':
#            print('character', i, 'was a canceller', s, 'so skipping next character')
            position += 2
        else:
#            print('adding character', i, 'to list')
            outputList.extend(l[position])
            position += 1
#        print('now at position', position, 'in list len', len(l))

    return outputList

dataList = removeCancelled(data,'!')

#now remove garbage terms

def cleanGarbage(l):
    """input: a list of single characters
    output: a list with 'garbage' terms stripped out, anything enclosed in <>
    """
    outputList = []
    isGarbage = False
    for i in l:
        if i == "<" and not isGarbage:
            isGarbage = True
        elif i == ">":
            isGarbage = False
        elif not isGarbage:
            outputList.extend(i)
    return outputList

dataList = cleanGarbage(dataList)

#now i'll turn this list into a string and remove commas

dataString = ''

for i in dataList:
    dataString += i
    
dataString = dataString.replace(',', '')

print(dataString)

#finally i want to count groups according to the scoring methodology

def score(s):
    """input: a string only of { and } brackets
    output: the score associated with this string
    """
    total = 0
    worth = 0
    for i in s:
        if i == '{':
            worth += 1
        else:
            total += worth
            worth -= 1
    return total

print('part a answer is', score(dataString))

"""part B"""

#dataList = ['<','{','!','>','}','>'] #test input

def garbageCounter(l):
    """input: a list of single characters
    output: the number of non-cancelled characters within <> brackets
    """
    total = 0
    position = 0
    isGarbage = False
    while position < len(l):
        if l[position] == "<" and not isGarbage:
            isGarbage = True
            position += 1
        elif l[position] == ">":
            isGarbage = False
            position += 1
        elif l[position] == "!":
            position += 2
        elif isGarbage:
            total += 1
            position += 1
        else:
            position +=1 
    return total

f = open('sethinput.txt', 'r')
data = f.read()
dataList = []
for i in data:
    dataList.extend(i)

print('part b answer is', garbageCounter(dataList))