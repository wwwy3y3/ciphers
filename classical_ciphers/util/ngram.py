from collections import Counter

def ngrams(sequence, n, pad_left=False, pad_right=False, pad_symbol=None): 
	if pad_left: 
		sequence = chain((pad_symbol,) * (n-1), sequence) 
	if pad_right: 
		sequence = chain(sequence, (pad_symbol,) * (n-1)) 
	#sequence = list(sequence)     
	count = max(0, len(sequence) - n + 1) 
	return [sequence[i:i+n] for i in range(count)]

# read file
path= '../plaintext/plaintext4_c.txt'
fr = open(path, 'r')
ciphertext= ''.join(c for c in fr.read() if c.isalpha())
fr.close()

# count ngrams counter
tri_freq= Counter()
bi_freq= Counter()

# bigrams
for string in ngrams(ciphertext,2):
	bi_freq[string] += 1

#trigrams
for string in ngrams(ciphertext,3):
	tri_freq[string] += 1
	
print bi_freq.most_common(50)
print tri_freq.most_common(50)