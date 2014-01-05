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

def lshift(char, shift):
	newcode= code(char)-shift
	if newcode<0:
		newcode= 26 + newcode
	return newcode

class  Mono(object):
	"""Monoalphabetic decryptor"""
	def __init__(self,ciphertext):
		self.ciphertext= ciphertext

	def ceasar(self, shift):
		shift= shift%26
		self.plaintext= ''
		for ch in self.ciphertext:
			newcode= lshift(ch, shift)
			self.plaintext += char(newcode)

	def prime(self, k):
		self.plaintext= ''
		for ch in self.ciphertext:
			newcode= (code(ch)*k)%26
			self.plaintext += char(newcode)
			
if __name__ == "__main__":
	path= '../plaintext/plaintext3_c.txt'
	f = open(path, 'r')
	ciphertext= ''.join(c for c in f.read() if c.isalpha())
	#plaintext= 'abcd'
	# mono
	mono= Mono(ciphertext)
	#for x in [3,5,7,9,11,15,17,19,21,23,25]:
		#mono.prime(x)
		#print mono.plaintext

	# answer= 11
	mono.prime(11)
	print mono.plaintext


