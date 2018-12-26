pline = []
test = []
dup = 0
copies = 0
trip = 0
totdup = 0
tottrip = 0
with open("2018/Day02/agd_input2.txt", "r") as x:
    data = x.readlines()

for line in data:
    pline.append(line.split())

for i in range(len(pline)):
    letters = list(str(pline[i]))
    letters.pop()
    letters.pop()
    letters.pop(0)
    letters.pop(0)
    letters.sort()

    for j in range(len(letters)):
        for k in range(j+1,len(letters)):
            if letters[k] != '0':
                if k+1 < len(letters):
                    if letters[k] == letters[j]:
                        if letters[k+1] == letters[j]:
                            trip = 1
                            letters[j] = '0'
                            letters[j+1] = '0'
                            letters[j+2] = '0'
                        else:
                            dup = 1
                            letters[j] = '0'
                            letters[j+1] = '0'
                elif k < len(letters):
                    if letters[k] == letters[j]:
                        dup = 1
                        letters[j] = '0'
                        letters[j+1] = '0'
        print(letters)
    totdup = totdup + dup
    tottrip = tottrip + trip
    dup = 0
    trip = 0
    print(totdup,tottrip,dup,trip)

print(totdup)
print(tottrip)
print(totdup*tottrip)