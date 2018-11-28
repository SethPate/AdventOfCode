f = open('sethinput.txt', 'r')
data = f.read()
data = data.split('\n')
del data[-1]

#first i'll create a dictionary and populate it with registers

registry = {}

for i in data:
    i = i.split()
    registry[i[0]] = 0

print(registry)
#then i'll evaluate all of the instructions to update the registers

def isCondition(d, l):
    """Input: d, a dictionary, containing l, a term and its comparison.
    Output: True is the condition is satisfied, false if not.
    """
    command = ''
    command += str(d[l[0]]) + ' ' + l[1] + ' ' + str(l[2])
    print('command is', command)
    return eval(command)
    
def act(d, l):
    """Input: d, a dictionary, containing l, a term and instructions to
    increase or decrease it by a certain amount.
    Output: the new value.
    """
    if l[1] == 'inc':
        return int(d[l[0]]) + int(l[2])
    if l[1] == 'dec':
        return int(d[l[0]]) - int(l[2])

valuelist = [] 
"""this will hold the value of every variable during the process,
to meet part B's requirements"""

for i in data:
    i = i.split()
    print(i)
    condition = []
    condition.extend(i[4:7])
    print(condition)
    action = []
    action.extend(i[:3])
    print(action)
    if isCondition(registry, condition):
        print(condition, 'met')
        registry[i[0]] = act(registry, action)
        print('so now', registry[i[0]], 'adding to list')
        valuelist.append(registry[i[0]])
    else:
        print(condition, 'not met')

print('part a answer is', max(registry.values()))
print('part b answer is', max(valuelist))