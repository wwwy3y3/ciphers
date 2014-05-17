from string import ascii_lowercase
from itertools import izip

# three ways- 
#	ceasar
#	keyword
#	prime

def code(char):
	if not char.isalpha():
		return char
	else:
		return ord(char)-97

def char(code):
	if not isinstance( code, int ):
		return code
	else:
		return chr(code+97)

def rshift(char, shift):
	newcode= code(char)+shift
	if newcode >=26:
		newcode= newcode %26
	return newcode

def uniqueStr(key):
	uniqueKey= ''
	for ch in key:
		if ch not in uniqueKey:
			uniqueKey += ch
	return uniqueKey

def reverseTablegen(key):
	# unique key
	uniqueKey= uniqueStr(key)

	# make mapping string
	for ch in ascii_lowercase:
		if ch not in uniqueKey:
			uniqueKey += ch
	#print uniqueKey

	# make table
	table= {}
	for item,key in izip(ascii_lowercase, uniqueKey):
		table[item]= key
	return table

class  Mono(object):
	"""Monoalphabetic decryptor"""
	def __init__(self,plaintext):
		self.plaintext= plaintext

	def ceasar(self, shift):
		shift= shift%26
		self.ciphertext= ''
		for ch in self.plaintext:
			newcode= rshift(ch, shift)
			self.ciphertext += char(newcode)

	def mapping(self, hashing):
		self.ciphertext= ''
		for ch in self.plaintext:
			self.ciphertext += hashing[ch]

	def keyword(self, keyword):
		self.mapping(reverseTablegen(keyword))
			
if __name__ == '__main__':
	mono= Mono('abc')
	mono.ceasar(29)
	print mono.ciphertext

	mono= Mono('abcdef')
	mono.keyword('xyzxyz')
	print mono.ciphertext


