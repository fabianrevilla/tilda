import sys
from quicksort import quicksort
import timeit
k=100
m=int(sys.argv[1])
i=int(sys.argv[2])
class songdata:
	def __init__(self,artistid,artistnamn,sångtitel,låtlängd,år):
		self.artistid=artistid
		self.artistnamn=artistnamn
		self.sångtitel=sångtitel
		self.låtlängd=float(låtlängd)
		self.år=år

def __It__(self,other):
        if self.artistnamn==other.artistnamn:
            return True
        else:
            return False

def readfile2(filename,m):
    f=open(filename,"r")
    count=1
    v=[]
    d={}	
    for r in f:
        s=r.split("\t")
        s[4]=s[4].strip('\n')#tar bort '\n' från sista elementet
        låt=songdata(s[0],s[1],s[2],s[3],s[4])
        v.append(låt)
        count=count+1
        if count>m:
            break
    return v,d

def printList(v):
	for låt in v:
		print(låt.låtlängd)

def searchLongest(v,n):
	redan_hittad={}
	for k in range(n):#kör algoritmen n gånger för att hitta n:te längsta ordet
		longest=songdata('','','',0,'')#nollställer det längsta ordet
		for låt in v:#stegar igenom varje låtobjekt i listan
			if låt.låtlängd > longest.låtlängd and låt.sångtitel not in redan_hittad:#om den nuvarande låtlängden är längre än den längsta låtlängden
				longest=låt
			redan_hittad[longest.sångtitel]=longest.sångtitel#sparar den längsta låtlängden för varje n:te runda		
	return longest
			
v,d=readfile2("song_artist_data.txt",m)
#mäter tiden det tar att hitta det längsta låtlängdet
t1=timeit.timeit(stmt = lambda: searchLongest(v,i), number=k)/k
#mäter tiden det tar att sortera listan med quicksort
t2=timeit.timeit(stmt = lambda: quicksort(v), number = 3)/3

print("tid för att hitta %dnde längsta ordet med linjärsökning= %f s" % (i, t1))
print("tid för att sortera listan = %f s" % (t2))
#print("den %dde längsta låten= %d s" % (i, searchLongest(v,i).låtlängd))
#print("v[i] = ",v[i-1].låtlängd)
#printList(v)


