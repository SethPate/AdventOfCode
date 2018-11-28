class linedance(str):
    def __init__(self, dancers):
        self.dancers = dancers
        
    def spin(self, x):
        #moves x digits from the end of the string to the beginning, updates the dancers to a modified str
        newString = ''
        movingPart = self.dancers[-x:]
        newString += movingPart
        newString += self.dancers[:-x]
        self.dancers = newString
    
    def exchange(self, a, b):
        #switches the dancers at positions a and b, updates the dancers to a modified str
        locations = [a,b] #these are the places that are switching
        locations.sort() #have to get them in the right order
        newString = ''
        x = locations[0] #location of first dancer
        y = locations[1] #location of second dancer
        dancerX = self.dancers[x] #save who's in the first spot
        dancerY = self.dancers[y] #save who's in the second spot
        newString += self.dancers[:x] #add anything before the first location
        newString += dancerY #then add who was in the second index before
        newString += self.dancers[x+1:y] #add anything between the two locations
        newString += dancerX #add who was in the first index
        newString += self.dancers[y+1:]
        self.dancers = newString
        
    def partner(self, a, b):
        #switches the location of dancers a and b, updates the dancers to a modified str
        newString = ''
        x = self.dancers.index(a) #find the index of dancer a
        y = self.dancers.index(b) #and the index of dancer b
        newString = self.exchange(x,y)
        self = newString
        
    def setDancers(self,string):
        self.dancers = string

def inputParser(instruction,linedance):
    #takes a string instruction and carries it out on the linedance given
    move = instruction[0]
    instruction = instruction[1:]
    if '/' in instruction:
        instruction = instruction.split('/')
    if move == 's':
        linedance.spin(int(instruction))
    elif move == 'x':
        linedance.exchange(int(instruction[0]),int(instruction[1]))
    elif move == 'p':
        linedance.partner(instruction[0],instruction[1])

partA = linedance('abcdefghijklmnop')

#partA = linedance('abcde')

f = open('sethinput.txt', 'r')
data = f.read()
data = data.strip()
data = data.split(',')

"""here's just part A."""

#for instruction in data:
#    inputParser(instruction,partA)
#
#print('part a answer is', partA.dancers)

savedStates = {}
counter = 0
cycle = 480000

while counter < cycle:
    for instruction in data:
        oldState = partA.dancers
        savedStates[counter] = oldState
        inputParser(instruction,partA)
        counter += 1

print('cycle', cycle)
instructions = len(data)
print('instructions', instructions)
loops = 1000000000
print('number of loops', loops)
iteration = instructions * loops
print('so search for iteration', iteration)
adjusted = iteration % cycle
print('on cycle index', adjusted)

print('part b answer is', savedStates[adjusted])