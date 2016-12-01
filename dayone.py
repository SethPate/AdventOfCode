import sys

input_fullpath = sys.argv[1]

with open(input_fullpath, 'r') as f:
	a = f.readline()

a = a.replace(" ", "")

a = a.split(',')

print (a)