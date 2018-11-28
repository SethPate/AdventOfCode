def stringClean(list):
#takes a string and returns a list of only the integers in the string

    result = []
    for i in list:
        try:
            result.append(int(i))
        except ValueError:
            print("skipping one non integer")
            
    return result

f = open('day1inputseth.txt', 'r')
data = f.read()

data = stringClean(data)

print(data)

answer = 0

dataCopy = data.copy()

for number in data:
    dataCopy.append(number)

lengthAhead = len(data) // 2
print(lengthAhead)

for number in range(len(data)):
    print(data[number],dataCopy[number+lengthAhead])
    if data[number] == dataCopy[number+lengthAhead]:
        print('same!')
        answer += data[number]
    
print(answer)