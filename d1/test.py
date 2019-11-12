from linkedQFile import LinkedQ
from linkedQFile import Node
#from arrayQFile import ArrayQ
a=input("Vilken ordning_in ligger korten i?") #Lagrar input i en sträng
ordning_in=LinkedQ()                          #Skapar objektet för inordningen
a=a.split()                                   #Gör strängen till en lista utan mellanslag
for indx, i in enumerate(a):                  #Omvandlar varje character i listan till integer
    ordning_in.enqueue(int(i))

/Users/fabian/Desktop/skolskit/Tilda/Datorlabbar/d1/test.py
k=len(a)
svar=k*[0]
for i in range(k):
    #ordning_in.disp()
    x=ordning_in.dequeue()  #Plockar ut det översta kortet
    ordning_in.enqueue(x)
    x=ordning_in.dequeue()
    ordning_in.disp()
    svar[i]=int(x)

print("svar = ",svar)
#RÄTT ORDNING 7 1 12 2 8 3 11 4 9 5 13 6 10
