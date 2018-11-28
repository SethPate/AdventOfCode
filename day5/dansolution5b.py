#adventday5b

import md5

def hashish(a):
	hash1 = md5.new(a)
	return hash1.hexdigest()
	
def first5(a):
	return a[0:5]

def sixer(a):
	return a[5:6]

def finalcode(a):
	password = ""
	for j in range(0,8):	
		password = password + a[str(j)]
	return password

i = 0
mystring = "wtnhxymk" + str(i)
cornedbeef = md5.new(mystring)

cornedbeefhash = hashish(mystring)
cornedbeefstring = first5(cornedbeefhash)
cornedbeefsix = sixer(cornedbeefhash)
cornedbeefdictionary = {"0": "",
						"1": "",
						"2": "",
						"3": "",
						"4": "",
						"5": "",
						"6": "",
						"7": ""}
						
finalresult = ""
counter = 0
while counter < 8:
	cornedbeefstring = "1"
	while cornedbeefstring != "00000":
		i = i + 1
		cornedbeefhash = hashish(mystring)
		cornedbeefstring = first5(cornedbeefhash)
		cornedbeefsix = sixer(cornedbeefhash)
		mystring = "wtnhxymk" + str(i)
	
	if cornedbeefsix in cornedbeefdictionary:
		if cornedbeefdictionary[str(cornedbeefsix)] == "":
			cornedbeefdictionary[str(cornedbeefsix)] = str(cornedbeefhash[6:7])
			counter = counter + 1

print finalcode(cornedbeefdictionary)
