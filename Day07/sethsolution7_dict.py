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

blockdict = {}

for block in datathree:
    name = block[0]
    weight = block[1]
    supports = []
    if len(block) > 2:
        supports.extend(block[2:])
    supported = []
    blockdict[name] = [weight, supports, supported]

for block in blockdict:
    if blockdict[block][1]:
        for support in blockdict[block][1]:
            blockdict[support][2].append(block)

for block in blockdict:
    if not blockdict[block][2]:
        print(block)