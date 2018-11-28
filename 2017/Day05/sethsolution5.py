f = open('sethinput5.py', 'r')
rawdata = f.read()
rawdata = rawdata.split()
l = []
for i in rawdata:
    l.append(int(i))

position = 0
counter = 0 #this will be my answer for 5a

"""part A"""

while position <= len(l): #so long as the position is in the list
    steps = 0
    try:
        steps = l[position] #take the number of steps by looking at the value of this location
        l[position] += 1 #increment the position by 1
        position += steps #move the position the required number of steps
    except IndexError: #when i "escape the maze" by exceeding the list,
        print('escape reached for Part A, total steps of', counter) #print the number of steps it took
        break
    counter += 1 #add to the counter every time i fully execute this loop
    
"""Part B"""

f = open('sethinput5.py', 'r')
rawdata = f.read()
rawdata = rawdata.split()
l = []
for i in rawdata:
    l.append(int(i))

position = 0
counter = 0

while position < len(l): #i scrapped the whole "try, except" deal by changing the comparison; this loop is better than part a's
    steps = 0
    steps = l[position] #save the number of steps to take
    if steps >= 3:
        l[position] -= 1 #decrease by 1 if the offset was three or more
    else:
        l[position] += 1 #otherwise, increase by 1
    position += steps #increase the position by offset
    counter += 1 #log that a step was taken

print('escape reached for Part B, total steps of', counter, 'position now at', position, 'list length', len(l))