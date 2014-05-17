import classical_ciphers as cc

# prime then trans
decrypter= cc.Decrypter('fsferxoupqxdilsmzbvj')
encrypter= cc.Encrypter('abcdef')
#decrypter.keyword('zero').trans(67)
decrypter.poly('snakekesn')
print encrypter.trans(3)
print encrypter.reset().poly('snakekesn')
print encrypter.reset().trans(3).keyword('snakekesn')
print encrypter.reset().keyword('snakekesn').trans(3)