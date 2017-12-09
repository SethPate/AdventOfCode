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

    def gettowerweight(self):
        #if len(self.children) > 0:
        for a in range(0,len(self.children)):
            self.towerweight += int(disc_dict[self.children[a]].towerweight)
        print str(self.name) + ": " + str(self.towerweight)

    def findanomaly(self):
        weightlist = []
        anomalyweight = 0
        if len(self.children) > 0:
            for a in range(0,len(self.children)):
                weightlist.append(disc_dict[self.children[a]].towerweight)
                weightcounter = collections.Counter(weightlist)
                #print weightcounter
                try:
                    anomalyweight = weightcounter.keys()[weightcounter.values().index(1)]
                except ValueError:
                    return self.name
            for a in range(0,len(self.children)):
                if disc_dict[self.children[a]].towerweight == anomalyweight:
                    return disc_dict[self.children[a]].name
                else:
                    return self.name

    def towerweightcascade(self):
        weightadd = int(self.weight)
        n = self.name
        while disc_dict[n].parent != '':
            x = disc_dict[n].parent
            disc_dict[x].towerweight += int(weightadd)
            n = x

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

#print "7a: " + str(bottomdisc)

#7b solution

nochildren = []

#print parentlist

#first, get the starting "tower weight" for all of the items.
#it's equivalent to the weight.
#at the same time, add the parents of the discs w/o children to a list: parentlist.
for i in range(0,len(disc_names)):
    if len(disc_dict[disc_names[i]].children) == 0:
        nochildren.append(disc_names[i])

#print nochildren

for i in range(0,len(nochildren)):
    disc_dict[nochildren[i]].towerweightcascade()

for i in range(0,len(disc_dict[bottomdisc].children)):
    print disc_dict[disc_dict[bottomdisc].children[i]].discfacts()

#last part: find the anomaly
#anomaly = bottomdisc
#anomalylist = []

#while True:
    #anomaly = disc_dict[anomaly].findanomaly()
    #print disc_dict[anomaly].discfacts()
    #if anomaly not in anomalylist:
        #anomalylist.append(anomaly)
    #else:
        #break

#print parentlist
#print anomalylist

#breakpoint = anomalylist[len(anomalylist)-2]

#next, a recursive while loop to get the tower weight. we expand parentlist over time.
#we need to do this to make sure we get the towerweight in the right order.
#while i < len(parentlist):
    #disc_dict[parentlist[i]].gettowerweight()
    #disc_dict[parentlist[i]].towerweight += disc_dict[parentlist[i]].weight
    #if disc_dict[parentlist[i]].parent not in parentlist and disc_dict[parentlist[i]].name != bottomdisc:
        #parentlist.append(disc_dict[parentlist[i]].parent)
    #i += 1

#first, get the starting "tower weight" for all of the items.
#it's equivalent to the weight.
#at the same time, add the parents of the discs w/o children to a list: parentlist.
#for i in range(0,len(disc_names)):
    #print disc_dict[disc_names[i]].name
    #print disc_dict[disc_names[i]].children
    #print len(disc_dict[disc_names[i]].children)
    #if len(disc_dict[disc_names[i]].children) == 0:
        #nochildren.append(disc_names[i])
        #disc_dict[disc_names[i]].towerweight += disc_dict[disc_names[i]].weight
        #if disc_dict[disc_names[i]].parent not in parentlist: #and disc_dict[disc_names[i]].parent != ':
            #nochildren.append(disc_dict[disc_names[i]].parent)
