import math

prompt = 361527 #taken from input

length = math.ceil(prompt ** .5) #how big a box do i need to hold it

# if the prompt is a "corner", return length - 1; this is the max number of possible steps (least efficent route)
corners = []
corners.append((length - 1) ** 2)
corners.append(length ** 2 - ((length ** 2 - (length - 1) ** 2) // 2))
corners.append(length ** 2)
if prompt in corners:
    print(length - 1)
        
#now find the smallest distance between the prompt and a corner
distances = []
for i in corners:
    distances.append(abs(i - prompt))
mindistance = min(distances)

#return the steps required by subtracting "mindistance" from the max steps required (length - 1)
if length % 2 == 0: #if this a square of even sides
    print("steps required from", prompt, "is", length - mindistance)
else:
    print("steps required from", prompt, "is", length - 1 - mindistance)
    
#part b

#take a prompt, and return the "next" value in the spiral, given a method

def r(n):
    print('\n', 'solving for', n)
    #generates "cells" according to a counterclockwise spiral method and returns the value of the nth cell
    #the value of the nth cell is the sum of values adjacent to the cell when generated
   
    #base cases
    
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2
    if n == 4:
        return 4
    if n == 5:
        return 5
    if n == 6:
        return 10
    if n == 7:
        return 11
    if n == 8:
        return 23
    if n == 9:
        return 25
    
    #how to handle different locations along the edge

    highSquare = math.ceil(n ** .5) ** 2
#    print(highSquare)
    if n != highSquare:
        lowSquare = int(n ** .5 // 1) ** 2
    elif n == highSquare:
        lowSquare = int((highSquare ** .5 - 1) ** 2)
#    print(lowSquare)
    distance = (highSquare - lowSquare) * 2
#    print('distance', distance)
    
    #first
    if n == highSquare - distance / 2 + 1:
#        print('solving for first, so cells', n - 1, n - distance + 6)
        return r(n - 1) + r(n - distance + 6)
    #square
    elif n == highSquare:
#        print('solving for square, so cells', n - 1, n - distance + 3, n - distance + 2)
        return r(n - 1) + r(n - distance + 3) + r(n - distance + 2)
    #second
    elif n == highSquare - distance / 2 + 2:
#        print('solving for second, so cells', n - 1 , n - 2, n - distance + 6, n - distance + 5)
        return r(n - 1) + r(n - 2) + r(n - distance + 6) + r(n - distance + 5)
    #pre-corner
    elif n == highSquare - distance // 4 - 1:
#        print('solving for pre-corner, so cells', n - 1, n - distance + 5, n - distance + 4)
        return r(n - 1) + r(n - distance + 5) + r(n - distance + 4)
    #corner
    elif n == highSquare - distance // 4:
#        print('solving for corner, so cells', n - 1, n - distance + 4)
        return r(n - 1) + r(n - distance + 4)
    #post-corner
    elif n == highSquare - distance // 4 + 1:
#        print('solving for post-corner, so cells', n - 1, n - 2, n - distance + 4, n - distance + 3)
        return r(n - 1) + r(n - 2) + r(n - distance + 4) + r(n - distance + 3)
    #pre-pre-corner (many)
    elif n < highSquare - distance // 4:
#        print('solving for preprecorner, so cells', n - 1, n - distance + 6, n - distance + 5, n - distance + 4)
        return r(n - 1) + r(n - distance + 6) + r(n - distance + 5) + r(n - distance + 4)
    #post-post-corner (many)
    else:
#        print('solving for postpostcorner, so cells', n - 1, n - distance + 4, n - distance + 3, n - distance + 2)
        return r(n - 1) + r(n - distance + 4) + r(n - distance + 3) + r(n - distance + 2)


#for i in range(1, prompt): #start with 0 but stop if you get to the prompt; tell me the answer
#    if r(i) > prompt:
#        print(r(i))
    