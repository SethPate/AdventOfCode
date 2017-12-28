#dansolution23

import time

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split('\n')
    if '' in input1:
        input1.remove('')
    return input1

def regset(register,value):
    register = value
    return register

def regsub(register,value):
    register -= value
    return register

def regmul(register,value):
    register *= value
    return register

def regjnz(current_pos,reg_x,reg_y):
    if reg_dict[reg_x] > 0:
        current_pos += int(reg_y)
    else:
        current_pos += 1
    return current_pos

def makedict(a):
    c = {}
    for b in range(0,len(a)):
        item = a[b].split(' ')
        if item[1].isalpha() == True and item[1] not in c:
            c[item[1]] = 0
        if len(item) > 2 and item[2] not in c and item[2].isalpha() == True:
            c[item[2]] = 0
    return c

input_text = 'daninputtemp.txt'

instructions = newlinefile(input_text)

print instructions

reg_dict = makedict(instructions)

print reg_dict

position = 0
int1 = 0
int2 = 0
mulcount = 0
runcount = 0
reg_dict['a'] = 1

#reg_dict['c'] = 123500
#reg_dict['b'] = 106500
#reg_dict['e'] = 2
#reg_dict['d'] = 2
#reg_dict['g'] = 0
#reg_dict['f'] = 1
#reg_dict['h'] = 0

#runcount = 10

while position >= 0 and position < len(instructions):
    item = instructions[position].split(' ')
    runjnz = 'no'
    if item[1].isalpha() == True:
        int1 = int(reg_dict[item[1]])
    else:
        int1 = int(item[1])
    if item[2].isalpha() == True:
        int2 = int(reg_dict[item[2]])
    else:
        int2 = int(item[2])
    if item[1].isalpha() == False and int(item[1]) != 0:
        runjnz = 'yes'
    elif int(reg_dict[item[1]]) != 0:
        runjnz = 'yes'
    if item[0] == 'sub':
        reg_dict[item[1]] -= int2
        position += 1
    elif item[0] == 'set':
        reg_dict[item[1]] = int2
        position += 1
    elif item[0] == 'mul':
        reg_dict[item[1]] *= int2
        position += 1
        mulcount += 1
    elif item[0] == 'jnz' and runjnz == 'yes':
        position += int2
    else:
        position += 1

    runcount += 1

print reg_dict
print runcount
#print mulcount
