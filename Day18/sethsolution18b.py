import copy

f = open('testinputb.txt','r')
data = f.readlines()

#create a dictionary of instructions

instructions = {} #list of instructions

for i in range(len(data)):
    instructions[i] = data[i].strip()

print(instructions)

#create two registries, one for each program, differing only in registry[p]

registry0 = {} #stores values for program 0

for i in instructions:
    if instructions[i][4].isalpha():
        registry0[instructions[i][4]] = 0

registry1 = copy.deepcopy(registry0) #stores values for program 1

registry1['p'] = 1 #changes the p value to 1

print(registry0,registry1)

#create two queues, one for each program, holding values "sent" by the other

Q0 = [] #the queue for program 0
Q1 = [] #the queue for program 1

#flow control: two positional variables, one for each program

position0 = 0 #'position' of program 0, controlling which instruction it does
zeroRunning = True #turns program 0 on or off
position1 = 0 #'position' of program 1, controlling which instruction it does
oneRunning = True #turns program 1 on or offs

#execute the instructions

while zeroRunning: #will not run unless it's on
    while position0 in instructions: #will not run unless position is real
        ins = instructions[position0].split(' ')
        print(ins)
        command = ins[0]
        x = ins[1]
        if len(ins) == 3:
            if not ins[2].isalpha():
                y = int(ins[2])
            else:
                y = registry0[ins[2]]
        if command == 'snd':
            if x.isalpha() == True:
                x = registry0[x]
            Q1.append(x) #give this value to program 1
            oneRunning = True #turn program one back on, if it's off
            position0 += 1
        if command == 'rcv':
            y = ins[1]
            if Q0:
                registry0[y] = Q0.pop(0) #pop off the first time in this queue
                position0 += 1
            else:
                print('program 0 entering wait because Q0', Q0)
                zeroRunning = False #turn this program off for the time being
                break

while oneRunning: #will not run unless it's on
    while position1 in instructions: #will not run unless position is real
        ins = instructions[position1].split(' ')
        print(ins)
        command = ins[0]
        x = ins[1]
        if len(ins) == 3:
            if not ins[2].isalpha():
                y = int(ins[2])
            else:
                y = registry1[ins[2]]
        if command == 'snd':
            if x.isalpha() == True:
                x = registry1[x]
            Q0.append(x) #give this value to program 1
            zeroRunning = True #turn program one back on, if it's off
            position1 += 1
        if command == 'rcv':
            y = ins[1]
            if Q1:
                registry1[y] = Q1.pop(0) #pop off the first time in this queue
                position1 += 1
            else:
                print('program 1 entering wait')
                oneRunning = False #turn this program off for the time being
                break

#if a program hits "rcv", it waits until there's something in the queue to recover
#maybe it also sets a flag to true
#and if both flags are true, the system is deadlocked and terminates

if oneRunning == False and zeroRunning == False:
    print('program deadlocked')