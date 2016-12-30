#dansolution14b

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

hash_dict = {}

for m in range(0,31001):
	#hashme = "abc" + str(m)
	hashme = "ahsbgdzn" + str(m)
	hashedstring = hashish(hashme)
	for y in range(0,2016):
		hashedstring = hashish(hashedstring)
	hash_dict[hashme] = hashedstring
	if m == 7500:
		print "DICT is 25% complete"
	if m == 15000:
		print "DICT is 50% complete"
	if m == 22500:
		print "DICT is 75% complete"
	if m == 29999:
		print "DICT is complete."

n = 0

while len(onetimepads) < 64:
	hashme = "ahsbgdzn" + str(n)
	x = 0
	if threestraight(hash_dict[hashme]) != "NOPE":
		hitme = threestraight(hash_dict[hashme])
		fiver = str(hitme) + str(hitme[0:2])
		j = n
		for j in range(j+1,j+1001):
			hashme2 = "ahsbgdzn" + str(j)
			hashedstring2 = hash_dict[hashme2]
			if x != 1:
				if fiver in hashedstring2:
					if hashme not in onetimepads:
						onetimepads.append(hashme)
						x = 1
	n += 1

print onetimepads[63][8:]
