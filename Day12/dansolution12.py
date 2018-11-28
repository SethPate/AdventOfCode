#dansolution12

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split('\n')
    return input1

def splitwise(a):
    a = a.replace(',','')
    a = a.split(' ')
    return a

def getconnections(a):
    b = []
    for c in range(2,len(a)):
        linkadd = a[c]
        linkadd = linkadd.replace(',','')
        b.append(linkadd)
    return b

def groupappend(a,b):
    for item in a:
        b.append(item)
    return b

class Pipe:
    name = '0'
    links = []
    group = []

    def pipefacts(self):
        return "This is pipe %s. The links are %s." % (self.name, self.links)

    def groupbuilder(self):
        counter = 0
        self.group = [self.name]
        while counter < len(self.group):
            checker = self.group[counter]
            for a in pipe_dict[checker].links:
                if a not in self.group:
                    self.group.append(a)
            counter += 1

input_text = 'daninput.txt'

#build our class data structure.
connections = newlinefile(input_text)
pipe_dict = {}
pipe_names = []

for item in connections:
    oneconnection = splitwise(item)
    pipe_dict[str(oneconnection[0])] = Pipe()
    pipe_dict[oneconnection[0]].name = str(oneconnection[0])
    pipe_names.append(str(oneconnection[0]))
    pipe_dict[oneconnection[0]].links = getconnections(oneconnection)

#12a: how many in the zero group?

pipe_dict['0'].groupbuilder()
print "12a: " + str(len(pipe_dict['0'].group))

#12b: how many groups in total?

#make a couple of lists.
list_of_groups = []
used_pipes = []

#compare the length of "used_pipes" to "pipe_names"
#check each class item in pipe_names.
#if the item isn't in used_pipes, run the groupbuilder...
#add the item to used_pipes...
#and append the grouplist to a list of groups.
while len(used_pipes) < len(pipe_names):
    for item in pipe_names:
        if item not in used_pipes:
            pipe_dict[item].groupbuilder()
            used_pipes = groupappend(pipe_dict[item].group,used_pipes)
            list_of_groups.append(pipe_dict[item].group)

#remove any lists that are just blank.
list_of_groups.remove([''])

#print the count!
print "12b: " + str(len(list_of_groups))
