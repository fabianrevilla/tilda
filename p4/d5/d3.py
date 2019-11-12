from makechildren import makechildren
from hashtest import DictHash
from linkedQFile import LinkedQ
import sys

if len(sys.argv) < 3:
    print("Start- och slutord saknas")
    print("Använd programmet så här: \n\t python3", sys.argv[0], " [startord] [slutord]")
    sys.exit()

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

startNode=ParentNode(sys.argv[1])
slutNode=ParentNode(sys.argv[2])
visited=DictHash()
visited.store(startNode,startNode)
queueOfNodes=LinkedQ()
q=LinkedQ()
queueOfNodes.enqueue(startNode)#lägger startnoden i kön
while not queueOfNodes.isEmpty():
    nextNode = queueOfNodes.dequeue()#plockar ut första noden ur kön
    if nextNode.word==slutNode.word:#om elementet är slutordet
        break
    else:
        makechildren(nextNode,visited,queueOfNodes)#skapa alla barn

def writechain(parentNode):
    if parentNode==None:
        return
    writechain(parentNode.parent)
    print(parentNode.word)

writechain(nextNode)
