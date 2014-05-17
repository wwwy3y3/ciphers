import classical_ciphers as cc

# prime then trans
decrypter= cc.Decrypter('fsferxoupqxdilsmzbvj')
encrypter= cc.Encrypter('abcdef123')
#decrypter.keyword('zero').trans(67)
decrypter.poly('snakekesn')
encrypter.trans(3).poly('snakekesn')
print decrypter.output()
print encrypter.output()