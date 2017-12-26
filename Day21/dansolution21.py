#dansolution21

import math
from random import *
import time

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split('\n')
    if '' in input1:
        input1.remove('')
    return input1

def slashcount(a):
    equals = a.index('=')
    return a[0:equals].count('/')

def findequals(a):
    return a.index('=') - 1

def fhoriz(a):
    a = a.replace('/','')
    matchlist = []
    charlength = len(a)
    boxsize = int(math.sqrt(charlength))
    #match 1 - flip horizontal
    match = ''
    reducer = charlength
    while reducer >= 0:
        #print reducer
        #print boxsize
        match = match + str(a[reducer - boxsize:reducer])
        reducer -= boxsize
    return match

def fvert(a):
    a = a.replace('/','')
    matchlist = []
    charlength = len(a)
    boxsize = int(math.sqrt(charlength))
    #match 2 - flip vertical
    match = ''
    increaser = 0
    while increaser < charlength:
        match = match + str(a[increaser:increaser + boxsize][::-1])
        increaser += boxsize
    return match

def r90(a):
    a = a.replace('/','')
    matchlist = []
    tempmatch = ''
    charlength = len(a)
    boxsize = int(math.sqrt(charlength))
    #match 4 - rotate 90
    match = ''
    decreaser = boxsize - 1
    while decreaser >= 0:
        for i in range(0,charlength):
            if i % boxsize == decreaser:
                match = a[i] + match
        decreaser -= 1
    return match

def randomizemove(a):
    x = randint(1, 3)
    if x == 1:
        a = fhoriz(a)
    elif x == 2:
        a = fvert(a)
    else:
        a = r90(a)
    return a

def makelol(a):
    gridlength = len(a)
    gridsize = int(math.sqrt(gridlength))
    gridline = []
    tempgridlist = []
    i = 0
    while i < gridlength:
        gridline = []
        for j in range(0,gridsize):
            gridline.append(a[i + j])
        #print gridline
        tempgridlist.append(gridline)
        i += gridsize
    return tempgridlist

def breakuplol2(a):
    print a
    multibox = []
    x = 0
    y = 0
    gridlength = len(a)
    boxcount = int(math.sqrt(gridlength)) - 1
    while y < boxcount:
        boxpattern = []
        boxpattern.append(a[x])
        boxpattern.append(a[x + 1])
        boxpattern.append(a[x+boxcount])
        boxpattern.append(a[x+boxcount+1])
        multibox.append(boxpattern)
        x += 2
        y += 1
    #while y < gridlength:
        #boxpattern = []
        #boxpattern.append(a[y][x])
        #boxpattern.append(a[y][x+1])
        #boxpattern.append(a[y+1][x])
        #boxpattern.append(a[y+1][x+1])
        #print boxpattern
        #x += 2
        #if x == gridlength:
            #y += 2
            #x = 0
    #print multibox
    #print multibox
    return multibox

def breakuplol3(a):
    print a
    multibox = []
    x = 0
    y = 0
    gridlength = len(a)
    boxcount = int(math.sqrt(gridlength)) -2
    while y < boxcount:
        boxpattern = []
        boxpattern.append(a[x])
        boxpattern.append(a[x + 1])
        boxpattern.append(a[x + 2])
        boxpattern.append(a[x + boxcount])
        boxpattern.append(a[x + boxcount + 1])
        boxpattern.append(a[x + boxcount + 2])
        boxpattern.append(a[x + (2 * boxcount)])
        boxpattern.append(a[x + (2 * boxcount) + 1])
        boxpattern.append(a[x + (2 * boxcount) + 2])
        multibox.append(boxpattern)
        x += 3
        y += 1
    #while y < gridlength:
        #boxpattern = []
        #boxpattern.append(a[y][x])
        #boxpattern.append(a[y][x+1])
        #boxpattern.append(a[y+1][x])
        #boxpattern.append(a[y+1][x+1])
        #print boxpattern
        #multibox.append(boxpattern)
        #x += 2
        #if x == gridlength:
            #y += 2
            #x = 0
    #print multibox
    #print multibox
    #time.sleep(2)
    return multibox


#def breakuplol3(a):
    #multibox = []
    #x = 0
    #y = 0
    #gridlength = len(a)
    #while y < gridlength:
        #boxpattern = []
        #boxpattern.append(a[y][x])
        #boxpattern.append(a[y][x+1])
        #boxpattern.append(a[y][x+2])
        #boxpattern.append(a[y+1][x])
        #boxpattern.append(a[y+1][x+1])
        #boxpattern.append(a[y+1][x+2])
        #boxpattern.append(a[y+2][x])
        #boxpattern.append(a[y+2][x+1])
        #boxpattern.append(a[y+2][x+2])
        #multibox.append(boxpattern)
        #x += 3
        #if x == len(a):
            #y += 3
            #x = 0
    #print multibox
    #return multibox

