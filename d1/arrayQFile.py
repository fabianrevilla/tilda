##
## Labb d1 i Tillämpapad datalogi & programmering
##
##

from array import array

class ArrayQ:

	def __init__(self,array=[]): ##Konstruerar klassens attribut
		self.__array=array
    

	def disp(self):
		print(self.__array)

	def enqueue(self,x):  # Lägger till x sist i listan
		self.__array.append(x)
		#print("self.__array after append= ",self.__array)

	def dequeue(self): #Plockar ut det som står först i listan
		return self.__array.pop(0) #Poppar elementet med index 0


######################################################################
## TESTKOD

if __name__ == "__main__":
    def basictest():
        q = ArrayQ()
        q.enqueue(1)
        q.enqueue(2)
        x = q.dequeue()
        y = q.dequeue()
        if (x == 1 and y == 2):
            print("test OK")
        else:
            print("FAILED expexted x=1 and y=2 but got x =", x, " y =", y)

    basictest()
    
######################################################################







