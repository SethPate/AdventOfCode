#dansolution6a

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.replace('\n','')
    input1 = input1.split('\t')
    return input1

def intconvert(a):
    b = []
    b = [int(i) for i in a]
    return b

#find the left-most instance of a given item in a list.
def leftmostinstance(a,b):
    c = 0
    for c in range(0,len(a)):
        if a[c] == b:
            break
    return c

#incrementation.
#store the current value of the max in c.
#start d as a counter to get distance from position in list.
#reset the moved memory to 0.
#use mod to get the position for the "wrap-around cases."
#keep going until c gets to zero as the memory is spread.
def posincrement(a,b):
    c = a[b]
    d = 1
    a[b] = 0
    while c > 0:
        a[(b+d) % len(a)] += 1
        d += 1
        c -= 1
    return a

input_text = 'daninput.txt'

#6a solution
memory = newlinefile(input_text)
memory = intconvert(memory)
memorylist = []
e = 1

#put the maximum list value in maxhit.
#find the left-most instance of "maxhit." (Tie goes to the first.)
#change the memory list using the posincrement function.
#if the new memory list exists in the list of all the memory states, break.
#append memory to a list of all of the memory states if not.

while e < 2:
    maxhit = max(memory)
    checkme = leftmostinstance(memory,maxhit)
    memory = posincrement(memory,checkme)
    if memory in memorylist:
        break
    memorylist.append(list(memory))

print "6a: " + str(len(memorylist) + 1)

#6b solution
#very straightforward, b/c all of our memories are stored in a list.
#the position of the second hit is the last one in memory.
#the position of the first hit is the "leftmostinstance."

secondhit = len(memorylist)
firsthit = leftmostinstance(memorylist,memory)

print "6b: " + str(int(secondhit) - int(firsthit))

#some notes: 1--a better way to slice the list?
#2 -- a better while loop than one that goes forever unless there's a break?
