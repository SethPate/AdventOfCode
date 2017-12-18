buffer = [0]

steps = 349 #number of steps to take each cycle

cycles = 100000 #number of cycles to take

position = 0

tracker = [] #keeps track of iterations that give position 1

#def spinlock(list, position, tracker):
#    #adds a number to a list according to the spinlock instructions
#    #returns list and new position
##    print('starting spinlock with buffer', buffer, 'position', position)
#    output = []
#    addvalue = max(list) + 1
##    print('changing position to', position, '+', steps, '%', len(buffer))
#    position = (position + steps) % len(buffer) + 1
#    if position == 1:
#        print('position 1 on iteration', addvalue)
#        tracker.append(addvalue)
##    print('meaning', position)
##    print('using everything before position + 1')
#    output = buffer[:position]
##    print(output)
##    print('adding', addvalue)
#    output.append(addvalue)
##    print(output)
##    print('adding everything after position + 1')
#    output += buffer[position:]
##    print('\n')
##    print('location of inserted value is new position')
##    position = output.index(addvalue)
#    return output,position
#    
#for i in range(cycles):
#    buffer, position = spinlock(buffer,position,tracker)

#print(buffer)

#print('part A answer is', buffer[buffer.index(2017)+1])

"""part B: stand back, i'm going to use an equation"""

previous = 0

oneList = []

def givePosition(steps, iteration, previous):
    if iteration == 0:
        return 0
    else:
        return ((steps + previous) % iteration) + 1

for i in range(50000000):
    previous = givePosition(steps,i,previous)
    if previous == 1:
        oneList.append(i)
        
"""it's not 1222154"""