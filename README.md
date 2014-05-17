# goal
help you learn Classical cipher more efficient

NOTICE it's not for production!!

# install
``` python
sudo pip install classical_ciphers
```

# quick example
``` python
import classical_ciphers as cc
encrypter= cc.Encrypter('abcdef')

# chain of encryption
# do transposition in three window size and then ceasar cipher shift 4 chars
print encrypter.trans(3).ceasar(4)


# encrypt example2
en= cc.Encrypter('ilovepythonjustlikeilovemymom')
print en.poly('snakekesn').trans(4) # output 'bjsvwerxzitdlcrpmgypwaguxenpp'

# decrypt what we just encrypt!!
de= cc.Decrypter('bjsvwerxzitdlcrpmgypwaguxenpp')
print de.trans(4).poly('snakekesn') #output 'ilovepythonjustlikeilovemymom'
```

# api overview
*	encrypter
	*	monoalphabetic
		*	ceasar cipher
		*	keyword cipher
	*	polyalphabetic
	*	transposition
*	decrypter
	*	monoalphabetic
		*	ceasar cipher
		*	keyword cipher
	*	polyalphabetic
	*	transposition

# api usage
## import
``` python
import classical_ciphers as cc
```
##	.encrypter(iteratable text)
**@args** iteratable text string

give encrypter plaintext first
``` python
encrypter= cc.Encrypter('abcdef')
```

###	start encrypt!!
NOTICE the encryption process is a chain, 

so the result of last encryption will be cached

unless you reset by doing:
``` python
encrypter.reset()
```

### monoalphabetic
there are two apis for monoalphabetic- ceasar cipher and keyword cipher
#### .ceasar(shift)
**@args** integer shift

how many char alphabets shift
``` python
encrypter.reset().ceasar(3)
```
#### .keyword(keyword)
**@args** string keyword
``` python
encrypter.reset().keyword('snake')
```


### polyalphabetic
```
encrypter.reset().poly('keyword')
```

### transposition
#### .trans(windowSize)
**@args**  window size integer
```
encrypter.reset().trans(3)
```

# .Decrypter(iteratable text)
## apis are as same as `Encrypter` above, only difference is it's doing decryption

# licence
MIT