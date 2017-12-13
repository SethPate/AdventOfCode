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
    dictionary[list[0]][0] = 1 #here's the location of the security scanner
    flag = True
    dictionary[list[0]] = [dictionary[list[0]],flag] #appends a boolean for direction
    return dictionary

def firewallFinisher(dictionary):
    #makes sure that the firewall is padded with empty values
    checker = set([i for i in range(max(firewall.keys()))])
    checkAgainst = set(firewall.keys())
    for i in checker.difference(checkAgainst):
        print(i)
        dictionary[i] = 'skip'
        print(dictionary[i])
    print(dictionary)
    return dictionary

def wallUpdater(dictionary):
    #updates the firewall after the scanners move
    for layer in dictionary:
        if not dictionary[layer] == 'skip':
            position = dictionary[layer][0].index(1) #mark where the scanner is
            dictionary[layer][0][position] = 0
            if dictionary[layer][1]: #if the flag is on, move forward
                dictionary[layer][0][position + 1] = 1
                if dictionary[layer][0][-1] == 1:
                    dictionary[layer][1] = False
            else:
                dictionary[layer][0][position - 1] = 1
                if dictionary[layer][0][0] == 1:
                    dictionary[layer][1] = True

def partA(dictionary):
    #given a firewall, returns the "severity" of attempting to cross
    #has to remind wallUpdater of which direction to update
    severity = 0
    for i in range(len(dictionary)): #iterate for as many layers as there are in the firewall
        print('now at location', i)
        if dictionary[i][0][0] == 1:
            print('encountered security, adding', i * len(dictionary[i][0]))
            severity += i * len(dictionary[i][0])
        wallUpdater(dictionary)
    return severity

f = open('sethinput.txt', 'r')
data = f.readlines()
    
firewall = {}

for instruction in data:
    firewall = firewallBuilder(firewall, inputParser(instruction))

firewallFinisher(firewall)

print('answer to part A is', partA(firewall))