#dansolution2a

#import tab-separate sheet as list of lines.
def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split("\n")
    return input1

#break up list at tabs.
def tabsplit(a):
    b = []
    b = a.split("\t")
    return b

#look for minimum value in list.
def minfind(a):
    b = a[0]
    for j in range(1,len(a)):
        if b > a[j]:
            b = a[j]
    return b

#look for maximum value in list.
def maxfind(a):
    b = a[0]
    for j in range(1,len(a)):
        if b < a[j]:
            b = a[j]
    return b

#sort numbers descending. divide every lower number by higher number.
#retain if the remainder is zero.
def modzero(a):
    c = 0
    a.sort(reverse=True)
    for j in range(0,len(a)):
        for k in range(j+1,len(a)):
            if a[j] % a[k] == 0:
                c = a[j] / a[k]
    return c

#convert strings to integers in a list.
def intconvert(a):
    b = []
    b = [int(i) for i in a]
    return b

#import text, make list of lists, convert all strings into integers.
textimport = 'danday2input.txt'

datalines = newlinefile(textimport)
doublelist = []

for i in range(0,len(datalines)-1):
    oneline = tabsplit(datalines[i])
    oneline = intconvert(oneline)
    doublelist.append(oneline)

#2a process
checksum = 0

for i in range(0,len(doublelist)):
    checksum += int(maxfind(doublelist[i])) - int(minfind(doublelist[i]))

print "2a: " + str(checksum)

#2b process
checksum = 0

for i in range(0,len(doublelist)):
    checksum += int(modzero(doublelist[i]))

print "2b: " + str(checksum)
