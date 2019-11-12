from hashtest import DictHash
from linkedQFile import LinkedQ

l=[i*1 for i in range(97,123)]
l.append(29)
l.append(28)
l.append(246)
class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

def makechildren(fatherNode,visited,q):
    visited.store(fatherNode.word,fatherNode.word)
    ordlista=DictHash()
    f=open("word3.txt","r",encoding="utf-8")
    count=0
    for r in f:
        word=r.strip("\n")#tar bord radbrytningstecknet från varje ord
        #print("word = ",word)
        ordlista.store(word,word)#sparar varje ord i tabellen med nyckeln word

    for i,x in enumerate(l):#byter första bokstaven
        s=fatherNode.word[1:3]
        s=chr(x)+s
        if s in ordlista and s not in visited:#ifall ordet finns i bland listan av godkända ord
            visited.store(s,s)
            childNode=ParentNode(s)
            childNode.parent=fatherNode
            q.enqueue(childNode)
            count=count+1

    for i,x in enumerate(l):#byter mittersta bokstaven
        s1=fatherNode.word[0]
        s2=fatherNode.word[2]
        s=s1+chr(x)+s2
        if s in ordlista and s not in visited:#ifall ordet finns i bland listan av godkända ord
            visited.store(s,s)
            childNode=ParentNode(s)
            childNode.parent=fatherNode
            q.enqueue(childNode)
            count=count+1

    for i,x in enumerate(l):#byter tredje bokstaven
        s=fatherNode.word[0:2]
        s=s+chr(x)
        if s in ordlista and s not in visited:#ifall ordet finns i bland listan av godkända ord
            visited.store(s,s)
            childNode=ParentNode(s)
            childNode.parent=fatherNode
            q.enqueue(childNode)
            count=count+1


######################################################################

