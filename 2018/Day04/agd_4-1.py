datum = []
cloth = []
dup_cloth = []
with open("2018/Day04/agd_input4.txt", "r") as x:
    data = x.readlines()

for line in data:
    datum.append(line.split())

for x in range(len(data)):
    datum[x].append(datum[x][1].split(":")[0])
    datum[x].append(datum[x][1].split(":")[1].split("]")[0])

print(datum[43])
print(datum[22])
print(datum[431])
print(datum[366])
print(datum[127])
print(datum[4])
print("help")