from order import songdata
import timeit
from quicksort import quicksort
from binarysearch import binary_search
import sys

N=int(sys.argv[1])
m=100
def readfile(filename,m):
    f=open(filename,"r",encoding="UTF-8")
    count=1
    v=[]
    d={}	
    for r in f:
        s=r.split("<SEP>")
        låt=songdata(s[0],s[1],s[2],s[3])
        v.append(låt)
        d[låt.artistnamn]=låt

        count=count+1
        if count>m:
            break
    return v,d
v,d=readfile("unique_tracks.txt",N)
v2=v

# Linjärsökning osorterad lista
def linsok(lista, artistnamn):
    i=0
    while lista[i].artistnamn!=artistnamn:
        i=i+1
    return i

n = len(v)
sista = v[n-1]
testartistnamn = sista.artistnamn
print("För N =",N)
# Linjärsökning osorterad lista
t1=timeit.timeit(stmt = lambda: linsok(v,testartistnamn), number = m)/m
print("Linjärsökningen osorterad lista tog", round(t1, 4) , "sekunder")

# Quicksort 
t3=timeit.timeit(stmt = lambda: quicksort(v), number = 1)
print("Sortering av en lista tog", round(t3, 4) , "sekunder")

# Linjärsökning sorterad lista
t2=timeit.timeit(stmt = lambda: linsok(v,testartistnamn), number = m)/m
print("Linjärsökningen i sorterad lista tog", round(t2, 4) , "sekunder")

# Binärsökning
ind=binary_search(v,testartistnamn)
t4=timeit.timeit(stmt = lambda: binary_search(v2,testartistnamn), number = m)/m
print("Binärsökningen i sorterad lista tog", round(t4, 4) , "sekunder")

#Slår upp element med Pythons dictionary
t5=timeit.timeit(stmt = lambda: d[testartistnamn], number = m)/m
print("Uppslag i en dictionary tog", round(t5, 8), "sekunder")

