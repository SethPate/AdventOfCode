#dansolution9

def fileread(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    return input1

def exclamfix(a):
    b = 0
    c = ''
    while b < len(a):
        if a[b] == "!":
            b += 2
        else:
            c = c + a[b]
            b += 1
    return c

def garbfix(a):
    b = 0
    c = ''
    while b < len(a):
        if a[b] != '<':
            c = c + a[b]
            b += 1
        else:
            d = a.find('>',b)
            b = d + 1
    return c

def garbcount(a):
    e = 0
    b = 0
    c = ''
    while b < len(a):
        if a[b] != '<':
            c = c + a[b]
            b += 1
        else:
            d = a.find('>',b)
            e += (d - b - 1)
            b = d + 1
    return e

#stole this from Seth. Very neat!
def score(s):
    total = 0
    worth = 0
    for i in s:
        if i == '{':
            worth += 1
        else:
            total += worth
            worth -= 1
    return total

input_text = 'daninput.txt'

trashtext = fileread(input_text)
garbcleantext = ''
exclamcleantext = ''
i = 0

#get to just brackets.
exclamcleantext = exclamfix(trashtext)
garbcleantext = garbfix(exclamcleantext)
garbcleantext = garbcleantext.replace(',','')
garbcleantext = garbcleantext.replace('\n','')

garbcleanlist = list(garbcleantext)

#equal number of opens/closes?
openbracket = 0
closedbracket = 0

#for i in range(0,len(garbcleanlist)):
    #if garbcleanlist[i] == '{':
        #openbracket += 1
    #if garbcleanlist[i] == '}':
        #closedbracket += 1

#print openbracket
#print closedbracket

#garbcleanlist2 = []

print "9a: " + str(score(garbcleantext))

#9b solution

print "9b: " + str(garbcount(exclamcleantext))
