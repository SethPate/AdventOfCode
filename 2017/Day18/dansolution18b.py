#dansolution18b

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split('\n')
    if '' in input1:
        input1.remove('')
    return input1

reg_dict_0 = {}
reg_dict_1 = {}

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

def regjgz(current_pos,reg_x,reg_y):
    if reg_x > 0:
        current_pos += int(reg_y)
    else:
        current_pos += 1
    return current_pos

def regmaker(a):
    my_dict = {}
    for a in range(0,len(instructions)):
        item = instructions[a].split(' ')
        if item[1].isalpha() == True and item[1] not in my_dict:
            my_dict[item[1]] = 0
        if len(item) > 2 and item[2] not in my_dict and item[2].isalpha() == True:
            my_dict[item[2]] = 0
    return my_dict

def regsnd(receiving_queue,value):
    receiving_queue.append(value)
    return receiving_queue

def regrcv(receiving_queue,receiving_register):
    receiving_register[value] = receiving_queue[0]
    return receiving_register



input_text = 'daninput.txt'

instructions = newlinefile(input_text)

reg_dict_0 = regmaker(instructions)
reg_dict_1 = regmaker(instructions)

reg_dict_0['p'] = 0
reg_dict_1['p'] = 1

term0 = 0
term1 = 0

print reg_dict_1
print reg_dict_0

reg_1_queue = []
reg_0_queue = []

reg_1_instruction_pos = 0
reg_0_instruction_pos = 0

reg_1_send_count = 0
reg_0_send_count = 0
breakflag_0 = 0
breakflag_1 = 0

while int(breakflag_1) + int(breakflag_0) < 2:

    #print "starting reg0"

    while breakflag_0 == 0 and reg_0_instruction_pos >= 0 and reg_0_instruction_pos < len(instructions) and term0 == 0:
        instruction = instructions[reg_0_instruction_pos].split(' ')
        if instruction[0] == 'snd':
            reg_1_queue = regsnd(reg_1_queue,reg_dict_0[instruction[1]])
            #print "1q:" + str(len(reg_1_queue))
            reg_0_instruction_pos += 1
            reg_0_send_count += 1
        elif instruction[0] == 'set':
            if instruction[2] in reg_dict_0:
                checkme = int(reg_dict_0[instruction[2]])
            else:
                checkme = int(instruction[2])
            reg_dict_0[instruction[1]] = regset(reg_dict_0[instruction[1]],checkme)
            reg_0_instruction_pos += 1
        elif instruction[0] == 'add':
            if instruction[2] in reg_dict_0:
                checkme = int(reg_dict_0[instruction[2]])
            else:
                checkme = int(instruction[2])
            reg_dict_0[instruction[1]] = regadd(reg_dict_0[instruction[1]],checkme)
            reg_0_instruction_pos += 1
        elif instruction[0] == 'mul':
            if instruction[2] in reg_dict_0:
                checkme = int(reg_dict_0[instruction[2]])
            else:
                checkme = int(instruction[2])
            reg_dict_0[instruction[1]] = regmul(reg_dict_0[instruction[1]],checkme)
            reg_0_instruction_pos += 1
        elif instruction[0] == 'mod':
            if instruction[2] in reg_dict_0:
                checkme = int(reg_dict_0[instruction[2]])
            else:
                checkme = int(instruction[2])
            reg_dict_0[instruction[1]] = regmod(reg_dict_0[instruction[1]],checkme)
            reg_0_instruction_pos += 1
        elif instruction[0] == 'rcv':
            #print "rcv!"
            if len(reg_0_queue) > 0:
                reg_dict_0[instruction[1]] = reg_0_queue[0]
                #print len(reg_0_queue)
                reg_0_queue.pop(0)
                #print len(reg_0_queue)
                reg_0_instruction_pos += 1
            else:
                breakflag_0 = 1
                reg_0_instruction_pos += 1
        elif instruction[0] == 'jgz':
            if instruction[2] in reg_dict_0:
                checkme = int(reg_dict_0[instruction[2]])
            else:
                checkme = int(instruction[2])
            if instruction[1] in reg_dict_0:
                reg_0_instruction_pos = regjgz(reg_0_instruction_pos,reg_dict_0[instruction[1]],checkme)
            else:
                reg_0_instruction_pos = regjgz(reg_0_instruction_pos,int(instruction[1]),checkme)

    #print "starting reg1"

    while breakflag_1 == 0 and reg_1_instruction_pos >= 0 and reg_1_instruction_pos < len(instructions) and term1 == 0:
        instruction = instructions[reg_1_instruction_pos].split(' ')
        print "reg1: " + str(instruction)
        if instruction[0] == 'snd':
            reg_0_queue = regsnd(reg_0_queue,reg_dict_1[instruction[1]])
            #print reg_0_queue
            reg_1_instruction_pos += 1
            reg_1_send_count += 1
        elif instruction[0] == 'set':
            if instruction[2] in reg_dict_1:
                checkme = int(reg_dict_1[instruction[2]])
            else:
                checkme = int(instruction[2])
            reg_dict_1[instruction[1]] = regset(reg_dict_1[instruction[1]],checkme)
            reg_1_instruction_pos += 1
        elif instruction[0] == 'add':
            if instruction[2] in reg_dict_1:
                checkme = int(reg_dict_1[instruction[2]])
            else:
                checkme = int(instruction[2])
            reg_dict_1[instruction[1]] = regadd(reg_dict_1[instruction[1]],checkme)
            reg_1_instruction_pos += 1
        elif instruction[0] == 'mul':
            if instruction[2] in reg_dict_1:
                checkme = int(reg_dict_1[instruction[2]])
            else:
                checkme = int(instruction[2])
            reg_dict_1[instruction[1]] = regmul(reg_dict_1[instruction[1]],checkme)
            reg_1_instruction_pos += 1
        elif instruction[0] == 'mod':
            if instruction[2] in reg_dict_1:
                checkme = int(reg_dict_1[instruction[2]])
            else:
                checkme = int(instruction[2])
            reg_dict_1[instruction[1]] = regmod(reg_dict_1[instruction[1]],checkme)
            reg_1_instruction_pos += 1
        elif instruction[0] == 'rcv':
            if len(reg_1_queue) > 0:
                #print len(reg_1_queue)
                reg_dict_1[instruction[1]] = reg_1_queue[0]
                reg_1_queue.pop(0)
                #print len(reg_1_queue)
                reg_1_instruction_pos += 1
            else:
                breakflag_1 = 1
                print "BREAK"
                reg_1_instruction_pos += 1
                #print "hello!"
        elif instruction[0] == 'jgz':
            if instruction[2] in reg_dict_1:
                checkme = int(reg_dict_1[instruction[2]])
            else:
                checkme = int(instruction[2])
            if instruction[1] in reg_dict_1:
                reg_1_instruction_pos = regjgz(reg_1_instruction_pos,reg_dict_1[instruction[1]],checkme)
            else:
                reg_1_instruction_pos = regjgz(reg_1_instruction_pos,int(instruction[1]),checkme)

    if len(reg_0_queue) > 0:
        breakflag_0 = 0

    if reg_0_instruction_pos < 0 or reg_0_instruction_pos >= len(instructions):
        breakflag_0 = 1
        term0 = 1

    if len(reg_1_queue) > 0:
        breakflag_1 = 0

    if reg_1_instruction_pos < 0 or reg_1_instruction_pos >= len(instructions):
        breakflag_1 = 1
        term1 = 1

    #print breakflag_0
    #print breakflag_1



print reg_0_send_count
print reg_1_send_count
