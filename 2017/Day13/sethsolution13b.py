import copy

def inputParser(string):
    #takes a string of input and turns it into a useful list of digits
    string = string.strip()
    string = string.split(':')
    output = [int(digit) for digit in string]
    return output
    
def firewallBuilder(dictionary, list):
    #calls inputParser to add a list of instructions to a dictionary
    dictionary[list[0]] = [] #the value will be a list of zeros
    for i in range(list[1]):
        dictionary[list[0]].append(0) #build out the depth of each layer
    return dictionary

def firewallFinisher(dictionary):
    #makes sure that the firewall is padded with empty values
    checker = set([i for i in range(max(firewall.keys()))])
    checkAgainst = set(firewall.keys())
    for i in checker.difference(checkAgainst):
        dictionary[i] = 'skip'
    return dictionary

def isCaught(dictionary, t):
#    print('\n', 'testing delay of', t)
    for i in range(len(dictionary)):
        if dictionary[i] == 'skip':
            t += 1
#            print('skipping layer', i, 'time now', t)
        else:
#            print('testing layer', i, 'time now', t)
            double = 2*(len(dictionary[i]) - 1)
            single = len(dictionary[i]) - 1
#            print('for layer', i, 'double', double, 'single', single)
#            print('t % double', t % double)
            position = 0
            if t % double > single:
#                print(t%double, 'is larger than', single)
                position = double % (t % double)
#                print('so position is', double % (t%double))
                t += 1
            else:
#                print('just using', t % double)
                position = t % double
                t += 1
#                print('position', position)
            if position == 0:
#                print('COLLISION')
                return True
    return False

f = open('sethinput.txt', 'r')
data = f.readlines()
    
firewall = {}

for instruction in data:
    firewall = firewallBuilder(firewall, inputParser(instruction))

firewallFinisher(firewall)

delay = 0

while isCaught(firewall,delay):
    delay += 1
    if delay > 10000000:
        break

print(delay)