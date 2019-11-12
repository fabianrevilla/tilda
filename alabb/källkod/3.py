import sys
from Fabian import *
from Node import *
from functions import *

m = MapEdges()
startcity = Node()
startcity.namn = str(sys.argv[1])
startcity.idx = m.getCityIdx(startcity.namn)
endcity = Node()
endcity.namn = str(sys.argv[2])
endcity.idx = m.getCityIdx(endcity.namn)

q = []
visited = []
q.append(startcity)
visited.append(startcity.namn)#lägger till startstaden i redan besökta

while len(q) != 0:#så länge kön inte är tom
	pNode = q.pop(0)#plockar ut den översta noden ur listan
	if pNode.namn == endcity.namn:#ifall slutstaden har hittats
		break
	else:
		pIdx = m.getCityIdx(pNode.namn)
		neighbors = m.getNeighborsTo(pIdx)#genererar en lista med index till grannar
		for idx in neighbors:
			newNode = Node()#skapar en nod
			newNode.namn = m.cities[idx][0]#sparar namn
			newNode.idx = m.getCityIdx(newNode.namn)#sparar index
			if newNode.namn not in visited:#om staden inte redan besökts
				newNode.parent = pNode#sparar parentnoden
				q.append(newNode)#lägg till Noden i kön
				visited.append(newNode.namn)#lägger till nodens namn i redan besökta
	
if len(q) == 0 and pNode.namn != endcity.namn:
	print("Vägen hittades inte")

else:
	print("")
	writechain(pNode)
	cost = calculatecost(pNode,m)
	print("")
	print("Total kostnad = ",cost,"sestertier")
	print("Kön innehåller",len(q),"noder")
	print("")




