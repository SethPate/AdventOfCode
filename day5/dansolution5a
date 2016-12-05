#adventday5a

import md5

def hashish(a):
	hash1 = md5.new(a)
	return hash1.hexdigest()
	
def first5(a):
	return a[0:5]

i = 1
mystring = "wtnhxymk" + str(i)
cornedbeef = md5.new(mystring)

cornedbeefhash = hashish(mystring)
cornedbeefstring = first5(cornedbeefhash)

finalresult = ""

while len(finalresult) < 8:
	cornedbeefstring = "1"
	while cornedbeefstring != "00000":
		i = i + 1
		cornedbeefhash = hashish(mystring)
		cornedbeefstring = first5(cornedbeefhash)
		mystring = "wtnhxymk" + str(i)
		
	finalresult = str(finalresult) + str(cornedbeefhash[5:6])

print finalresult
