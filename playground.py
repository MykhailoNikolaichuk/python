
asd = 'a'
print('asd: ', ord(asd))
das = 'A'
print('das: ', ord(das))

def tolower(self,x):
        o = ord(x)
        return chr(o+32) if 64<o<91 else x