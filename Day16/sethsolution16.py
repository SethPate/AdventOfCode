class linedance(str):
    def __init__(self, dancers):
        self.dancers = dancers
        
    def spin(self, x):
        #moves x digits from the end of the string to the beginning, returns a modified str
        newString = ''
        movingPart = self.dancers[-x:]
        newString += movingPart
        newString += self.dancers[:-x]
        self.dancers = newString
    
    def exchange(self, a, b):
        #switches the dancers at positions a and b, returns a modified str
        locations = [a,b] #these are the places that are switching
        locations.sort() #have to get them in the right order
        print('locations', locations)
        newString = ''
        x = locations[0] #location of first dancer
        print('x', x)
        y = locations[1] #location of second dancer
        print('y', y)
        dancerX = self.dancers[x] #save who's in the first spot
        print('dancerX', dancerX)
        dancerY = self.dancers[y] #save who's in the second spot
        print('dancerY', dancerY)
        newString += self.dancers[:x] #add anything before the first location
        print(newString)
        newString += dancerY #then add who was in the second index before
        print(newString)
        newString += self.dancers[x+1:y] #add anything between the two locations
        print(newString)
        newString += dancerX #add who was in the first index
        print(newString)
        newString += self.dancers[y+1:]
        return newString
        

partA = linedance('abcde')