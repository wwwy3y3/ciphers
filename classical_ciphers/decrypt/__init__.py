import trans as Trans
import mono as Mono
import poly as Poly
from string import ascii_lowercase
from collections import Counter,OrderedDict
from itertools import izip,permutations
from pprint import pprint

def uniqueStr(key):
	uniqueKey= ''
	for ch in key:
		if ch not in uniqueKey:
			uniqueKey += ch
	return uniqueKey

def validate(letter):
	uniqueKey= uniqueStr(letter)
	valid= True
	length= len(uniqueKey)
	if length >= 5 and not uniqueKey[4]=='a': # letter longer than 5, 5th ele must be 'a'
		valid= False
	elif length < 5 and 'a' in uniqueKey: # letter shoter than 5, cannot have 'a'
		valid= False
	return valid

def tablegen(key):
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
		table[key]= item
	return table

def meanSth(plaintext):
	meaning= False
	aletters= ['a', 'e', 'i', 'o', 'u']
	for words in ['is','are','for','of','in','be','to','and','that','have' ]:
		if words in plaintext:
			meaning= True
	#if plaintext[0] not in aletters and plaintext[1] not in aletters:
	#	meaning= False
	return meaning

class Decrypter(object):
	"""Decrypter"""
	def __init__(self, ciphertext):
		self.ciphertext= ciphertext
		self.plaintext= ciphertext

	def reset(self):
		self.plaintext= self.ciphertext
		return self

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

	def keyword(self, keyword):
		mono= Mono.Mono(self.plaintext)
		mono.keyword(keyword)
		self.plaintext= mono.plaintext
		return self

	def mapping(self, hashing):
		string= ''
		for ch in self.plaintext:
			string += hashing[ch]
		self.plaintext= string
		return self

	def poly(self, key):
		poly= Poly.Poly(self.plaintext, uniqueStr(key));
		self.plaintext= poly.decode()
		return self

	def output(self):
		return self.plaintext

	def __repr__(self):
		return self.plaintext[:50]

