#excessively lengthy data input part

f = open('sethinput.txt', 'r')
data = f.read()
data = data.split('\n')
del(data[-1])
newdata = []
for i in data:
    saved = ''
    for j in i:
        if j.isalnum() == True or j == ' ':
            saved += j
    newdata.append(saved)
datathree = []
for i in newdata:
    saved = []
    saved = i.split()
    datathree.append(saved)

blockdict = {} #i'll use this variable to store the graph

#now i'll create the graph from the input

for block in datathree:
    name = block[0]
    weight = block[1]
    supports = []
    if len(block) > 2:
        supports.extend(block[2:])
    supported = []
    blockdict[name] = [weight, supports, supported]

#use the "supports" information to fill in which blocks "support" each other block

for block in blockdict:
    if blockdict[block][1]:
        for support in blockdict[block][1]:
            blockdict[support][2].append(block)

#now give me any block without a "supported by" list (there should only be one)

for block in blockdict:
    if not blockdict[block][2]:
        print('answer to part a is', block)
        
#now for part b

def totalWeight(d, block):
    """Returns the sum of the weight of every disk it supports, recursively.
    d is a dictionary, block is a key in that dictionary."""
    if not d[block][1]:
        return int(d[block][0])
    else:
        total = int(d[block][0])
        for support in d[block][1]:
            total += int(totalWeight(d, support))
        return total

def isBalanced(d, block):
    """Returns True if the weight of all supported blocks and all blocks above
    them are equal, False otherwise.
    d is a dictionary, block is a key in that dictionary."""
    if not d[block][1]:
        return True
    else:
        weightsList = {}
        for support in d[block][1]:
            weightsList[support] = totalWeight(d,support)
        if sum(weightsList.values()) / len(weightsList.values()) != weightsList[support]:
            print('unbalanced block at', block, '!')
            for i in weightsList:
                print('support', i, 'weight of', d[i][0], 'total weight of', weightsList[i])
            return False
        else:
            return True

for block in blockdict:
    isBalanced(blockdict, block)