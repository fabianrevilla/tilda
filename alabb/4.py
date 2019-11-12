from Fabian import *
import sys,pickle
from Node import *
from functions import *
from heap import *
from karta import *
from qs import *

m = MapEdges()
startcity = Node()
startcity.namn = str(sys.argv[1])
startcity.idx = m.getCityIdx(startcity.namn)
startcity.coord = m.cities[startcity.idx][1]
startcity.prio = 0
endcity = Node()
endcity.namn = str(sys.argv[2])
endcity.idx = m.getCityIdx(endcity.namn)
endcity.coord = m.cities[endcity.idx][1]

q = Heap()
visited = []
q.insert(startcity)
visited.append(startcity.namn)#lägger till startstaden i redan besökta

while not q.isEmpty():#så länge kön inte är tom
	#print("q = ",q)
	pNode = q.getMin()#plockar ut den översta noden ur listan
	if pNode.namn == endcity.namn:#ifall slutstaden har hittats
		break
	elif pNode == None:
		print("Vägen finns inte")

	else:
		tempList = []#en provisorisk lista för att mellanlagra noder
		pIdx = m.getCityIdx(pNode.namn)
		neighbors = m.getNeighborsTo(pIdx)#genererar en lista med index till grannar
		for idx in neighbors:
			newNode = Node()#skapar en nod
			newNode.namn = m.cities[idx][0]#sparar namn
			newNode.idx = m.getCityIdx(newNode.namn)#sparar index
			newNode.coord = m.cities[idx][1]
			newNode.prio = pNode.prio + m.getCostBetween(pNode.idx, newNode.idx)#beräknar kostaden
			tempList.append(newNode)#lägger till i templist
		
#Sorterar grannarna med avseende på kostnad i resväg och lägger in de i priokön

		for node in tempList:#stegar igenom den sorterade listan
			if node.namn not in visited:#om staden inte redan besökts
				node.parent = pNode#sparar parentnoden
				q.insert(node)#lägg till Noden i priokön
				visited.append(node.namn)#lägger till nodens namn i redan besökta

writechain(pNode)
cost = calculatecost(pNode,m)
dist = calcdist(pNode)
print("Total kostnad = ",cost,"sestertier")
print("Total sträcka = ",dist,"st städer")
print("Priokön har = ",q.numOfNodes(),"element")

#Skriver ut kartan
#FILE = open("resultat.pkl",'rb')
#island_data = pickle.load(FILE)
#FILE.close()
#print(drawMap(island_data[3]))
#print(drawPath(pNode,drawMap(island_data[3])))