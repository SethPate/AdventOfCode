#dan's combined 3a and 3b

#hard-coding in input because it's just a single number.
inputtext = 361527

#using a class to do this work.
#class holds the name of the point, the horizontal distance from center...
#the vertical distance from center, the Manhattan distance from center...
#and the "value" for the 3b puzzle.
class SpiralPoint:
    name = 0
    hdistance = 0
    vdistance = 0
    mdistance = 0
    value = 0

    #basic function for testing.
    def pointfacts(self):
        print '''This is point %s. I have an hdistance of %s,
        a vdistance of %s, and an mdistance of %s.''' % (self.name,
        self.hdistance, self.vdistance, self.mdistance)

    #movement direction determined based on N/S/E/W facing.
    def movement(self,a):
        if a == 'n':
            self.vdistance += 1
        elif a == 's':
            self.vdistance -= 1
        elif a == 'e':
            self.hdistance += 1
        elif a == 'w':
            self.hdistance -= 1

    #simple calculation of Manhattan distance.
    def mdistancecalc(self):
        return abs(self.hdistance) + abs(self.vdistance)

#turning function. turns are always counterclockwise.
def turnme(a):
    if a == 'e':
        return 'n'
    elif a == 'n':
        return 'w'
    elif a == 'w':
        return 's'
    elif a == 's':
        return 'e'

#using a dictionary for our objects in the class.
spiralpoint_dict = {}

#using a list for comparison of values in 3b.
spiralpoint_list = []

#maximum distance in the "spiral" from the center for each direction.
maxe = 0
maxw = 0
maxn = 0
maxs = 0

#need to tell the system when to stop 3b computations. they are significant.
puzzleb = 0

#starting direction.
direction = 'e'
#initializing variable to signify need to change direction.
directionchange = 0

#going to initialize the center "1".
spiralpoint_dict[1] = SpiralPoint()
spiralpoint_dict[1].value = 1
spiralpoint_list.append(1)

#starting our while loop at 2 b/c 1 is already in.
i = 2

while i <= inputtext:
    #create a new object for each value i.
    spiralpoint_dict[i] = SpiralPoint()
    spiralpoint_dict[i].name = i
    #bring over the h and v distances from the previous object.
    spiralpoint_dict[i].hdistance = spiralpoint_dict[i-1].hdistance
    spiralpoint_dict[i].vdistance = spiralpoint_dict[i-1].vdistance

    #move in the direction we're facing.
    spiralpoint_dict[i].movement(direction)

    #these four conditionals determine if we've reached our max.
    #if we're as furthest in any one direction, we need to turn c-clockwise.
    #we update the max in question and indicate that...
    #we're ready for a direction change.
    if direction == 'e' and abs(spiralpoint_dict[i].hdistance) > maxe:
        maxe = abs(spiralpoint_dict[i].hdistance)
        directionchange = 1

    if direction == 'n' and abs(spiralpoint_dict[i].vdistance) > maxn:
        maxn = abs(spiralpoint_dict[i].vdistance)
        directionchange = 1

    if direction == 'w' and abs(spiralpoint_dict[i].hdistance) > maxw:
        maxw = abs(spiralpoint_dict[i].hdistance)
        directionchange = 1

    if direction == 's' and abs(spiralpoint_dict[i].vdistance) > maxs:
        maxs = abs(spiralpoint_dict[i].vdistance)
        directionchange = 1

    #directionchange needed, so we run the "turnme" function.
    if directionchange == 1:
        direction = turnme(direction)
        directionchange = 0

    #calculate the mdistance.
    spiralpoint_dict[i].mdistance = spiralpoint_dict[i].mdistancecalc()

    #if we're still trying to solve 3b...
    if puzzleb == 0:
        #compare the current spiralpoint w/ every previous spiralpoint.
        #if the abs. of the difference in hdistance AND vdistance are <=1...
        #then we have a "bordering" point...
        #and should increment the "value."
        for j in range(0,len(spiralpoint_list)):
            if abs(spiralpoint_dict[i].hdistance - spiralpoint_dict[spiralpoint_list[j]].hdistance) <= 1 and abs(spiralpoint_dict[i].vdistance - spiralpoint_dict[spiralpoint_list[j]].vdistance) <= 1:
                spiralpoint_dict[i].value += spiralpoint_dict[spiralpoint_list[j]].value

        #add the most recent i to our list of values for future comparison.
        spiralpoint_list.append(i)

        #if the value is greater than the input text...
        #print the answer with "3b"...
        #and then change "puzzleb" to stop running this process.
        #this process would get extremely intensive as our spiral grows.
        if spiralpoint_dict[i].value > inputtext:
            print "3b: " + str(spiralpoint_dict[i].value)
            puzzleb = 1

    #go to the next step.
    i += 1

#print our 3a solution once we've computed the mdistance of the inputtext.
print "3a: " + str(spiralpoint_dict[inputtext].mdistance)
