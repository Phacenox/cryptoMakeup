import math
import sys
import binascii
import time
import random
import os


#format: Miller-Rabin.py <input> <accuracy>

factors = []

if(len(sys.argv) < 2):
	print "format: Pollard-Rho.py <input>"
	quit()

inp = int(sys.argv[1])

while(True):
	x = 2
	y = 2
	d = 1
	while d == 1:
		x = (pow(x, 2, inp) + 1) % inp
		y = (pow(y, 2, inp) + 1) % inp
		y = (pow(y, 2, inp) + 1) % inp
		a = abs(x-y)
		b = inp
		while b != 0:
			tmp = a
			a = b
			b = tmp % b
		d = a
	if a == inp:
		print "failed to find a divisor"
		factors.append(int(inp))
		factors.sort()
		print "Prime factorization: " + str(factors)
		quit()
	print "Found factor " + str(d)
	factors.append(int(d))

	inp = inp/d
	print "n is now " + str(inp)









