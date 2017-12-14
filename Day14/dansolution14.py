#dansolution14

import collections

input_text = 'hxtvlmkl'
#input_text = 'flqrgnkx'

def hexstring(a):
    myhexstring = ''
    for b in a:
        hexme = str(hex(ord(b))[2:])
        hexme = hexme.zfill(2)
        myhexstring = myhexstring + hexme
    return myhexstring

def hexcreate(a):
    finalhex = ''
    for b in range(0,len(a)):
        hexme = hex(a[b])
        hexme = str(hexme)
        hexme = hexme.replace('0x','')
        if len(hexme) == 1:
            hexme = '0' + hexme
        finalhex = finalhex + hexme
    return finalhex

def binarystring(a):
    scale = 16
    b = bin(int(a, scale))[2:].zfill(8)
    return b

def asciilistmaker(a):
    b = []
    for c in range(0,len(a)):
        b.append(str(ord(a[c])))
    b.append('17')
    b.append('31')
    b.append('73')
    b.append('47')
    b.append('23')
    return b

def intconvert(a):
    b = []
    b = [int(i) for i in a]
    return b

#a = current_position
#b = input_length
#c = spiral_list
def reverse_segment(a,b,c):
    d = []
    f = 0
    for e in range(a,b + a):
        d.append(c[e % len(c)])
    d.reverse()
    for e in range(a,b + a):
        c[e % len(c)] = d[f]
        f += 1
    return c

def densehash(a,b):
    c = a[b]
    for d in range(1,16):
        c = c ^ a[b+d]
    return c

#hexedinput = hexstring(input_text)

#print hexedinput

#binaryinput = binarystring(hexedinput)

#print binaryinput

hash_list = []
spiral_size = 256

#we're going to run the 10b procedure for 128 different text inputs.
for k in range(0,128):

    #the text input is the input string, plus a dash, plus our value k.
    textinput = str(input_text) + "-" + str(k)

    #1. Convert input_lengths into ASCII.
    asciilist = asciilistmaker(textinput)
    asciilist = intconvert(asciilist)
    #print asciilist

    #2. Run procedure on spiral list with input_lengths 64 times.

    spiral_list = []

    for i in range(0,spiral_size):
        spiral_list.append(int(i))

    #initialize "skip_size" and "current_position"
    skip_size = 0
    current_position = 0

    for j in range(0,64):
        for i in range(0,len(asciilist)):
            spiral_list = reverse_segment(current_position,asciilist[i],spiral_list)
            current_position += (asciilist[i] + skip_size)
            current_position = current_position % len(spiral_list)
            skip_size += 1

    #3. Dense hash.
    i = 0
    dense_hash_list = []

    while i < 255:
        dense_hash_list.append(densehash(spiral_list,i))
        i += 16

    dense_hash_list = intconvert(dense_hash_list)

    #4. Convert to hexadecimal.
    hexanswer = hexcreate(dense_hash_list)
    hash_list.append(hexanswer)

#now the new stuff.

binary_list = ''

for item in hash_list:
    binary_input = binarystring(item)
    binary_list = str(binary_list) + str(binary_input)

counter=collections.Counter(binary_list)

print "14a: " + str(counter['1'])

#14b is harder. will revisit in evening.
