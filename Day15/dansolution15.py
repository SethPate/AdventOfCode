#dansolution15

input_text = 'daninput.txt'

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split('\n')
    input1.remove('')
    return input1

def getnumber(a):
    a = a.split(' ')
    return int(a[4])

#take list input and factor from input.
#multiply to get new number, mod against strange constant.
#append result to the list.
def genbuild(generator_list,generator_factor):
    mostrecent = len(generator_list) - 1
    newnumber = generator_list[mostrecent] * generator_factor
    newnumber = newnumber % 2147483647
    generator_list.append(newnumber)
    return generator_list

#take the most recent addition to the generator list.
#check if it's a factor of the given number using mod.
#if so, add it to a new list.
def pickyjudge(generator_list,generator_factor,new_list):
    mostrecent = len(generator_list) - 1
    if generator_list[mostrecent] % int(generator_factor) == 0:
        new_list.append(generator_list[mostrecent])
    return new_list

#convert input into last 16 digits of binary.
def rightmost16(a):
    b = str(bin(a))[2:]
    b = b.zfill(32)
    b = b[-16:]
    return b

instructions = newlinefile(input_text)
afactor = 16807
bfactor = 48271

afactor15b = 4
bfactor15b = 8

generatora = []
generatorb = []

#start by appending our input into the generator lists.
generatora.append(getnumber(instructions[0]))
generatorb.append(getnumber(instructions[1]))
matchcount = 0

#15a procedure.
#looping through 40,000,000 times.
#starting at 1 to skip the start numbers.
for i in range(1,40000001):
    #this if statement set is to keep our generator lists short.
    #memory might be an issue, so we'll just constantly clear out older values.
    #if there's a match, increment matchcount.
    if i > 2:
        generatora.remove(generatora[0])
        generatorb.remove(generatorb[0])
        generatora = genbuild(generatora,afactor)
        generatorb = genbuild(generatorb,bfactor)
        amatcher = rightmost16(generatora[2])
        bmatcher = rightmost16(generatorb[2])
    else:
        generatora = genbuild(generatora,afactor)
        generatorb = genbuild(generatorb,bfactor)
        amatcher = rightmost16(generatora[i])
        bmatcher = rightmost16(generatorb[i])
    if amatcher == bmatcher:
        matchcount += 1
    #simple timer
    if i % 100000 == 0:
        print i

print "15a: " + str(matchcount)

#15b procdure

generatora = []
generatorb = []

generatora.append(getnumber(instructions[0]))
generatorb.append(getnumber(instructions[1]))

generatora15b = []
generatorb15b = []

matchcount = 0
minlength = 0
targetminlength = 1
i = 0

#we don't know how long this loop will take, so we'll use a while loop.
while targetminlength < 5000000:
    if i > 2:
        generatora.remove(generatora[0])
        generatorb.remove(generatorb[0])
        generatora = genbuild(generatora,afactor)
        generatorb = genbuild(generatorb,bfactor)
    else:
        generatora = genbuild(generatora,afactor)
        generatorb = genbuild(generatorb,bfactor)
    #these use "pickyjudge" to check if they're a multiple of the given factors.
    #if so, append them to a new list.
    generatora15b = pickyjudge(generatora,4,generatora15b)
    generatorb15b = pickyjudge(generatorb,8,generatorb15b)
    #get the length of the shorter of the two lists.
    if len(generatora15b) > len(generatorb15b):
        minlength = len(generatorb15b)
    else:
        minlength = len(generatora15b)
    #if the shorter list is the same as the targetminlength, we can do the check.
    if minlength == targetminlength:
        amatcher = rightmost16(generatora15b[targetminlength - 1])
        bmatcher = rightmost16(generatorb15b[targetminlength - 1])
        if amatcher == bmatcher:
            matchcount += 1
        #once we've run the check at the minlength, we can increment that too.
        targetminlength += 1
    #this to keep the space-saver car running.
    i += 1

print "15b: " + str(matchcount)
