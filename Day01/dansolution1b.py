#dansolution1b

input_file = 'day1inputdan.txt'
captchalist = []
captchasum = 0

def fileimport(input_file1):
	input1 = open(input_file1, 'r')
	input1 = input1.read()
	return input1

def listmaker(a):
    b = []
    for i in range(0,len(a)):
        if a[i].isdigit() == True:
            b.append(a[i])
    return b

def checker(a,b,c):
    if a[int(b)] == a[int(c)]:
        return a[b]
    else:
        return 0

def compcheck(a,b):
    if b > (.5 * len(a)) - 1:
        return b - (.5 * len(a))
    else:
        return b + (.5 * len(a))

captcha = fileimport(input_file)
captchalist = listmaker(captcha)

#print captchalist
#print len(captchalist)

for i in range(0,len(captchalist)-1):
    comparison = compcheck(captchalist,i)
    captchasum += int(checker(captchalist,i,comparison))

#1b solution
print captchasum

#if captchalist[len(captchalist)-1] == captchalist[0]:
    #captchasum += int(captchalist[0])

#1a solution
#print captchasum
