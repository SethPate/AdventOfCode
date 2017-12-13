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
#computationally too inefficient?
#it works in testing but no result w/ live data after 25 minutes.
starttime = 0

while True:
    layer_dict = layer_reset(layer_dict,layer_list)
    severity = 0
    #print starttime
    for i in range(0,starttime):
        layer_dict = move_every_scanner(layer_dict,layer_list)
    for i in range(0,firewallsize):
        if i in layer_list:
            if layer_dict[i].scanner_position == 1:
                #note the trick! Getting caught at zero still counts.
                #precision not important; just yes/no.
                severity += 1
        layer_dict = move_every_scanner(layer_dict,layer_list)
    #print severity
    if severity == 0:
        break
    else:
        starttime += 1
        #print "miss"

print "13b: " + str(starttime)
