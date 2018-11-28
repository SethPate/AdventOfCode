#dansolution1a

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

def checker(a,b):
    if a[b] == a[b+1]:
        return a[b]
    else:
        return 0

captcha = fileimport(input_file)
captchalist = listmaker(captcha)

for i in range(0,len(captchalist)-2):
    captchasum += int(checker(captchalist,i))

if captchalist[len(captchalist)-1] == captchalist[0]:
    captchasum += int(captchalist[0])

#1a solution
print captchasum
