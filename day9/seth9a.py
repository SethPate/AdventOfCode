input_file = open('input.txt', 'r')
content = input_file.read()
content = content.strip() #the content is just one long string

answer = '' #it's a (much longer) string, whose length is the answer

#content = '(1x2)AG(5x2)B(1x5)D'
repper = False #determines whether the repper section is running
placeholder = 0 #holds the position of the last content copied over

for i in range(0,len(content)): #for each character in this string,
	print '\n', 'function at position', i
	if content[i] == '(' and i >= placeholder: #first check if it's a parentheses
		replicator_start = i #if so, save this position
		print "repper start at", i
	if content[i] == ')' and i > placeholder: #then check if it's an ending parentheses
		replicator_end = i #if so, save this position
		print "repper end at", i
		repper = True
		print 'activating repper'
	if repper == True:
		print 'repper is now catching up by adding', content[placeholder:replicator_start]
		answer += content[placeholder:replicator_start]
		replicator = content[replicator_start + 1:replicator_end]
		replicator = replicator.split('x')
		print 'replicate', replicator[0], 'characters for', replicator[1], 'times'
		replicator_contents = content[replicator_end + 1:replicator_end + int(replicator[0]) + 1] #the contents reach from the character after the ), to the last character specified by the replicator
		print 'now adding', replicator_contents, 'to string for', replicator[1], 'times'
		for i in range(0,int(replicator[1])): #for as many times as specified by the replicator,
			answer += replicator_contents
		print 'deactivating repper'
		placeholder = replicator_end + int(replicator[0]) + 1 #shows what position the next repper should catch up from
		print 'placeholder is', placeholder
		repper = False

print 'program catching up after last replication by adding', content[placeholder:]
answer += content[placeholder:]

print '\n', 'compressed content is', content
print 'uncompressed content is', answer
print 'uncompressed content should be AAGB(1x5B(1x5D'

answer = answer.strip()

print 'length of uncompressed content is', len(answer) #this is my answer

#162713 is too high!
#162745 is too high!