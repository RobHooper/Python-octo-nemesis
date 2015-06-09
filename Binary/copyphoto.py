#!/usr/bin/python2.7

# Copies input to output

buffersize = 100000
input = open('paris.jpg','rb')
output = open('paris-copy.jpg','wb')
buffer = input.read(buffersize)

while len(buffer):
	output.write(buffer)
	print '0'
	buffer = input.read(buffersize)
