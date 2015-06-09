#!/usr/bin/python2.7

# Memory location list

mem = [3,4,0,0,0,0,0]

##### Functions #####

# Zero memory location
# Z(3) - Zero mem[3]
def Z(loc):
	mem[loc] = 0

# Add one to the memory location
# I(3) - Add 1 to mem[3]
def I(loc):
	mem[loc] = mem[loc] + 1

# Are memory locations different
# J(2,3) - returns boolean if different
def J(loc,loc2):
	if mem[loc] != mem[loc2]:
		return False
	else:
		return True

##### End of functions #####

## Solution 1 ##
#
#Z(2)
#while J(2,0) == False:
#	I(2)
#
#
#Z(3)
#while J(3,1) == False:
#	I(3)
#	I(2)

## Solution 2 ##
#
Z(2)

while J(2,0) == False:
	I(2)
	I(1)

while J(2,1) == False:
	I(2)

## Solution 3 ##
#
#Z(2)
#while J(2,0) == False:
#	I(2)
#
#Z(0)
#while J(0,1) == False:
#	I(0)
#	I(2)

## Solution 4 ##
#Z(2)
#
#while J(2,0) == False:
#	I(1)
#	I(2)
#
#while J(2,1) == False:
#	I(2)

print mem



