#dansolution25

import time

class Turing:
    name = ''
    zeroval = 0
    zeromove = 0
    zerostate = ''
    oneval = 0
    onemove = 0
    onestate = ''

    def turing_facts(self):
        return '''This is %s.
        His zeroval is %s.
        His zeromove is %s.
        His zerostate is %s.
        His oneval is %s.
        His onemove is %s.
        His onestate is %s.''' % (self.name, self.zeroval,
        self.zeromove, self.zerostate, self.oneval,
        self.onemove, self.onestate)

def fileread(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    return input1

def checksumcount(a):
    b = a.index('after') + 6
    c = a.index('steps') - 1
    return a[b:c]

def beginstate(a):
    return a[15:16]

def stateme(a):
    a = a.split('In state')
    return a

def newlinesplit(a):
    a = a.split('\n')
    return a

def getval(a):
    b = a.index('value') + 6
    c = a.index('.')
    return a[b:c]

def getdir(a):
    if a[-3:] == 'ft.':
        return -1
    else:
        return 1

def getnextstate(a):
    return a[-2:-1]

input_text = 'daninput.txt'

instructions = fileread(input_text)

justinstructions = stateme(instructions)

turing_dict = {}

#make the Turing instruction set.
for i in range(1,len(justinstructions)):
    splittest = newlinesplit(justinstructions[i])

    turing_dict[splittest[0][1:2]] = Turing()
    turing_dict[splittest[0][1:2]].name = splittest[0][1:2]
    turing_dict[splittest[0][1:2]].zeroval = int(getval(splittest[2]))
    turing_dict[splittest[0][1:2]].zeromove = int(getdir(splittest[3]))
    turing_dict[splittest[0][1:2]].zerostate = getnextstate(splittest[4])
    turing_dict[splittest[0][1:2]].oneval = int(getval(splittest[6]))
    turing_dict[splittest[0][1:2]].onemove = int(getdir(splittest[7]))
    turing_dict[splittest[0][1:2]].onestate = getnextstate(splittest[8])

    print turing_dict[splittest[0][1:2]].turing_facts()

#print turing_dict

slot_list = [0]
current_position = 0

turing_state = beginstate(instructions)
iter_count = int(checksumcount(instructions))

k = 0

while k < iter_count:
    if slot_list[current_position] == 0:
        slot_list[current_position] = turing_dict[turing_state].zeroval
        current_position += turing_dict[turing_state].zeromove
        if current_position < 0:
            slot_list.insert(0,0)
            current_position = 0
        elif current_position >= len(slot_list):
            slot_list.append(0)
        turing_state = turing_dict[turing_state].zerostate
    else:
        slot_list[current_position] = turing_dict[turing_state].oneval
        current_position += turing_dict[turing_state].onemove
        if current_position < 0:
            slot_list.insert(0,0)
            current_position = 0
        elif current_position >= len(slot_list):
            slot_list.append(0)
        turing_state = turing_dict[turing_state].onestate

    k += 1

print "25a: " + str(slot_list.count(1))
