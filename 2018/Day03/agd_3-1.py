datum = []
cloth = []
dup_cloth = []
with open("2018/Day03/agd_input3.txt", "r") as x:
    data = x.readlines()

for line in data:
    datum.append(line.split())

for x in range(len(data)):
    datum[x].append(int(datum[x][2].split(",")[0]))
    datum[x].append(datum[x][2].split(",")[1])
    datum[x].append(int(datum[x][5].split(":")[0]))
    datum[x].append(int(datum[x][3].split("x")[0]))
    datum[x].append(int(datum[x][3].split("x")[1]))
    datum[x].pop(1)
    datum[x].pop(1)
    datum[x].pop(1)
    datum[x].pop(2)

for x in range(1000):
    cloth.append([])
    dup_cloth.append([])
    for y in range(1000):
        dup_cloth[x].append(0)

for i in range(len(data)):
    for x in range(datum[i][3]):
        for y in range(datum[i][4]):
            cloth[datum[i][1]+x].append(datum[i][2]+y)

print(datum[43])
print(datum[43][2]+2)
for i in range(len(cloth)):
    cloth[i].sort()
print(cloth[466])
print(len(cloth))

for i in range(len(cloth)):
    for j in range(len(cloth[i])-1):
        if cloth[i][j] == cloth[i][j+1]:
            dup_cloth[i][cloth[i][j]] = 1

print(dup_cloth[0][0])
print(dup_cloth[466][251])

total_dups = 0

for x in range(len(dup_cloth)):
    for y in range(len(dup_cloth[x])):
        total_dups += dup_cloth[x][y]

print(total_dups)





