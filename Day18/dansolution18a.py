#dansolution18a

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split('\n')
    if '' in input1:
        input1.remove('')
    return input1

#maybe worth converting into class...
class Register:
    reg_name = ''
    reg_value = 0

def regsnd(register,mylist):
    if register != 0:
        mylist.append(register)
    return mylist

def regset(register,value):
    register = value
    return register

def regadd(register,value):
    register += value
    return register

def regmul(register,value):
    register *= value
    return register

def regmod(register,value):
    register = register % value
    return register

def regrcv(mylist):
    length = len(mylist)
    return mylist[length - 1]

def regjgz(current_pos,reg_x,reg_y):
    if reg_dict[reg_x] > 0:
        current_pos += int(reg_y)
    else:
        current_pos += 1
    return current_pos

input_text = 'daninput.txt'

instructions = newlinefile(input_text)

print instructions

#create dictionary of register positions.
reg_dict = {}

for i in range(0,len(instructions)):
    item = instructions[i].split(' ')
    #print item
    if item[1].isalpha() == True and item[1] not in reg_dict:
        reg_dict[item[1]] = 0
    if len(item) > 2 and item[2] not in reg_dict and item[2].isalpha() == True:
        reg_dict[item[2]] = 0

print reg_dict
regposition = 0

soundlist = []

#issue right now: need to translate non-numbers into dict. values.

while regposition >= 0 and regposition < len(instructions):
    instruction = instructions[regposition].split(' ')
    #print instruction
    if instruction[0] == 'snd':
        soundlist = regsnd(reg_dict[instruction[1]],soundlist)
        regposition += 1
    elif instruction[0] == 'set':
        if instruction[2] in reg_dict:
            checkme = int(reg_dict[instruction[2]])
        else:
            checkme = int(instruction[2])
        reg_dict[instruction[1]] = regset(reg_dict[instruction[1]],checkme)
        regposition += 1
    elif instruction[0] == 'add':
        if instruction[2] in reg_dict:
            checkme = int(reg_dict[instruction[2]])
        else:
            checkme = int(instruction[2])
        reg_dict[instruction[1]] = regadd(reg_dict[instruction[1]],checkme)
        regposition += 1
    elif instruction[0] == 'mul':
        if instruction[2] in reg_dict:
            checkme = int(reg_dict[instruction[2]])
        else:
            checkme = int(instruction[2])
        reg_dict[instruction[1]] = regmul(reg_dict[instruction[1]],checkme)
        regposition += 1
    elif instruction[0] == 'mod':
        if instruction[2] in reg_dict:
            checkme = int(reg_dict[instruction[2]])
        else:
            checkme = int(instruction[2])
        reg_dict[instruction[1]] = regmod(reg_dict[instruction[1]],checkme)
        regposition += 1
    elif instruction[0] == 'rcv':
        print "Play Sound " + str(regrcv(soundlist))
        break
    elif instruction[0] == 'jgz':
        if instruction[2] in reg_dict:
            checkme = int(reg_dict[instruction[2]])
        else:
            checkme = int(instruction[2])
        regposition = regjgz(regposition,instruction[1],checkme)
    else:
        print "Error"
        break

#print soundlist
