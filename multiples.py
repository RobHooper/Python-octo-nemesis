#!/usr/bin/python2.7

Y = 0
for X in range(1,1000):
	if X%3 == 0 or X%5 ==0:
		Y = Y + X
		print X
print Y
