#dansolution19

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split('\n')
    if '' in input1:
        input1.remove('')
    return input1

def nestedlist(a):
    fulllist = []
    for item in a:
        nlist = [c for c in item]
        fulllist.append(nlist)
    return fulllist

def stringmaker(a,b):
    if a.isalpha() is True:
        b = b + str(a)
    return b

def directionset(a):
    return a

#direction only changes on a + sign.
#everything else, direction is stable.

input_text = 'daninput.txt'

#make the list of lists.
inputmap = newlinefile(input_text)
fullmap = nestedlist(inputmap)

#figure out where we start.
for i in range(0,len(fullmap[0])):
    if fullmap[0][i] != ' ':
        startingpoint = i
        break
