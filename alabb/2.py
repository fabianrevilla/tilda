from karta import *
from Fabian import *

m = MapEdges()
x = 0
y = 0
l = []
for c in island_map:
	
	if c == "\n":#om tecknet är en radbrytning
		x = -1#x nollställs
		y +=1

	elif ord(c) > 2000:
		l.append((x,y))
	x +=1

for city in m.cities: 
	if city[1] in l:
		print("Stadsnamn = ",city[0])
		print("Koordinater = ",city[1])
		print("\n")
