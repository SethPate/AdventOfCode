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

input_text = 'daninput.txt'

trashtext = fileread(input_text)
garbcleantext = ''
exclamcleantext = ''
i = 0

#get to just brackets.
exclamcleantext = exclamfix(trashtext)
garbcleantext = garbfix(exclamcleantext)
#garbcleantext = garbcleantext.replace(',','')
garbcleantext = garbcleantext.replace('\n','')

garbcleanlist = list(garbcleantext)

#equal number of opens/closes?
openbracket = 0
closedbracket = 0

for i in range(0,len(garbcleanlist)):
    if garbcleanlist[i] == '{':
        openbracket += 1
    if garbcleanlist[i] == '}':
        closedbracket += 1

print openbracket
print closedbracket

garbcleanlist2 = []

for i in range(0,len(garbcleantext)):
    if garbcleantext[i] == '{':
        openbracket += 1
    if garbcleantext[i] == '}':
        closedbracket += 1
    if openbracket == closedbracket:
        j = i - (openbracket + closedbracket) + 1
        garbcleanlist2.append(garbcleantext[j:i+1])
        openbracket = 0
        closedbracket = 0

print garbcleantext
#backwards scoring. hmm.
#score = 0
#scorelist = []
#while len(garbcleantext2) > 1:
    #for i in range(0,len(garbcleantext2)):
        #if garbcleantext2[i:i+2] == '{}':
            #score += 1
    #garbcleantext2 = garbcleantext2.replace('{}','')
    #scorelist.append(score)
    #score = 0

#print scorelist

#j = len(scorelist)
#score = 0
#for i in range(0,len(scorelist)):
    #score += scorelist[i] * j
    #j -= 1



#print scorelist
#print score
