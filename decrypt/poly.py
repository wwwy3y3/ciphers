from collections import Counter
from itertools import islice
		
path= '../plaintext/test_poly.txt'
f = open(path, 'r')
ciphertext= ''.join(c for c in f.read() if c.isalpha()).lower()

# most common repeat word
#keylen= [9,3,6,18,2]
keylen= [5]
key= ''
for key in keylen:
	#Do a frequency count on the ciphertext, on every nth letter
	for shift in xrange(1,key+1):
		freq= Counter()
		for ch in islice(ciphertext,0,None,shift):
			freq[ch] += 1
		char= freq.most_common()
		#print freq.most_common()[-1]

