from Fabian import *
import sys,pickle
from Node import *
from functions import *
from heap import *
from karta import *

maxv = 200000
m = MapEdges()
l = m.getNumberOfCities() * [None]
visited =[]

#Skapar en startnod med prio 0
startnode = Node()
startnode.namn = sys.argv[1]
startnode.idx =m.getCityIdx(startnode.namn)

#Slutnod
slutnode = Node()
slutnode.namn = sys.argv[2]
slutnode.idx = m.getCityIdx(slutnode.namn)

##Skapar en priokö
pq = Heap()

#Lagra all städer i noder
for idx in range(m.getNumberOfCities()):
	node = Node()
	node.namn = m.cities[idx][0]
	node.idx = m.getCityIdx(node.namn)
	node.coord = m.cities[idx][1]
	l[node.idx] = node #lägger till noden i en lista på rätt index
	if idx == startnode.idx:
		node.prio = 0
	else:
		node.prio = maxv
	pq.insert(node)#lägger in noden i priokön


#Sålänge priokön inte är tom
while not pq.isEmpty():
	#Plocka ut första noden från prioritetskön
	parentnode = pq.getMin()
	visited.append(parentnode.idx)
	#Undersök nodens grannar en & en
	neighborsidx = m.getNeighborsTo(parentnode.idx)
	for childidx in neighborsidx:

		#Räkna ut kostnaden att gå från p till barnet.
		cost = m.getCostBetween(parentnode.idx,childidx)
		#Om kostnaden är mindre än barnets nuvarande prioritet (från början var kostnaden ∞) 
		if childidx not in visited and parentnode.prio + cost < l[childidx].prio :

			#sätt föräldrapekaren att peka på p
			l[childidx].parent = parentnode
			#sätt om barnets prioritet till den nya kostnaden
			l[childidx].prio = parentnode.prio + cost
			#Omprioritera barnet genom att ta bort noden & sedan sätta in igen
			#Tar bort noden ur listan
			tempnode = pq.delNode(l[childidx])
			#Sätter in noden i listan
			pq.insert(tempnode)

writechain(l[slutnode.idx])
totcost = calculatecost(l[slutnode.idx],m)
dist  = calcdist(l[slutnode.idx])
print("Total kostnad = ",totcost,"sestertier")
print("Total sträcka = ",dist,"st städer")
print("Priokön har = ",pq.numOfNodes(),"element")

#Skriver ut kartan
#FILE = open("resultat.pkl",'rb')
#island_data = pickle.load(FILE)
#FILE.close()
#print(drawMap(island_data[3]))
#print(drawPath(l[slutnode.idx],drawMap(island_data[3])))
