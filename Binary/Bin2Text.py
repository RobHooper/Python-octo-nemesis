#!/usr/bin/python3

file = open('paris.jpg','rb')
output = open('paris.txt','w')

for line in file:
	output.write(str(line))
