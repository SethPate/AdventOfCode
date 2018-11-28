import hashlib

input_file = 'ffykfhsq'

password = ''

hash_holder = ''

integer_counter = 0

while len(password) < 8:
	hash_holder = hashlib.md5(input_file + str(integer_counter)).hexdigest()
	if hash_holder[:5] == '00000':
		password += hash_holder[5]
		print password
		integer_counter += 1
	else:
		integer_counter += 1

print password

