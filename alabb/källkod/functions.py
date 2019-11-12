from Node import *
import random
## Räknar alla städer i en ö
## IN En lista med besäkta noder, startindex i listan samt ett kartobjekt m
## OUT En lista med besökta(räknade) noder
def cityCounter(startidx, visited, m):
#Skapar en ny nod utifrån startindexet
	q = []#Kö
	startnode = Node()
	startnode.namn = m.cities[startidx][0]
	startnode.idx = m.getCityIdx(startnode.namn)

	q.append(startnode)
	if startnode.idx not in visited:
		visited.append(startnode.idx)
	
	while len(q) != 0:#Sålänge kön inte är tom
		#Plocka ur första noden ut kön
		node = q.pop()
		#Genererar alla grannstäder
		nb = m.getNeighborsTo(node.idx)
		for idx in nb:#Stegar igenom listan med grannar
			node = Node()
			node.namn = m.getCityName(idx)
			node.idx = idx
			if idx not in visited:#ifall staden inte har besökts
				q.append(node)#lägger till noden i kön
				visited.append(node.idx)#lägger till noden i redan besökta
	return visited	

## Skriver ut vägen mellan två städer
## IN nod
## OUT Utskrift av alla noder på en väg mellan två städer
def writechain(node):
	if node == None:
		return
	writechain(node.parent)
	print("Namn = ",node.namn)
	print("Index = ",node.idx)
	print("Prioritetsvärde = ",node.prio)
	print("Koorninater = ",node.coord)
	print("")

## Beräknar total kostnad för en väg mellan två städer
## IN slutnod & 
def calculatecost(node,m):
	if node.parent == None:
		return 0	
	return calculatecost(node.parent,m) + m.getCostBetween(node.idx, node.parent.idx)

## Beräknar avståndet mellan två städer mätt i antalet städer
## IN En slutnod
## OUT Det totala beräknade avståndet
def calcdist(Node):
	if Node == None:
		return 0
	return calcdist(Node.parent) + 1

## Skriver ut varje nod i en lista
## IN En lista med noder
## OUT Utskrift av varje nod med dess data 
def printlist(l):
	for node in l:
		print("\n")
		print("Namn = ",node.namn)
		print("Index = ",node.idx)
		print("Prioritetsvärde = ",node.prio)

##Numrerar varje stad i en väg som en algoritm har valt
## IN En slutnod i algoritmen och en karta som en lång textsträng
## OUT En kart-sträng med städerna utmarkerade(numrerade)
def drawPath(node,mapStr):
	coordList = []
	currentnode = node
	while currentnode != None:
		coordList.insert(0,currentnode.coord)
		currentnode = currentnode.parent
	print("coordList = ",coordList)

	x = 0
	y = 0
	l = []
	count = 1
	s = list(mapStr)
	for num,c in enumerate(s):

		if c == "\n":#om tecknet är en radbrytning
			x = -1#x nollställs
			y +=1

		elif (x,y) in coordList:
			s[num] = str(coordList.index((x,y))+1)
			count += 1
		x +=1

	return "".join(s)

## Funktion som ritar en karta utifrån stadskoordinater
## IN En lista med stadskoordinater
## OUT En karta som en sträng med städerna utmarkerade
##
def drawMap(idxList):
	w = 120
	h = 25
	s = (w*h)*['.']
	x = 0
	y = 0
	ll = int('1F3E0',16)
	hl = int('1F3E5',16)
	
	#Konstruerar kart-strängen
	for num,c in enumerate(s):
		if x == w:
			s[num-1] = "\n"
			x = -1#x nollställs
			y +=1

		elif (x,y) in idxList:
			s[num-1] = chr(random.randint(ll,hl+1))
		x +=1

	#Returnerar kartan
	return str(''.join(s))


   