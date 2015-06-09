#!/usr/bin/python2.7

file = open('paris.txt','r+b')
output = open('paris-copy.jpg','w+b')

for line in file:
	output.write(str(line))

