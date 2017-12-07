#dansolution7a

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split('\n')
    input1.remove('')
    return input1

class Disc:
    name = ''
    weight = 0
    parent = ''
    children = []

    def discfacts(self):
        return '''This is %s. I weigh %s units. My parent is %s.
        My children are %s.''' % (self.name, self.weight,
        self.parent, self.children)

    def parenthood(self):
        if len(self.children) > 0:
            for a in range(0,len(self.children)):
                disc_dict[self.children[a]].parent = self.name

def findweight(a):
    b = a.find('(') + 1
    c = a.find(')')
    return a[b:c]

def findname(a):
    b = a.find(' ')
    return a[0:b]

def findchildren(a):
    b = a.replace(',','')
    b = b.split(' ')
    c = []
    if len(b) > 2:
        for d in range(3,len(b)):
            c.append(b[d])
    return c


input_text = 'daninput.txt'

discinput = newlinefile(input_text)

#put all of our data into the Disc class.
disc_dict = {}
disc_names = []

for i in range(0,len(discinput)):
    disc_names.append(findname(discinput[i]))
    disc_dict[disc_names[i]] = Disc()
    disc_dict[disc_names[i]].name = findname(discinput[i])
    disc_dict[disc_names[i]].weight = findweight(discinput[i])
    disc_dict[disc_names[i]].children = list(findchildren(discinput[i]))

#7a solution
#assign everybody their parents using the parenthood function.
for i in range(0,len(disc_names)):
    disc_dict[disc_names[i]].parenthood()

#find the disc with no parent.
for i in range(0,len(disc_names)):
    if disc_dict[disc_names[i]].parent == '':
        break

print "7a: " + str(disc_dict[disc_names[i]].name)

#7b solution
#7b requires recursion, I think. Will need more time.
