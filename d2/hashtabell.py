from hashf import hashf
m=23
class HashNode:
    def __init__(self,key,val):
        self.hash=hashf(key,m) #beräknar objektets index i listan m.h.a. hashfunktion
        self.key=key
        self.val=val


class HashTable:
    def __init__(self):
        self.l=[None]*m#skapar en lista med m st toma platser
    
    def store(self,key,val):
        nodetobeadded=HashNode(key,val)
        new_hash=nodetobeadded.hash
        if self.l[nodetobeadded.hash]==None:#ifall platsen dit nyckeln leder är ledig
            self.l[nodetobeadded.hash]=nodetobeadded#noden läggs till i listan
        else:
            i=0
            new_hash=nodetobeadded.hash
            while self.l[new_hash]!=None:
                new_hash=new_hash+(i+1)**2#kvadratisk probning
                if new_hash>(m-1):#ifall hashvärdet kommer övestiga listans högsta index
                    new_hash=(new_hash-1)%m

                i=i+1
            nodetobeadded.hash=new_hash
            self.l[nodetobeadded.hash]=nodetobeadded#noden läggs till i listan

    def search(self,key):#returnerar värdet i listan som nyckeln ge
        start_node=HashNode(key,None)#skapar en tillfällig nod med key som nyckel
        new_hash=start_node.hash#nodens hashvärde blir startvärde för hashräknaren
        new_key = self.l[start_node.hash].key#startnodens nyckel blir startvärde för keyräknaren
        
        i = 0
        while new_key != key:#så länge den nuvarande nyckeln inte är nyckeln vi söker
            new_hash=new_hash+(i+1)**2
            if new_hash > (m-1):#om hashvärdet överstiger listans storlek
                new_hash = (new_hash-1)%m#gör om indexet till ett tal mellan 0 & m
            elif self.l[new_hash]==None:
                break
            new_key = self.l[new_hash].key#nästa nyckel blir nästa nods nyckel
            
            i = i + 1
                
        if self.l[new_hash]==None:
            raise KeyError
        else:
            return self.l[new_hash].val

