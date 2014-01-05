import trans as Trans
import mono as Mono
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
path= '../plaintext/plaintext4_c.txt'
fr = open(path, 'r')
ciphertext= ''.join(c for c in fr.read() if c.isalpha())
fr.close()
#print ciphertext
#write file
fw = open('result_mix3.txt', 'w+')

# prime then trans
decrypter= Decrypter(ciphertext)
#for x in [3,5,7,9,11,15,17,19,21,23,25]:
#	for winsize in xrange(70,90):
#		decrypter.reset()

#for word in zletters:
word= 'zero'
charHash= tablegen(word)
print len(charHash)
#print charHash
decrypter.mapping(charHash)
fw.write(decrypter.plaintext)
'''
for winsize in xrange(3,151):
	decrypter.mapping(charHash).trans(winsize)
	#if meanSth(decrypter.plaintext[:100]):
	fw.write(decrypter.plaintext[:100])
	fw.write('\n')
fw.close()


for x in [1,2,4,6,7,8,9,13,15,16,18,20,23]:
	decrypter.reset()
	decrypter.ceasar(x)
	print "shift: {0}, j: {1}, q: {2}, x: {3}, z: {4}, e: {5}".format(
		x,
		decrypter.plaintext.count('j'),
		decrypter.plaintext.count('q'),
		decrypter.plaintext.count('x'),
		decrypter.plaintext.count('z'),
		decrypter.plaintext.count('e')
	)

for x in [1,2,4,6,7,8,9,13,15,16,18,20,23]:
	for winsize in xrange(90,101):
		decrypter.reset()
		decrypter.trans(winsize).ceasar(x)

		#print decrypter.plaintext[:50]
		fw.write('ceasar: {0}, size: {1}- {2}\n'.format(x,winsize,decrypter))
		#fw.write(decrypter.plaintext)
'''


'''
freq= Counter()
for ch in ascii_lowercase:
	freq[ch] += decrypter.plaintext.count(ch)

common= 'etaoinshrdlcumwfgypbvkjxqz'

#charHash -> decode table
for item,fch in izip(freq.most_common(), common):
	ch= item[0][0]
	charHash[ch]= fch
print OrderedDict(sorted(charHash.items(), key=lambda t: t[1]))
'''

#for com in permutations('ABCD', 4):
#	print com
