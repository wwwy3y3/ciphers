import decrypt as decrypt
import encrypt as encrypt

# read file
path= './plaintext/plaintext4_c.txt'
fr = open(path, 'r')
ciphertext= ''.join(c for c in fr.read() if c.isalpha())
fr.close()
#print ciphertext
#write file
fw = open('test2.txt', 'w+')

# prime then trans
decrypter= decrypt.Decrypter('fsferxoupqxdilsmzbvj')
encrypter= encrypt.Encrypter('abcdef123')
#decrypter.keyword('zero').trans(67)
decrypter.poly('snakekesn')
encrypter.trans(3)
print decrypter.output()
print encrypter.output()