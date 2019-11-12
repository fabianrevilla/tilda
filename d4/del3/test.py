from order import songdata
import timeit
from quicksort2 import quicksort
from binarysearch import binary_search
import sys

N=int(sys.argv[1])
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
        d[låt.artistnamn]=låt

        count=count+1
        if count>m:
            break
    return v,d
v,d=readfile("unique_tracks.txt",N)
v2=v
a=['dsfd','sdfsd','shmkig']
a1=[47,7,9,0,6,4,6,6,435,8,0,23]

# Linjärsökning osorterad lista
def linsok(lista, artistnamn):
    i=0
    while lista[i].artistnamn!=artistnamn:
        i=i+1
    return i

# Linjärsökning osorterad lista
t1=timeit.timeit(stmt = lambda: linsok(v,"John Williams"), number = N)
#print("Linjärsökningen osorterad lista tog", round(1, 4) , "sekunder")

# Linjärsökning sorterad lista
quicksort(v)
t2=timeit.timeit(stmt = lambda: linsok(v2,"John Williams"), number = N)
#print("Linjärsökningen i sorterad lista tog", round(t, 4) , "sekunder")

# Quicksort 
t3=timeit.timeit(stmt = lambda: quicksort(v2), number = N)
#print("Sortering av en lista tog", round(t, 4) , "sekunder")

# Binärsökning
ind=binary_search(v,"Hall Of Fame")
t4=timeit.timeit(stmt = lambda: binary_search(v,"Hall Of Fame"), number = N)
#print("Binärsökningen i sorterad lista tog", round(t, 4) , "sekunder")

#Slår upp element med Pythons dictionary
t5=timeit.timeit(stmt = lambda: d["John Williams"], number = N)
#print("Uppslag i en dictionary tog", round(t5, 6) , "sekunder")

print(N)
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(v[ind].artistnamn)
