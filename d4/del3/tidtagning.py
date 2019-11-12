from order import songdata
import timeit
from quicksort2 import quicksort
from binarysearch import binary_search
import sys

N=int(sys.argv[1])
k=100
#print("N = ",N)
def readfile(filename,m):
    f=open(filename,"r")
    count=1
    v=[]
    d={}	
    for r in f:
        s=r.split("<SEP>")
        låt=songdata(s[0],s[1],s[2],s[3])
        v.append(låt)
        d[låt.låttitel]=låt

        count=count+1
        if count>m:
            break
    return v,d
v,d=readfile("unique_tracks.txt",N)
v2=v
n = len(v)
sista = v[(n-1)]
testartistnamn = sista.artistnamn
testlåt = sista.låttitel

# Linjärsökning osorterad lista
def linsok(lista, låttitel):
    i=0
    while lista[i].låttitel != låttitel:
        i=i+1
    return i

# Linjärsökning i osorterad lista
t1=timeit.timeit(stmt = lambda: linsok(v,testlåt), number = k)/k
#print("Linjärsökningen osorterad lista tog", round(1, 4) , "sekunder")

# Linjärsökning i sorterad lista
quicksort(v)#sorterar listan
t2=timeit.timeit(stmt = lambda: linsok(v,testlåt), number = k)/k
#print("Linjärsökningen i sorterad lista tog", round(t, 4) , "sekunder")

# Quicksort 
t3=timeit.timeit(stmt = lambda: quicksort(v2), number = 3)/3
#print("Sortering av en lista tog", round(t, 4) , "sekunder")

# Binärsökning
indx = binary_search(v,testlåt)
print("v[indx].låttitel = ",v[indx].låttitel)
t4=timeit.timeit(stmt = lambda: binary_search(v,testlåt), number = k)/k
#print("Binärsökningen i sorterad lista tog", round(t, 4) , "sekunder")

#Slår upp element med Pythons dictionary
t5=timeit.timeit(stmt = lambda: d[testlåt], number = k)/k
#print("Uppslag i en dictionary tog", round(t5, 6) , "sekunder")

print(N)
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)

