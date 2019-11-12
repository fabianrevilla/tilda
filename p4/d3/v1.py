def makechildren(word):

for i in range(97,123):#byter tredje bokstaven
    s=word[0:2]
    s=s+chr(i)

for i in range(97,123):#byter mittersta bokstaven
    s1=word[0]
    s2=word[2]
    s=s1+chr(i)+s2


for i in range(97,123):#byter tredje bokstaven
    s=word[0:2]
    s=s+chr(i)

