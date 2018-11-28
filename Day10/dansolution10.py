#dansolution10

def filereader(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.replace('\n','')
    input1 = input1.split(',')
    return input1

def filereadnoline(a):
    input1 = open(a,'r')
    input1 = input1.read()
    input1 = input1.replace('\n','')
    return input1

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

def densehash(a,b):
    c = a[b]
    for d in range(1,16):
        c = c ^ a[b+d]
    return c

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

#inputs
input_text = 'daninput.txt'
spiral_size = 256

#make spiral list of designated size.
spiral_list = []

for i in range(0,spiral_size):
    spiral_list.append(int(i))

#put the input lengths into a list.
input_lengths = filereader(input_text)
input_lengths = intconvert(input_lengths)

#initialize "skip_size" and "current_position"
skip_size = 0
current_position = 0

#Run through the loop
for i in range(0,len(input_lengths)):
    spiral_list = reverse_segment(current_position,input_lengths[i],spiral_list)
    current_position += (input_lengths[i] + skip_size)
    current_position = current_position % len(spiral_list)
    skip_size += 1
    #print spiral_list

print "10a: " + str(spiral_list[0] * spiral_list[1])

#10b requires several additional steps.

#1. Convert input_lengths into ASCII.
textinput = filereadnoline(input_text)
asciilist = asciilistmaker(textinput)
asciilist = intconvert(asciilist)

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
hexstring = hexcreate(dense_hash_list)

print "10b: " + str(hexstring)
