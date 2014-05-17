## goal
help you learn Classical cipher more efficient

NOTICE it's not for production!!

## install
```
sudo pip install classical_ciphers
```

## api overview
*	encrypter
	*	monoalphabetic
	*	polyalphabetic
	*	transposition
*	decrypter
	*	monoalphabetic
	*	polyalphabetic
	*	transposition

## api usage
### import
```
import classical_ciphers as cc
```
###	encrypter
give encrypter plaintext first
```
encrypter= cc.Encrypter('abcdef')
```
####	start encrypt!!
NOTICE the encryption process is a chain, 

so the result of last encryption will be cached

unless you reset by:
```
decrypter.reset
```