from string import ascii_lowercase
from itertools import cycle

'''
poly
	circle minus keyword to ciphertext
'''
def code(char):
	if not char.isalpha():
		return char
	else:
		return ord(char)-96

def char(code):
	if not isinstance( code, int ):
		return code
	else:
		return chr(code+96)

def encode(codes):
	string= ''
	for code in codes:
		string += char(code)
	return string

# add key to plaintext
def minus(key_codes, p_codes):
	for key, plain in zip(cycle(key_codes), p_codes):
		num= (plain-key) % 26
		if num == 0:
			yield 26
		else:
			yield num

class Poly(object):
	"""poly decrypt"""
	def __init__(self, ciphertext, key):
		self.ciphertext = ciphertext
		self.key= key;

	def decode(self):
		# transter key, plaintext to codes
		key_codes= [code(x) for x in self.key]
		p_codes= [code(x) for x in self.ciphertext if x.isalpha()]

		# cipher codes
		c_codes= [x for x in minus(key_codes, p_codes)]
		return encode(c_codes)

		

'''
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
'''
