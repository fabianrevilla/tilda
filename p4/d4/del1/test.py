from order import songdata
from quicksort import quicksort
from binarysearch import binary_search

def readfile(filename):
    f=open(filename,"r")
    count=1
    v=[]
    d={}	
    for r in f:
        s=r.split("<SEP>")
        #print("s = ",s)
        #print("namn = ",namn)
        låt=songdata(s[0],s[1],s[2],s[3])
        v.append(låt)
        d[låt.artistnamn]=låt
        #print("artistnamn = ",låt.artistnamn)
        count=count+1
        if count>100:
            break
    return v,d
v,d=readfile("unique_tracks.txt")
n = len(v)
sista = v[n-4]
testartistnamn = sista.artistnamn
print("testartistnamn = ",testartistnamn)
quicksort(v)
print(v[0].artistnamn)
print(v[1].artistnamn)
print(v[2].artistnamn)
print(v[99].artistnamn)
x=binary_search(v,testartistnamn)

print("x = ",v[x].artistnamn)
