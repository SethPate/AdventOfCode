content = open('input.txt').read().strip()

def dekompressor(s):
	if '(' not in s: #if you don't find the open parentheses,
		return len(s) #just give me the length of the string itself
	length = 0 #this is a placeholder that we're going to add onto, keeping the length of each string
	while '(' in s: #for so long as the open parentheses is in the string, we're going to run the dekompressor to work out the kinks
		length += s.find('(') #find the first instance of the open parentheses in the string, and add its index to the length, accounting for any characters before the marker
		s = s[s.find('('):]	#redefines the string so as to truncate everything before the (
		replicator = s[1:s.find(')')].split('x') #a quick way of making a list 'replicator' consisting of everything after the paren and before the close paren, split on 'x'
		s = s[s.find(')') + 1:] #redefines the string so as to truncate the marker
		length += dekompressor(s[:int(replicator[0])]) * int(replicator[1])
		#the above line adds to the overall length tally, the result of running this function again on replicated section of string
		#and then multiplying that result by the replicator multiplier
		s = s[int(replicator[0]):] #redefines the string so as to truncate the replicated function
	length += len(s) #adds the rest of the string to the length
	return length

print dekompressor(content)