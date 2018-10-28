import math
import numpy as np
import sys
import binascii
import time
import random
import os
import hashlib

#load md5 hash algorithm
h = hashlib.md5()

print "We will attempt to find a hash collision for some wikepedia text, one that provides"
print "correct information and one that does not. For this example, we will use a 32 bit hash,"
print "so we should expect to find a collision within sqrt(2^32) = 2^16 unique correct texts"
print "and incorrect texts. This particular instance takes about 4 minutes on my mahcine,"
print "going through about a third of the options for the incorrect text."

random.seed()
goodfile = open('GoodText.txt', "r")
tmptext = goodfile.read();
goodfile.close()

#generate 2^16 pairs of correct text and their hash values
texts = []
hashValues = []
print ""
print "generating correct texts and hash values"
for i in range(0, int(math.pow(2,16))):
	index = 0


	goodtext = "";

	alltext = tmptext;
	for line in alltext.splitlines():
		if(line[0] == '{'):
			options = line.split(';')
			chosen = int(i/math.pow(2,index) % 2)
			if chosen == 0:
				goodtext += options[0][1:];
			else:
				goodtext += options[1][:-1];
			index += 1;
		else:
			goodtext += line[:-1] + " ";
	texts.append(goodtext)
	#hash function, I'm using md5 and compressing it into a 32 bit integer.
	h.update(goodtext);
	hashValues.append(int(h.hexdigest(), 16) % long(math.pow(2,32)))
	if (i+1)%6553 == 0:
		print str(i/655) + '%'

print ""
print "generating and testing incorrect texts"

badfile = open('BadText.txt', "r")
tmptext = badfile.read();
badfile.close()

#generate incorrect texts until we find a hash value match
for i in range(0, int(math.pow(2,16))):
	index = 0
	
	badtext = "";

	alltext = tmptext;
	for line in alltext.splitlines():
		if(line[0] == '{'):
			options = line.split(';')
			chosen = int(i/math.pow(2,index) % 2)
			if chosen == 0:
				badtext += options[0][1:];
			else:
				badtext += options[1][:-1];
			index += 1;
		else:
			badtext += line[:-1] + " ";
	#hash function
	h.update(badtext);
	found = False;
	hashval = int(h.hexdigest(), 16) % long(math.pow(2,32))
	for j in range(0, int(math.pow(2,16))):
		if(hashval == hashValues[j]):
			print "match found at: " + str(hashval)
			print "Correct text: "
			print texts[j]
			print "Incorrect text: "
			print badtext
			found = True
			break
	if(found):
		break
	if (i+1)%6553 == 0:
		print str(i/655) + '%'



		
		
		
		
		
		
		
