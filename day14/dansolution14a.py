#dansolution14a

import md5

def hashish(a):
	hash1 = md5.new(a)
	return hash1.hexdigest()

def threestraight(a):
	b = 0
	c = "NOPE"
	for i in range(0,len(a)-1):
		if b == 0:
			if a[i:i+1] == a[i+1:i+2] and a[i+1:i+2] == a[i+2:i+3]:
				b = 1
				c = a[i:i+3]
	return c

hashcount = 0
onetimepads = []
n = 0
fiver = ""

#hashme = hashish("abc39")
#print hashme
#print threestraight(hashme)

while len(onetimepads) < 64:
	hashme = "ahsbgdzn" + str(n)
	hashedstring = hashish(hashme)
	x = 0
	if threestraight(hashedstring) != "NOPE":
		hitme = threestraight(hashedstring)
		fiver = str(hitme) + str(hitme[0:2])
		j = n
		for j in range(j+1,j+1001):
			hashme2 = "ahsbgdzn" + str(j)
			hashedstring = hashish(hashme2)
			if x != 1:
				if fiver in hashedstring:
					if hashme2 not in onetimepads:
						onetimepads.append(hashme)
						x = 1
	n += 1

print onetimepads[63][4:]
