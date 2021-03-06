datum = []
guard = "#999"
sleepmin = {}

### Read Data
with open("2018/Day04/agd_input4.txt", "r") as x:
    data = x.readlines()
for line in data:
    datum.append(line.split())

### Cleaning Up Data
for x in range(len(data)):
    datum[x].append(int(datum[x][0].split("-")[0].split("[")[1]))
    datum[x].append(int(datum[x][0].split("-")[1]))
    datum[x].append(int(datum[x][0].split("-")[2]))
    datum[x].pop(0)
    datum[x].append(int(datum[x][0].split(":")[0]))
    datum[x].append(int(datum[x][0].split(":")[1].split("]")[0]))
    datum[x].pop(0)
    if datum[x][0] == "Guard":
        for i in range(4):
            datum[x].append(datum[x][0])
            datum[x].pop(0)
    else:
        for i in range(2):
            datum[x].append(datum[x][0])
            datum[x].pop(0)
    datum[x].pop(0)

datum.sort()

for x in range(len(data)):
    if datum[x][2] != 0:    #set all times to start at midnight 00:00
        datum[x][2] = 0
        datum[x][3] = 0
    if datum[x][4] == "Guard":
        guard = int(datum[x][5].split("#")[1])
        datum[x].pop(4)
        datum[x].pop(4)
        datum[x].insert(0,guard)
    else:
        datum[x].insert(0,guard)
    # datum[x].pop(3)
    # datum[x].insert(1,int(datum[x][1].split("#")[1]))
    # datum[x].pop(2)
    # datum[x].pop(0)
    # datum[x].pop(2)
    # datum[x].append(datum[x][1])
    # datum[x].pop(1)
    #

datum.sort()

for x in range(len(data)):
    sleepmin[datum[x][0]] = 0

for x in range(len(data)):
    if datum[x][5] == "falls":
        sleepmin[datum[x][0]] += datum[x+1][4]-datum[x][4]

print(sleepmin)
maxmin = 0
maxguard = 0
for x in sleepmin:
    if sleepmin[x] > maxmin:
        maxmin = sleepmin[x]
        maxguard = x

print(maxmin)
print(maxguard)
minutes = []

for x in range(60):
    minutes.append(0)

for x in range(len(data)):
    if datum[x][0] == maxguard:
        if datum[x][5] == "falls":
            for i in range(datum[x+1][4]-datum[x][4]):
                minutes[datum[x][4]+i] += 1

check = 0
print(minutes)
for i in range(len(minutes)):
    if minutes[i] > check:
        check = minutes[i]
        print(i)



