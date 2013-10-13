from string import ascii_lowercase
from collections import deque, OrderedDict

# read plaintext and key form file
f= open('text', 'r')
plaintext= f.readline().lower()
key= ''.join(OrderedDict.fromkeys(f.readline()).keys()) # unique the string


# init a fillList, from a-z
#fillList= map(chr, range(97, 123))

# init a table dict, keys from a-z
table= OrderedDict((el,0) for el in ascii_lowercase)

# concat key and alphabets
fillList= deque()
for char in key:
	fillList.append(char)

# delete chars from list
chars= []
for char in ascii_lowercase:
	if char not in key: # if char not appear in key
		chars.append(char)

# fill the chars
for char in chars:
	fillList.append(char)

# fill the table
for x in table:
	table[x]= fillList.popleft()

# encrypt the plaintext
# if char is alpha, then map the table, print it
# else just print it
pr= ''
for char in plaintext:
	if char.isalpha():
		pr+=table[char]
	else:
		pr+=char
print pr