def makeliststring(a):
    hdist = len(a[0])
    vdist = len(a)
    mystring = ''
    for y in range(0,vdist):
        for x in range(0,hdist):
            mystring = mystring + a[y][x]
    return mystring


input_text = 'daninput.txt'
currentgrid = '.#...####'
#currentgrid = 'abcdefghi'

rules = newlinefile(input_text)

rules_dict = {}
ruleschecklist = []

for rule in rules:
    rule = rule.replace('/','')
    newrule = rule.split(' => ')
    rules_dict[newrule[0]] = newrule[1]

#break up the rules into two lists.
for rule in rules:
    rule = rule.replace('/','')
    ruleschecklist.append(rule)

iter_count = 0

ruleinput = []

print rules

for rule in ruleschecklist:
    ruleinput.append(rule[0:findequals(rule)])

#print ruleinput

transformcount = 0

#print currentgrid

while True:
    if currentgrid in ruleinput:
        #print currentgrid
        #print transformcount
        break
    else:
        currentgrid = randomizemove(currentgrid)
        transformcount += 1

currentgrid = rules_dict[currentgrid]
gridlist = makelol(currentgrid)

#print gridlist

iter_count = 1
while iter_count < 6:

    newgrid = []
    #print gridlist
    for i in range(0,len(gridlist)):
        gridlist[i] = [y for x in gridlist[i] for y in x]
        print len(gridlist[i])
        print gridlist[i]
        print "hello"
        print len(gridlist[i][0])
        #if len(gridlist[i]) <= 4:
            #newgrid.append(gridlist[i])
        if int(math.sqrt(len(gridlist[i]))) % 2 == 0:
            print len(gridlist[i])
            brokengrid = breakuplol2(gridlist[i])
            for j in range(0,len(brokengrid)):
                newgrid.append(brokengrid[j])
        else:
            brokengrid = breakuplol3(gridlist[i])
            for j in range(0,len(brokengrid)):
                newgrid.append(brokengrid[j])

    #print "newgrid"
    #print newgrid

    #newgrid = [y for x in newgrid for y in x]

    #time.sleep(2)
    match = 0

    #print ruleinput

    for k in range(0,len(newgrid)):
    #for k in range(0,len(gridlist)):
        gridstring = makeliststring(newgrid[k])
        #gridstring = makeliststring(gridlist[k])
        match = 0
        while match == 0:
            if gridstring in ruleinput and match == 0:
                #print "hit me!"
                newgrid[k] = rules_dict[gridstring]
                #gridlist[k] = rules_dict[gridstring]
                #print rules_dict[gridstring]
                #print newgrid[k]
                newgrid[k] = makelol(newgrid[k])
                #gridlist[k] = makelol(gridlist[k])
                #print newgrid[k]
                #print rules_dict[gridstring]
                #newgrid[k] = makelol(newgrid[k])
                match = 1
            else:
                gridstring = randomizemove(gridstring)
                #print gridstring
                #time.sleep(2)

    gridlist = list(newgrid)
    #for i in range(0,len(newgrid)):
        #print newgrid[i]
        #flattened_list = [y for x in newgrid[i] for y in x]
        #print flattened_list
        #gridlist.append(flattened_list)
        #gridlist.append(newgrid[i])

    print gridlist
    time.sleep(2)

    #fullgrid = []

    #for j in range(0,len(newgrid[0])):
        #gridline = []
        #for i in range(0,len(newgrid)):
            #gridline.append(newgrid[i][j])
        #fullgrid.append(gridline)

    #for i in range()

    #print fullgrid

    #flattened_list = [y for x in fullgrid for y in x]
    #flattened_list = [y for x in flattened_list for y in x]
    #print flattened_list

    #setcount = int(math.sqrt(len(flattened_list)))

    #gridlist = []
    #listline = []

    #for j in range(0,len(flattened_list)):
        #listline.append(flattened_list[j])
        #if len(listline) == setcount:
            #gridlist.append(listline)
            #listline = []

    iter_count += 1

    #print gridlist

new_flattened_list = list(gridlist)

new_flattened_list = [y for x in new_flattened_list for y in x]
new_flattened_list = [y for x in new_flattened_list for y in x]

print new_flattened_list

print new_flattened_list.count('#')
