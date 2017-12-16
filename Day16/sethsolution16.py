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
#        locations = [x,y]
#        locations.sort()
#        x = locations[0] #location of first dancer
#        y = locations[1] #location of second dancer
        self = newString

partA = linedance('abcde')