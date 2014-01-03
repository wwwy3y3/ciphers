# iterate window size from 4-15
# read file
# truncate
# put in matrix and put blanks on
# read it!
import string
from pprint import pprint
import math

class Columns(object):
	"""Columns"""
	def __init__(self, size, textLen):
		self.result= []
		self.winsize= size
		self.fullLines= textLen%winsize # full char lines
		self.charPerLine= math.ceil(float(textLen)/float(size))
		self.result.append('')		

	def append(self, char):
		result= self.result
		now= len(result)-1
		if len(result[now]) < self.charPerLine:
			if len(result)>self.fullLines and len(result[now])+1 == self.charPerLine: # last N lines, need to add -
				result[now] += '-'
				result.append('')
				result[len(result)-1]+= char
			else:	
				result[now] += char
		else:
			result.append('')
			result[len(result)-1]+= char

	def __repr__(self):
		string= ''
		for line in xrange(0,int(self.charPerLine)):
			string += ''.join(string[line] for string in self.result if len(string)>line)
		
		return string[:50]
		# return repr(self.result)

# read file
path= '../plaintext/plaintext1_c.txt'
f = open(path, 'r')
plaintext= ''.join(c for c in f.read() if c.isalpha())
#plaintext= 'dttfsehwttfeahleeleenalcdsoa'
# put in matrix
for winsize in xrange(3,120):
	cols= Columns(winsize, len(plaintext))
	for char in plaintext:
		cols.append(char)
		# print first line
	pprint(cols)