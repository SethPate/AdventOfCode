import hashlib
from sys import stdout

input_file = 'ffykfhsq'

password = ['*','*','*','*','*','*','*','*']

hash_holder = ''

integer_counter = 0

position = 0

print 'Decrypting...'

#print password

while '*' in password:
	hash_holder = hashlib.md5(input_file + str(integer_counter)).hexdigest()
	if hash_holder[:5] == '00000':
		#print 'interesting hash, seth', hash_holder
		if hash_holder[5].isdigit() == True:
		#	print 'the positional digit is', hash_holder[5]
			if int(hash_holder[5]) in range(0,8):
		#		print 'the positional digit is in range'
				if password[int(hash_holder[5])] == '*':
		#			print 'so i will fill the position with', hash_holder[6]
					password[int(hash_holder[5])] = hash_holder[6]
		#			print password
					stdout.write("\r" + ''.join(password))
					stdout.flush()
					integer_counter += 1
				else:
		#			print 'but the position is already full'
					integer_counter += 1
			else:
		#		print 'but the positional digit is NOT in range'
				integer_counter += 1
		else:
		#	print 'but the positional character is NOT a digit'
			integer_counter += 1
	else:
		integer_counter += 1

print '\n', 'Decryption complete, Seth.'