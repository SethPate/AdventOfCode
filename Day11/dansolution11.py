#dansolution11

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.replace('\n','')
    input1 = input1.split(',')
    if '' in input1:
        input1.remove('')
    return input1

#a = direction instruction
#b = frequency list
def freqmaker_step(a,b):
    if a not in b:
        b[a] = 1
    else:
        b[a] += 1
    return b

#basically, we're updating the frequency table...
#account for the most recent move.
def simplifiedfreq(b):
    if b['se'] > b['nw']:
        b['se'] = b['se'] - b['nw']
        b['nw'] = 0
    elif b['se'] < b['nw']:
        b['nw'] = b['nw'] - b['se']
        b['se'] = 0
    else:
        b['se'] = 0
        b['nw'] = 0
    if b['sw'] > b['ne']:
        b['sw'] = b['sw'] - b['ne']
        b['ne'] = 0
    elif b['sw'] < b['ne']:
        b['ne'] = b['ne'] - b['sw']
        b['sw'] = 0
    else:
        b['sw'] = 0
        b['ne'] = 0
    if b['s'] > b['n']:
        b['s'] = b['s'] - b['n']
        b['n'] = 0
    elif b['s'] < b['n']:
        b['n'] = b['n'] - b['s']
        b['s'] = 0
    else:
        b['s'] = 0
        b['n'] = 0
    return b

#b/c it's a hex grid, n/s only matter if we're further out than e/w.
#this formula gets the distance.
def getdistance(b):
    eastwest = b['sw'] + b['ne'] + b['se'] + b['nw']
    northsouth = b['n'] + b['s']
    if eastwest >= northsouth:
        return eastwest
    else:
        return eastwest + northsouth

#bring in movement as a list.
input_text = 'daninput.txt'
directionlist = newlinefile(input_text)

#get the individual directions into a list w/ no duplicates.
directionset = set(directionlist)
dir_list = list(directionset)

#create dictionary of frequency of movements.
freq_dict = {}

for item in dir_list:
    freq_dict[item] = 0

#initialize max distance.
maxdistance = 0

#simple for loop:
#add a direction to the freq_dict.
#simplify the freq_dict to get the updated position.
#calculate the distance.
for item in directionlist:
    freq_dict = freqmaker_step(item,freq_dict)
    freq_dict = simplifiedfreq(freq_dict)
    totaldistance = getdistance(freq_dict)
    if maxdistance < totaldistance:
        maxdistance = totaldistance

print "11a: " + str(totaldistance)
print "11b: " + str(maxdistance)
