#dansolution21

import math
from random import *

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

def r180(a):
    a = a.replace('/','')
    matchlist = []
    charlength = len(a)
    boxsize = int(math.sqrt(charlength))
    #match 3 - rotate 180
    match = ''
    reducer = charlength
    while reducer >= 0:
        #print reducer
        #print boxsize
        match = match + str(a[reducer - boxsize:reducer][::-1])
        reducer -= boxsize
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

def r270(a):
    #match 4 - rotate 270
    a = a.replace('/','')
    match = ''
    charlength = len(a)
    boxsize = int(math.sqrt(charlength))
    decreaser = boxsize - 1
    while decreaser >= 0:
        for i in range(0,charlength):
            if i % boxsize == decreaser:
                match = match + a[i]
        decreaser -= 1
    return match

def randomizemove(a):
    x = randint(1, 3)
    print x
    if x == 1:
        a = fhoriz(a)
    elif x == 2:
        a = fvert(a)
    elif x == 3:
        a = r90(a)
    return a

input_text = 'daninput.txt'
currentgrid = '.#...####'
#currentgrid = 'abcdefghi'

rules = newlinefile(input_text)
rules2 = []
rules3 = []

#break up the rules into two lists.
for rule in rules:
    if slashcount(rule) == 1:
        rules2.append(rule)
    else:
        rules3.append(rule)

iter_count = 0

if len(currentgrid) % 2 == 0:
    ruleschecklist = list(rules2)
else:
    ruleschecklist = list(rules3)

for i in range(0,len(ruleschecklist)):
    ruleschecklist[i] = ruleschecklist[i].replace('/','')

print ruleschecklist

ruleinput = []

for rule in ruleschecklist:
    ruleinput.append(rule[0:findequals(rule)])

transformcount = 0

while True:
    if currentgrid in ruleinput:
        print currentgrid
        print transformcount
        break
    else:
        currentgrid = randomizemove(currentgrid)
        transformcount += 1
