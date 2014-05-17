import string
from pprint import pprint
import math

class Columns(object):
	"""Columns"""
	def __init__(self, size, textLen):
		self.result= []
		self.winsize= size
		self.fullLines= textLen%self.winsize # full char lines
		self.charPerLine= math.ceil(float(textLen)/float(size))
		self.result.append('')		

	def append(self, char):
		if not char.isalpha():
			return

		result= self.result
		now= len(result)-1
		if len(result[now]) < self.winsize:
			result[now] += char
		else:
			result.append('')
			result[len(result)-1]+= char

	def getplain(self):
		string= ''
		for line in xrange(0,int(self.winsize)):
			string += ''.join(string[line] for string in self.result if len(string)>line)
		
		return string

	def __repr__(self):
		return self.getplain()

if __name__ == "__main__":
	# read file
	'''
	abcdefghijk
	abc
	def
	ghi
	jk

	adgjbenkcfi
	adg
	jbe
	nkc
	fi
	'''
	plaintext= 'abc def ghi jkl mon p'
	#plaintext= 'dttfsehwttfeahleeleenalcxdsoax'
	#plaintext= 'dauoisorrdegegfnsoord'
	# put in matrix
	#for winsize in xrange(60,70):
	winsize= 3
	cols= Columns(winsize, len(plaintext))
	for char in plaintext:
		cols.append(char)
		# print first line
	pprint(cols.result)
	pprint(cols)