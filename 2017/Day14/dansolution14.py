#dansolution14

input_text = 'hxtvlmkl'
#input_text = 'flqrgnkx'

class Coordinate:
    name = []
    x_pos = 0
    y_pos = 0
    display = ''

    def countrychange(self):
        coordinatecheck = self.name
        ncheck = str(coordinate_dict[coordinatecheck].y_pos + 1)
        scheck = str(coordinate_dict[coordinatecheck].y_pos - 1)
        echeck = str(coordinate_dict[coordinatecheck].x_pos + 1)
        wcheck = str(coordinate_dict[coordinatecheck].x_pos - 1)

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
    b = ''
    for c in str(a):
        binval = str(bin(int(c,16))[2:])
        binval = binval.zfill(4)
        b = str(b) + binval
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

def countrybuild(short_list,long_list,check_value):
    check_list = []
    check_list.append([check_value[0] + 1, check_value[1]])
    check_list.append([check_value[0] - 1, check_value[1]])
    check_list.append([check_value[0], check_value[1] + 1])
    check_list.append([check_value[0], check_value[1] - 1])
    for a in check_list:
        if a in long_list:
            short_list.append(a)
    return short_list

def listclean(short_list,long_list):
    for a in short_list:
        if a in long_list:
            long_list.remove(a)
    return long_list

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

#binary_list = ''

coordinate_dict = {}
onecounter = 0
countrylist = []

for y in range(0,len(hash_list)):
    #print hash_list[y]
    binary_input = binarystring(hash_list[y])
    #print binary_input
    for x in range(0,len(binary_input)):
        coordinatename = str(x) + "-" + str(y)
        coordinate_dict[coordinatename] = Coordinate()
        coordinate_dict[coordinatename].name = [x,y]
        coordinate_dict[coordinatename].x_pos = x
        coordinate_dict[coordinatename].y_pos = y
        if binary_input[x] == '1':
            coordinate_dict[coordinatename].display = "#"
            countrylist.append(coordinate_dict[coordinatename].name)
            onecounter += 1
        else:
            coordinate_dict[coordinatename].display = "."

print "14a: " + str(onecounter)

#14b solution. genuinely shocked this worked!
list_of_new_countries = []

while len(countrylist) > 0:
    newcountry = []
    i = 0
    j = 0
    if countrylist[i] not in newcountry and len(newcountry) == 0:
        newcountry.append(countrylist[i])
        newcountry = countrybuild(newcountry,countrylist,countrylist[i])
        countrylist = listclean(newcountry,countrylist)
    while j < len(newcountry):
        newcountry = countrybuild(newcountry,countrylist,newcountry[j])
        countrylist = listclean(newcountry,countrylist)
        j += 1
    list_of_new_countries.append(newcountry)

print "14b: " + str(len(list_of_new_countries))
