def genA(previous):
    #given a previous value, returns a new one
    return previous * 16807 % 2147483647

def genB(previous):
    #same as genA with different numbers
    return previous * 48271 % 2147483647

def getBin16(integer):
    #returns the first 16 binary digits of a number
    return bin(integer)[-16:].zfill(16)

a = 699
b = 124

count = 0 #this is my answer

for i in range(5000000):
    a = genA(a)
    b = genB(b)
    while not a % 4 == 0:
        a = genA(a)
    while not b % 8 == 0:
        b = genB(b)
    if getBin16(a) == getBin16(b):
        count += 1
    
#get an answer for a that's divisible for 4

#get a b that's divisible by 8

#compare them

#print('part a answer is', count)

print('part b answer is', count)