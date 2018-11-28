#dansolution8a

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split('\n')
    if '' in input1:
        input1.remove('')
    return input1

def reglistbuild(a,b):
    a = a.split(' ')
    if a[0] not in b:
        b.append(a[0])
    if a[4] not in b:
        b.append(a[4])
    return b

def get_reg_to_change(a):
    a = a.split(' ')
    return a[0]

def get_reg_to_check(a):
    a = a.split(' ')
    return a[4]

def conduct_operation(b,c_instr):
    c_instr = c_instr.split(' ')
    movement = int(c_instr[2])
    if c_instr[1] == 'dec':
        movement *= -1
    if c_instr[5] == "==" and b == int(c_instr[6]):
        movement = movement
    elif c_instr[5] == ">=" and b >= int(c_instr[6]):
        movement = movement
    elif c_instr[5] == "<=" and b <= int(c_instr[6]):
        movement = movement
    elif c_instr[5] == ">" and b > int(c_instr[6]):
        movement = movement
    elif c_instr[5] == "<" and b < int(c_instr[6]):
        movement = movement
    elif c_instr[5] == "!=" and b != int(c_instr[6]):
        movement = movement
    else:
        movement = 0
    return movement

input_text = 'daninput.txt'

instructions_list = newlinefile(input_text)

reg_dict = {}
reg_list = []
highestevermax = 0

#first, make a list of all of the registry items.
for i in range(0,len(instructions_list)):
    reg_list = reglistbuild(instructions_list[i],reg_list)

#next, make a dictionary with all of the reg_list items initialized at 0.
for i in range(0,len(reg_list)):
    reg_dict[reg_list[i]] = 0

#finally, run the function
for i in range(0,len(instructions_list)):
    reg_to_change = get_reg_to_change(instructions_list[i])
    reg_to_check = reg_dict[get_reg_to_check(instructions_list[i])]
    reg_dict[reg_to_change] += int(conduct_operation(reg_to_check,instructions_list[i]))
    if max(reg_dict.values()) > int(highestevermax):
        highestevermax = max(reg_dict.values())

print "8a: " + str(max(reg_dict.values()))
print "8b: " + str(highestevermax)
