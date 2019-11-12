from makechildren import makechildren
from hashtest import DictHash
from linkedQFile import LinkedQ

startord='fan'
slutord='gud'
visited=DictHash()
visited.store(startord,startord)
queueOfWords=LinkedQ()
q=LinkedQ()
queueOfWords.enqueue(startord)#lägger startordet i kön
while not queueOfWords.isEmpty():
    nextWord = queueOfWords.dequeue()#plockar ut första elementet ur kön
    if nextWord==slutord:#om elementet är slutordet
        break
    else:
        makechildren(nextWord,visited,queueOfWords)#skapa alla barn
print("slutord = ",slutord)


