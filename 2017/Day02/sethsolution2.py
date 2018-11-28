def stringToList(s):
    #input: a string of integers delimited by \t
    #output: a list of integers in that string
    output = []
    s = s.split() #get rid of the whitespace
    for i in s: #now i've got a list of strings
        output.append(int(i)) #and i want to add the integer value of each string to my output
    return output

def getChecksum(l):
    #input: a list of integers
    #output: the difference of the highest and lowest digits in the list
    high = l[0]
    low = l[0]
    for i in l:
        if i > high:
            high = i
        if i < low:
            low = i
    print("checksum for this line is", high, "minus", low)
    return high - low

def getDividesEvenlySum(l):
    #input: a list of integers with only two values that divide evenly
    #output: sum of the two integers that divide evenly
    for i in l: #for every number in the list
        for j in l: #compare it to every other number in the list
            if i % j == 0 and i != j: #if it divides evenly with a number other than itself
                print(i, "divides evenly with", j)
                return i / j

f = open('sethday2input.txt', 'r')

table = [] #input: a table of values in a .txt

for line in f: #take every line in the .txt
    table.append(line) #and add it to the table as a string

checksum = 0 #output: the sum of differences between the highest and lowest values in each row of a table

dividesEvenlySum = 0 #output: the sum of division between the only two values in each row that divide evenly

for row in table:
    print("current checksum is", checksum)
    row = stringToList(row)
    checksum += getChecksum(row)
    dividesEvenlySum += getDividesEvenlySum(row)

print("checksum is", checksum)
print("sum of even divisions is", dividesEvenlySum)