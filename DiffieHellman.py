#!/usr/bin/python2.7

#Alice and Bob agree to use a prime number p = 23 and base g = 5 (which is a primitive root modulo 23).
## Prime number
P = 24
## Base
G = 50

#Alice chooses a secret integer a = 6,
A = input('Your secret number: ')
#then sends Bob A = ga mod p

print "Send this to freind:", G**A%P

#Bob chooses a secret integer b = 15, then sends Alice B = gb mod p
B = input ('Enter the number they sent you: ')

#Alice computes s = Ba mod p
#  Bob computes s = Ab mod p

print "This is your shared secret key: ", B**A%P

#Alice and Bob now share a secret (the number 2).
