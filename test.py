import classical_ciphers as cc

# prime then trans
en= cc.Encrypter('ilovepythonjustlikeilovemymom')
print en.poly('snakekesn').trans(4)

de= cc.Decrypter('bjsvwerxzitdlcrpmgypwaguxenpp')
print de.trans(4).poly('snakekesn')
