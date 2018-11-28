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



for number in range(len(data)-1):
#    print(data[number],data[number+1])
    if data[number] == data[number+1]:
#        print('same!')
        answer += data[number]

if data[len(data)-1] == data[0]:
    print('the end is the beginning!')
    answer += data[len(data)-1]
    
print(answer)