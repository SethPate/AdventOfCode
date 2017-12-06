def getInput(f):
    """
    input: .txt
    output: a list of integers
    """
    f = open(f, 'r') #open the file
    data = f.read() #read it into a string
    data = data.split() #split on whitespace and read into a list
    for i in range(len(data)):
        data[i] = int(data[i])
    
    return data

def update(l):
    """
    input: l is a list of integers
    output: a list of integers, whose max value has been reduced to 0, and spread down the list
    """
    blocks = max(l) #find the biggest stack and store how many blocks it had
    start = l.index(blocks) #record its location (if it's a tie, start with leftmost)
#   print('list', l, 'biggest is', blocks, 'starting at index', start)
    l[start] = 0 #take all of its blocks away (if it's a tie, start with the leftmost)
    stepper = 1 #how far i've gone in redistributing blocks equally among the people
    while blocks > 0:
        try:
            l[start + stepper] += 1
            blocks -= 1 #reduce n by one, because i've redistributed another "block"
            stepper += 1
        except IndexError:
#            print('reached end of line, typewriter thingy dings back')
            start = 0
            stepper = 0
#   print('finished this stack, new list', l)
    return l

l = getInput('sethinput.txt')

archive = [] #this "list of lists" will store all the configurations of l that have been encountered

cycles = 0 #this is my answer for part A; the number of times "update" has to run to meet an old configuration

while archive.count(l) < 2:
#   print(l)
    l = update(l)
#   print(l)
    archive.append(l.copy()) #this was important; i had to append a copy of list l, not l itself
#   print('archive', archive)
    cycles += 1
    
print("part A answer is", cycles) #finally, give the answer

"""
For part B, just subtract the location of the final l in the archive,
from the number of times the updater ran,
minus 1 because the archive doesn't store the original list.
"""

print("part B answer is", cycles - archive.index(l) - 1)