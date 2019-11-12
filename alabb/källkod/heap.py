class HeapNode:

    def __init__(self, data, prio):
        """data är det objekt vi vill lagra
           prio är nyckelvärdet som används för att jämföra objekten"""
        self.data = data
        self.prio = prio

    def __str__(self):
        return "{0}:{1}".format(self.data, self.prio)

class Heap:
    # En min-heap

    def __init__(self):
        """Skapar en lista där vi använder element 1..minsize"""
        self.minsize = 500
        self.tab = (self.minsize+1)*[None]
        self.size = 0

    def isEmpty(self):
        """Returnerar True om heapen är tom, False annars"""
        return self.size  == 0

    def isFull(self):
        """Returnerar True om heapen är full, False annars"""        
        return self.size == self.minsize

    def insert(self, node):
        """Lägger in nya data med nyckeln prio i heapen"""
        if not self.isFull():
            self.size += 1
            self.tab[self.size] = node
            i = self.size
            while i > 1 and self.tab[i//2].prio > self.tab[i].prio:#sålänge fadern är större
                self.tab[i//2], self.tab[i] = self.tab[i], self.tab[i//2]
                i = i//2

    def getMin(self):
        """Hämtar det största (översta) objektet ur heapen"""
        if not self.isEmpty():
            data = self.tab[1]
            self.tab[1] = self.tab[self.size]
            self.size -= 1
            i = 1
            while i <= self.size//2:
                mini = self.minindex(i)
                if self.tab[i].prio > self.tab[mini].prio:
                    self.tab[i],self.tab[mini] = self.tab[mini], self.tab[i]
                i = mini
            self.tab[self.size+1] = None
            return data
        else:
            return None

    def delNode(self,node):
        if not self.isEmpty():
            #Sätter den sista noden i listan på den gamla nodens plats
            i = self.tab.index(node)#hämta index för den givna noden
            self.tab[i] = self.tab[self.size]#switchar roten & noden som ska tas bort
            self.size -= 1
            while i <= self.size//2:
                mini = self.minindex(i)
                if self.tab[i].prio > self.tab[mini].prio:
                    self.tab[i],self.tab[mini] = self.tab[mini], self.tab[i]
                i = mini
            self.tab[self.size+1] = None
            return node
        else:
            return None


    def minindex(self, i):
        """Returnerar index för det minsta barnet"""
        if 2*i+1 > self.size:
            return 2*i
        if self.tab[2*i].prio < self.tab[2*i+1].prio:
            return 2*i
        else:
            return 2*i+1

    def numOfNodes(self):
        count = 0
        for idx in self.tab:
            if idx is not None:
                count += 1
        return count


