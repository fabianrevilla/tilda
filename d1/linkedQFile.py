class Node:
	def __init__(self,value,next=None): ##Konstruerar klassens attribut
		self.value=value
		self.next=next

## Håller koll på hela listan, vilken nod som är först och sist
class LinkedQ:
    def __init__(self): ##Konstruerar klassens attribut
        self.__first=None #Första elementet i kön
        self.__last=None  #Sista elementet i kön
        self.__count=0    #Antal element i kön, default är 0

    def enqueue(self,value):
        new_node=Node(value)

        if self.__last is not None: 	     # Om listan har sista nod
            self.__last.next=new_node      # Gör att nextpekaren från gamla noden pekar på den nya noden

        else:
            self.__first=new_node 		 # Ifall listan är tom blir den nya noden både första & sista #elementet i listan

        self.__last=new_node               # Nya noden läggs sist i kön
        self.__count+=1 					 # Registrerar att ett element har lagts till i kön

    def dequeue(self):

        if self.__count!=0 and self.__count!=1: 			     # Ifall listan inte är tom

            old_value=self.__first.value
            self.__first = self.__first.next # Flyttar firstpekaren till nästa element
            self.__count -= 1 			 # Registrerar att ett element har tagits bort från kön
            return old_value

        elif self.__count==1:
        	old_value=self.__first.value
        	self.__first=None
        	self.__last=None
        	return old_value


        else:
            print("Kön är tom")

    def isEmpty(self): #Kollar ifall listan är tom
        if self.__count==0:
        	print("Kön är tom")
        	return True

        else:
            print("Kön är inte tom")
            return False

    def disp(self):
        current = self.__first
        while current is not None:
            print(current.value, end = ' ')
            current = current.next

    def contains(self,value):
        current = self.__first
        while current.value is not value:
            if curren.next==None:
                return False
                break
            else:
            current = current.next
        return True


######################################################################
## TESTKOD

if __name__ == "__main__":

    #Skapar en tom kö
    q=LinkedQ()

    #Lägger till tre värden i kön
    q.enqueue(3365)
    q.enqueue(34)
    q.enqueue(0)
    q.enqueue(9595)
    q.dequeue()
    
    x=q.dequeue()


    #Kollar om kön är tom
    q.isEmpty()

    #Kollar om ordningen är rätt
    print("Första värdet är = ",q.__first.value)
    print("Andra värdet är = ",q.__first.next.value)
    #print("Tredje värdet är = ",q.__first.next.next.value)
    print("Sista värdet är = ",q.__last.value)
    print("x = ",x)
######################################################################
