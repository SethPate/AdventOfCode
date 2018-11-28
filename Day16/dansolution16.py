#dansolution16

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.replace('\n','')
    input1 = input1.split(',')
    if '' in input1:
        input1.remove('')
    return input1

#a = list
#b = number to rotate
def spin(a,b):
    rotation = len(a) - (b % len(a))
    removal_list = a[rotation:]
    a = a[:rotation]
    a = removal_list + a
    return a

#a = list
#b = exchange position 1
#c = exchange position 2
def exchange(a,b,c):
    position1val = a[b]
    position2val = a[c]
    a[c] = position1val
    a[b] = position2val
    return a

#a = list
#b = exchange value 1
#c = exchange value 2
def partner(a,b,c):
    position1 = a.index(b)
    position2 = a.index(c)
    a[position1] = c
    a[position2] = b
    return a

def instruction_parse(list_name, instruction_input):
    if instruction_input[0] == 's':
        spin_number = int(instruction_input[1:])
        list_name = spin(list_name,spin_number)
        #print list_name
        return list_name
    elif instruction_input[0] == 'x':
        slash = instruction_input.index('/')
        pos1 = int(instruction_input[1:slash])
        pos2 = int(instruction_input[(slash + 1):])
        list_name = exchange(list_name,pos1,pos2)
        #print list_name
        return list_name
    elif instruction_input[0] == 'p':
        slash = instruction_input.index('/')
        pos1 = instruction_input[1:slash].upper()
        pos2 = instruction_input[(slash + 1):].upper()
        list_name = partner(list_name,pos1,pos2)
        #print list_name
        return list_name

#test_list = ['A','B','C','D','E']

dance_list = []

#make a dance list
for i in range(65,81):
    dance_list.append(chr(i))

input_text = 'daninput.txt'
instructions = newlinefile(input_text)

for item in instructions:
    dance_list = instruction_parse(dance_list,item)

#16a solution

dancestring = ''

for i in range(0,len(dance_list)):
    dancestring = dancestring + dance_list[i]

dancestring = dancestring.lower()

print "16a: " + dancestring.lower()

#16bsolution
#assumption is there HAS to be recurrence at some point.
#figure out where it starts to repeat, and project 1,000,000,000 using mod.

string_list = []

cyclecount = 1
string_list.append(dancestring)

while True:
    for item in instructions:
        dance_list = instruction_parse(dance_list,item)

    dancestring = ''

    for i in range(0,len(dance_list)):
        dancestring = dancestring + dance_list[i]

    dancestring = dancestring.lower()

    if dancestring not in string_list:
        string_list.append(dancestring)
        cyclecount += 1
    else:
        break

print "16b: " + string_list[999999999 % cyclecount]
