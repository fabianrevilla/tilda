from Fabian import *
import pickle

m = MapEdges()


#Definierar variabler & listor
islandCount = 0
visited = []
q = []
island_data = []
#Stegar igenom alla index mellan 0 och antalet städer-1
for startidx in range(m.getNumberOfCities()):
	if startidx not in visited:
		citycount = 0
		islandCount += 1
		q.append(startidx)
		while len(q) != 0:
			idx = q.pop(0)#plockar ut det första elentet ur kön
			neighbors = m.getNeighborsTo(idx)
			templist = []#initierar en tom lista
			for idx in neighbors:
				if idx not in visited:
					citycount += 1
					q.append(idx)
					visited.append(idx)
					coord = m.getCityCoord(idx)
					templist.append(coord)
					island_data.append(templist)
		#print("den %d:a ön" %(islandCount),"har",citycount,"städer")

print("Totalt finns det",islandCount,"öar i övärlden")
#Spara ner kartorna i en extern fil
FILE = open("resultat.pkl",'wb')
pickle.dump(island_data,FILE)
FILE.close()

			
