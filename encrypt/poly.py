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

# read plaintext and key form file
#f= open('../text2', 'r')
plaintext= 'meet me at elephant lake'.lower()
key= 'snakeke'

# transter key, plaintext to codes
key_codes= [code(x) for x in uniqueStr(key)]
p_codes= [code(x) for x in plaintext if x.isalpha()]


# cipher codes
c_codes= [x for x in addUp(key_codes, p_codes)]
print c_codes
# traster plaintext code back to ciphertext 
cipherText= encode(c_codes)
print cipherText
