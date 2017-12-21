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
    if a.isalpha() == True:
        b = b + str(a)
    return b

def directionset(arrayname,ud,lr,dire):
    if arrayname[ud][lr] != '+':
        return dire
    else:
        if dire == 'u' or dire == 'd':
            if arrayname[ud][lr - 1] != "|" and arrayname[ud][lr - 1] != ' ':
                return 'l'
            else:
                return 'r'
        else:
            if arrayname[ud - 1][lr] != "-" and arrayname[ud - 1][lr] != " ":
                return 'u'
            else:
                return 'd'


#a = updown
#b = leftright
#c = direction
def movement(a,b,c):
    d = []
    if c == 'd':
        a += 1
    elif c == 'u':
        a -= 1
    elif c == 'l':
        b -= 1
    elif c == 'r':
        b += 1
    else:
        print "ERROR"
    d.append(a)
    d.append(b)
    return d

#a = list position
#b = current word string
def isletter(a,b):
    if a.isalpha() is True:
        b = b + str(a)
    #else:
        #return "no"
    return b

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

if fullmap[0][i] == '|':
    direction = 'd'
else:
    direction = 'r'

updown = 0
leftright = i

totalmove = 0

newdirections = []

letterstring = ''

while True:
    newdirections = movement(updown,leftright,direction)
    if fullmap[updown][leftright] == ' ':
        break
    totalmove += 1
    updown = newdirections[0]
    leftright = newdirections[1]
    letterstring = isletter(fullmap[updown][leftright],letterstring)
    direction = directionset(fullmap,updown,leftright,direction)

print "19a: " + str(letterstring)
print "19b: " + str(totalmove)
