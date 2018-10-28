import math
import sys
import binascii
import time
import random
import os


#format: Miller-Rabin.py <input> <accuracy>

if(len(sys.argv) < 3 or int(sys.argv[1]) - int(sys.argv[2]) < 3):
	print "format: Miller-Rabin.py <input> <accuracy>"
	quit()


inp = int(sys.argv[1])
k = int(sys.argv[2])

order = range(2, inp - 1)
random.shuffle(order)

if(inp % 2 == 0):
	print str(inp) + " is obviously not prime, since is even."
	quit()

r = 0
d = inp-1
while(d % 2 == 0):
	d /= 2
	r += 1

for i in range(0, k):
	a = order[i]
	x = pow(a, d, inp)
	if x == 1 or x == inp-1:
		continue
	primeish = False
	for j in range(0, r):
		x = pow(x, 2, inp)
		if x == 1 or x == inp-1:
			primeish = True
			break;
	if primeish:
		continue
	print str(inp) + " was found to be composite at a = " + str(a) + "."
	quit()
print str(inp) + " is probably prime."









