from hashf import hashf

m=103#primtal som ger listan "50% luft"
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
        starthash=nodetobeadded.hash
        if self.l[nodetobeadded.hash]==None:#ifall platsen dit nyckeln leder är ledig
            self.l[nodetobeadded.hash]=nodetobeadded.val
        else:
            
            i=0
            new_hash=nodetobeadded.hash
            while self.l[new_hash]!=None:
                next_hash=new_hash+(i+1)**2
                if next_hash>(m-1):#ifall hashvärdet kommer övestiga listans högsta index
                    new_hash=starthash
                    while self.l[new_hash]!=None:
                        new_hash=(new_hash+i**2-1)%m#räknar med modulo
                        i=i+1
                else:
                    new_hash=new_hash+i**2
                    i=i+1
            
            nodetobeadded.hash=new_hash
            self.l[nodetobeadded.hash]=nodetobeadded.val

    def search(self,key):#returnerar värdet i listan som nyckeln ge
        node=HashNode(key,None)
        starthash=node.hash
        if self.l[node.hash]==None:#ifall nyckeln inte finns
            raise KeyError
        else:
          return self.l[node.hash]
