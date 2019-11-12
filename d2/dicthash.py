class DictHash:
    def __init__(self):
        self.lista={}#skapar tom lista som heter
    
    def store(self,nyckel,data):
        self.lista[nyckel]=data#lagrar data i listan dic med nyckeln "nyckel"
    
    def search(self,nyckel):
        nyckel=str(nyckel)#lägger till \n efter sökordet
        x=self.lista[nyckel]
        return x

låtlista=DictHash()
f = open("unique_tracks.txt","r")
count=0
for r in f:
    s=r.split("<SEP>")#splitar varje rad vid varje <SEP> markör
    artist=s[2]
    låt=s[3]
    låtlista.store(artist,låt)#artist blir nyckel, låt blir data
    count=count+1
    if count > 100:
        break
x=låtlista.search('Yerba Brava')
print("x= ",x)
