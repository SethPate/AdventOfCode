#dansolution5a

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split("\n")
    input1.remove('')
    return input1

def intconvert(a):
    b = []
    b = [int(i) for i in a]
    return b

#5b procedure
def jumper(a):
    if a >= 3:
        return a - 1
    else:
        return a + 1

input_text = 'daninput.txt'

instructions = newlinefile(input_text)
instructions = intconvert(instructions)
changelist = list(instructions)

movecount = 0

i = 0

#5asolution
while i < len(changelist):
    j = i
    i += changelist[i]
    changelist[j] += 1
    movecount += 1

print "5a: " + str(movecount)

#5bsolution

changelist = []

#this is the key. list a = list b just makes a reference, not a new list.
changelist = list(instructions)
movecount = 0
i = 0

while i < len(changelist):
    j = i
    i += changelist[i]
    changelist[j] = jumper(changelist[j])
    movecount += 1

print "5b: " + str(movecount)
