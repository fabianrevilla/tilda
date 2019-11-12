
class songdata:
    def __init__(self,trackid,låtid,artistnamn,låttitel):
        self.trackid=trackid
        self.låtid=låtid
        self.artistnamn=artistnamn
        self.låttitel=låttitel

    def __lt__(self,other):
        if self.artistnamn > other.artistnamn:
            return True
        else:
            return False
f=open("unique_tracks.txt","r")

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
    count=count+1
    if count>100:
        break

#print("50.låttitel = ",v[50].artistnamn)
#print("50.låttitel = ",d['Orquesta Sonara La Habana'].låttitel•)
