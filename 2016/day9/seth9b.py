input_filepath = 'input.txt'
input1 = open(input_filepath, 'r')
content = input1.read()

content = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN' #so 8

print content, len(content)

def decompressor(string): #this function tracks the multiplier and the length, and calls itself as it needs to
	print '\n', 'starting decompressor with string', string
	multiplier = 1
	length = 0
	start = -1
	stop = -1
	last_stop = -1
	replicator_length = 0
	for i in range(0,len(string)):
		print 'cursor at', i
		if string[i] == '(' and i > last_stop + len(string[stop + 1: stop + replicator_length + 1]):
			print 'start at', i
			start = i
		if string[i] == ')' and i > last_stop + len(string[stop + 1: stop + replicator_length + 1]):
			print 'stop at', i
			stop = i
		if start > -1 and stop > -1 and i > last_stop + len(string[stop + 1: stop + replicator_length + 1]):
			print 'starting replicator'
			last_stop = stop #adjusts the position of the cursor
			last_start = start
			replicator = string[start + 1:stop] #contents of the replicator
			print replicator #show what the contents are
			replicator = replicator.split('x') #split the contents around x
			print 'replicator is', replicator #show your work
			multiplier *= int(replicator[1]) #define the multiplier
			print 'multiplier is', multiplier 
			replicator_length = int(replicator[0]) #define what you're multiplying
			print 'replicating segment is', string[stop + 1: stop + replicator_length + 1]
			if '(' in string[stop + 1: stop + replicator_length + 1]: #check to see if the replicator string has another replicator
				print 'new replicator found, restarting decompressor'
				length += decompressor(string[stop + 1: stop + replicator_length + 1]) #adds the result of (len * mul) to the length
			else:
				print 'no new replicator found, adding string', string[stop + 1: stop + replicator_length + 1], 'with length of', len(string[stop + 1: stop + replicator_length + 1])
				length += len(string[stop + 1: stop + replicator_length + 1])
			stop = -1
			start = -1
	total_length = 0
	print 'head of length', string[:last_start], 'with length', len(string[:last_start]), 
	print 'length is', length, 'multiplier is', multiplier, 'so', (length * multiplier)
	print 'tail of', string[last_stop + replicator_length + 1:], 'with length', len(string[last_stop + replicator_length + 1:]) 
	total_length = len(string[:last_start]) + length * multiplier + len(string[last_stop + replicator_length + 1:])
	print 'returning all for', len(string[:last_start]) + length * multiplier + len(string[last_stop + replicator_length + 1:])
	print 'decompression complete', '\n'
	return total_length

print decompressor(content)

#add every character to the length, add to the multiplier, then pass the rest of the string back to itself