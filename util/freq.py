from collections import Counter
from string import ascii_lowercase

class Decrypter(object):
	"""Decrypter"""
	def __init__(self, ciphertext):
		self.ciphertext= ciphertext
		self.plaintext= ciphertext

	def reset(self):
		self.plaintext= self.ciphertext

	def trans(self, winsize):
		cols= Trans.Columns(winsize, len(self.plaintext))
		for char in self.plaintext:
			cols.append(char)
		self.plaintext= cols.getplain()
		return self

	def prime(self, k):
		mono= Mono.Mono(self.plaintext)
		mono.prime(k)
		self.plaintext= mono.plaintext
		return self

	def ceasar(self, shift):
		mono= Mono.Mono(self.plaintext)
		mono.ceasar(shift)
		self.plaintext= mono.plaintext
		return self

	def mapping(self, hashing):
		string= ''
		for ch in self.plaintext:
			string += hashing[ch]
		self.plaintext= string
		return self

	def __repr__(self):
		return self.plaintext[:50]

# read file
path= '../decrypt/result_mix3.txt'
fr = open(path, 'r')
ciphertext= ''.join(c for c in fr.read() if c.isalpha())
fr.close()

decrypter= Decrypter(ciphertext)
freq= Counter()
for ch in ascii_lowercase:
	freq[ch] += decrypter.plaintext.count(ch)

print freq