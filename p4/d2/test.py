from hashtabell import HashNode,HashTable
from hashf import hashf
låtlista=HashTable()
f = open("unique_tracks.txt","r")
count=0
for r in f:
    s=r.split("<SEP>")#splitar varje rad vid varje <SEP> markör
    artist=s[2]
    låt=s[3]
    låtlista.store(artist,låt)#artist blir nyckel, låt blir data
    count=count+1
    if count > 10:
        break


for i in låtlista.l:
    try:
        print(i.key)
    except AttributeError:
        print("None")
x=låtlista.search('Yerba Brava')
print("x = ",x)
