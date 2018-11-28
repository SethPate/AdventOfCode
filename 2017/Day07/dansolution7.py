#dansolution7a

import collections

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split('\n')
    input1.remove('')
    return input1

class Disc:
    name = ''
    weight = 0
    towerweight = 0
    parent = ''
    children = []

    def discfacts(self):
        return '''This is %s. I weigh %s units. My parent is %s.
        My towerweight is %s.
        My children are %s.''' % (self.name, self.weight,
        self.parent, self.towerweight, self.children)

    def parenthood(self):
        if len(self.children) > 0:
            for a in range(0,len(self.children)):
                disc_dict[self.children[a]].parent = self.name

    def towerweightcascade(self):
        weightadd = int(self.weight)
        n = self.name
        while disc_dict[n].parent != '':
            x = disc_dict[n].parent
            disc_dict[x].towerweight += int(weightadd)
            n = x

    def findanomaly(self):
        weightlist = []
        anomalyweight = 0
        if len(self.children) > 0:
            for a in range(0,len(self.children)):
                weightlist.append(disc_dict[self.children[a]].towerweight)
                weightcounter = collections.Counter(weightlist)
                try:
                    anomalyweight = weightcounter.keys()[weightcounter.values().index(1)]
                except ValueError:
                    return self.name
            for a in range(0,len(self.children)):
                if disc_dict[self.children[a]].towerweight == anomalyweight:
                    return disc_dict[self.children[a]].name
                else:
                    return self.name

    def towerdiff(self):
        weightlist = []
        anomalyweight = 0
        if len(self.children) > 0:
            for a in range(0,len(self.children)):
                weightlist.append(disc_dict[self.children[a]].towerweight)
            weightcounter = collections.Counter(weightlist)
            anomalyweight = int(weightcounter.keys()[weightcounter.values().index(1)])
            modalweight = collections.Counter(weightlist).most_common(1)[0][0]
            return modalweight - anomalyweight

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
    disc_dict[disc_names[i]].weight = int(findweight(discinput[i]))
    disc_dict[disc_names[i]].towerweight = int(findweight(discinput[i]))
    disc_dict[disc_names[i]].children = list(findchildren(discinput[i]))

#7a solution
#assign everybody their parents using the parenthood function.
for i in range(0,len(disc_names)):
    disc_dict[disc_names[i]].parenthood()

#find the disc with no parent.
for i in range(0,len(disc_names)):
    if disc_dict[disc_names[i]].parent == '':
        bottomdisc = disc_dict[disc_names[i]].name

print "7a: " + str(bottomdisc)

#7b solution

#run the recursive function for each of the discs.
for i in range(0,len(disc_names)):
    disc_dict[disc_names[i]].towerweightcascade()

#print out all of the info on the children of our bottomdisc.
#for i in range(0,len(disc_dict[bottomdisc].children)):
    #print disc_dict[disc_dict[bottomdisc].children[i]].discfacts()

#now find the anomalies.
anomaly = bottomdisc
anomalylist = []

while True:
    anomaly = disc_dict[anomaly].findanomaly()
    #print disc_dict[anomaly].discfacts()
    if anomaly not in anomalylist:
        anomalylist.append(anomaly)
    else:
        break

anomaly = anomalylist[len(anomalylist)-1]

#print disc_dict[bottomdisc].towerdiff()

print "7b: " + str(disc_dict[anomaly].weight + disc_dict[bottomdisc].towerdiff())
