#dansolution24

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split('\n')
    if '' in input1:
        input1.remove('')
    return input1

def splitme(a):
    for b in range(0,len(a)):
        a[b] = a[b].split('/')
        a[b][0] = int(a[b][0])
        a[b][1] = int(a[b][1])
        a[b].sort()
    return a

input_text = 'testinput.txt'

instructions = newlinefile(input_text)

bridgenodes = splitme(instructions)

bridgelist = []
