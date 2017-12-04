#dansolution4a

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split("\n")
    return input1

def spacebreaker(a):
    a = a.split(' ')
    return a

#4a check for identicals.
#straightforward: just do a count of the items in the list.
def passchecker(a):
    d = 0
    for b in range(0,len(a)):
        c = a.count(a[b])
        if c > 1:
            d = 1
    return d

#4b check for anagrams.
#for this, we're going to make a list of "sets," list f.
#sets are unordered.
#then do the exact same check as the previous one.
def anagramchecker(a):
    d = 0
    f = []
    for b in range(0,len(a)):
        f.append(set(a[b]))
    for b in range(0,len(f)):
        c = f.count(f[b])
        if c > 1:
            d = 1
    return d

input_text = 'daninput.txt'

passphrases = newlinefile(input_text)

#4a procedure
ppcount = 0

for i in range(0,len(passphrases)-1):
    checkinglist = spacebreaker(passphrases[i])
    if passchecker(checkinglist) == 0:
        ppcount += 1

print "4a: " + str(ppcount)

#4b procedure
ppcount = 0

for i in range(0,len(passphrases)-1):
    checkinglist = spacebreaker(passphrases[i])
    if anagramchecker(checkinglist) == 0:
        ppcount += 1

print "4b: " + str(ppcount)
