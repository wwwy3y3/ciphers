from string import ascii_lowercase
from collections import deque

# read plaintext and key form file
f= open('text', 'r')
plaintext= f.readline().lower()
key= ''.join(set(f.readline())) # unique the string

# init a fillList, from a-z
#fillList= map(chr, range(97, 123))

# init a table dict, keys from a-z
table= dict((el,0) for el in ascii_lowercase)

# concat key and alphabets
fillList= deque()
for char in key:
	fillList.append(char)

for char in ascii_lowercase:
	fillList.append(char)

# fill the table
for x in table:
	table[x]= fillList.popleft()

# encrypt the plaintext
# if char is alpha, then map the table, print it
# else just print it
for char in plaintext:
	if char.isalpha():
		print table[char],
	else:
		print char,