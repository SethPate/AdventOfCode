import math

prompt = int(input("please enter the puzzle input"))

length = math.ceil(prompt ** .5) #how big a box do i need
    
#now we know what length would be required of a square that would hold our prompt in memory

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