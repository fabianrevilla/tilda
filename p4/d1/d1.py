from arrayQFile import ArrayQ
#from linkedQFile import LinkedQ
#from linkedQFile import Node

a=input("Vilken ordning_in ligger korten i?") #Lagrar input i en sträng
ordning_in=ArrayQ()                           #Skapar objektet för inordningen
a=a.split()                                   #Gör strängen till en lista utan mellanslag
for indx, i in enumerate(a):                  #Omvandlar varje character i listan till integer
    ordning_in.enqueue(int(i))

k=len(a)#Antal kort i kortleken
svar=k*[0]
for i in range(k):
    x=ordning_in.dequeue()  #Plockar ut det översta kortet
    ordning_in.enqueue(x)   #Lägger det uttagna kortet längst bak i listan
    x=ordning_in.dequeue()  #Plockar ut det översta kortet
    svar[i]=int(x)
print("Ordning efter tricket = ",svar)

