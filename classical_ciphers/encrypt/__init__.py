import mono as Mono
import poly as Poly
import trans as Trans
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

class Encrypter(object):
	"""Encrypter"""
	def __init__(self, text):
		self.ciphertext= text
		self.plaintext= text

	def reset(self):
		self.ciphertext= self.plaintext
		return self
		
	def trans(self, winsize):
		cols= Trans.Columns(winsize, len(self.ciphertext))
		for char in self.ciphertext:
			cols.append(char)
		self.ciphertext= cols.getplain()
		return self
		
	def ceasar(self, shift):
		mono= Mono.Mono(self.ciphertext)
		mono.ceasar(shift)
		self.ciphertext= mono.ciphertext
		return self

	def keyword(self, keyword):
		mono= Mono.Mono(self.ciphertext)
		mono.keyword(keyword)
		self.ciphertext= mono.ciphertext
		return self

	def mapping(self, hashing):
		string= ''
		for ch in self.ciphertext:
			string += hashing[ch]
		self.ciphertext= string
		return self

	def poly(self, key):
		poly= Poly.Poly(self.ciphertext, uniqueStr(key));
		self.ciphertext= poly.decode()
		return self

	def output(self):
		return self.ciphertext

	def __repr__(self):
		return self.ciphertext[:50]
		