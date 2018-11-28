#dansolution13

class Layer:
    name = 0
    size = 0
    scanner_position = 1
    direction = 'd'

    def layerfacts(self):
        return '''This is layer %s. It is %s in size.
        The scanner is at position %s.''' % (self.name, self.size,
        self.scanner_position)

    def scannermove(self):
        if self.scanner_position == self.size:
            self.direction = 'u'
            self.scanner_position -= 1
        elif self.scanner_position == 1:
            self.direction = 'd'
            self.scanner_position += 1
        else:
            if self.direction == 'u':
                self.scanner_position -= 1
            else:
                self.scanner_position += 1

    def timeshift(self,time_input):
        poscount = (2 * self.size) - 2
        if 2 * (time_input % poscount) <= poscount:
            self.scanner_position = (time_input % poscount) + 1
            self.direction = 'd'
        else:
            self.scanner_position = poscount - (time_input % poscount) + 1
            self.direction = 'u'
        #print str(time_input) + ": " + str(self.scanner_position)

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split('\n')
    input1.remove('')
    return input1

def instructionparse(a):
    a = a.split(': ')
    return a

def move_every_scanner(a,b):
    #print a[0].layerfacts()
    for c in b:
        a[c].scannermove()
    return a

def layer_reset(a,b):
    for c in b:
        a[c].scanner_position = 1
        a[c].direction = 'd'
    return a

input_text = 'daninput.txt'
instructionslist = newlinefile(input_text)

#create the dictionary of Layers.
layer_dict = {}
layer_list = []

for item in instructionslist:
    instruction = instructionparse(item)
    layer_dict[int(instruction[0])] = Layer()
    layer_dict[int(instruction[0])].name = int(instruction[0])
    layer_dict[int(instruction[0])].size = int(instruction[1])
    layer_list.append(int(instruction[0]))

#13a solution
firewallsize = max(layer_list) + 1
severity = 0

for i in range(0,firewallsize):
    if i in layer_list:
        if layer_dict[i].scanner_position == 1:
            severity += (i * layer_dict[i].size)
    layer_dict = move_every_scanner(layer_dict,layer_list)

print "13a: " + str(severity)

#13b solution
starttime = 0

#pared down to the bare bones.
while True:
    severity = 0
    for item in layer_list:
        layer_dict[item].scanner_position = 1
        layer_dict[item].direction = 'd'
        layer_dict[item].timeshift(starttime + item)
    for i in layer_list:
        if layer_dict[i].scanner_position == 1:
            severity = 1
            break
    if severity == 0:
        break
    else:
        starttime += 1
    #just to have an idea of the rate of calculation.
    if starttime % 10000 == 0:
        print starttime

print "13b: " + str(starttime)
