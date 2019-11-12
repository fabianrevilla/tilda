class Node:
    def __init__(self,key,value,left=None,right=None):
        self.key=key
        self.value=value
        self.left=left
        self.right=right

#rekursiv store
def rekstore(p,key,newvalue):
    if p==None:         #ifall noden som skickas in inte finns
        return Node(key,newvalue)#returnerar fadernoden
        
    elif key < p.key:   #ifall värdet som ska sättas in är mindre än den nuvarande noden
        p.left=rekstore(p.left,key,newvalue)
    
    else:               #ifall värdet som ska sättas in är större än den nuvarande noden
        p.right=rekstore(p.right,key,newvalue)

    return p

#rekursiv write
def rekwrite(p):
    while p!=None:       #så länge den nuvarande noden inte är tom
        rekwrite(p.left) #skriv ut vänster delträd rekursivt
        print(p.key)     #printar nyckel
        print(p.value)   #printar data
        rekwrite(p.right)#skriv ut höger delträd rekursivt

#rekursiv search
def reksearch(p,key):
    if p.key==key:       #ifall nyckeln är hittad
        return p.value        #värdet som finns på platsen dit nyckeln leder
    elif key < p.key:    #ifall nyckeln som söks är mindre än nuvarande nyckeln
        return reksearch(p.left,key)
    else:
        return reksearch(p.right,key)
    return

class Bintree:
    def __init__(self):
        self.root=None#rootnoden
    
    def __contains__(self,key):
        p=self.root#rootnoden
        while p!=None:
            if p.key==key:#ifall noden är hittad
                return True

            elif key < p.key:# ifall den sökta nyckeln är mindre än den nyckel som söks
                p=p.left#går vänster

            else:
                p=p.right#går höger
        return False
        
    def store(self,key,newvalue):
        #Sorterar in newvalue i trädet
        self.root=rekstore(self.root,key,newvalue)

    def search(self,key):
        # returnerar value om key finns i trädet, KeyError annars
        if key not in self:
            raise KeyError
        
        else:
            x=reksearch(self.root,key)
            return x

    def write(self):
        # Skriver ut trädet i inorder
        rekwrite(self.root)
        print("\n")




