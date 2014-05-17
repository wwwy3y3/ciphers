from string import ascii_lowercase
from itertools import cycle

def uniqueStr(key):
	uniqueKey= ''
	for ch in key:
		if ch not in uniqueKey:
			uniqueKey += ch
	return uniqueKey

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

# add key to plaintext
def addUp(key_codes, p_codes):
	for key, plain in zip(cycle(key_codes), p_codes):
		num= (key+plain) % 26
		if num == 0:
			yield 26
		else:
			yield num

def encode(codes):
	string= ''
	for code in codes:
		string += char(code)
	return string

class Poly(object):
	"""poly decrypt"""
	def __init__(self, plaintext, key):
		self.plaintext = plaintext
		self.key= key;

	def decode(self):
		# transter key, plaintext to codes
		key_codes= [code(x) for x in self.key]
		p_codes= [code(x) for x in self.plaintext if x.isalpha()]

		# cipher codes
		c_codes= [x for x in addUp(key_codes, p_codes)]
		return encode(c_codes)
