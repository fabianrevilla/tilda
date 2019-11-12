## Testprogram för funktionen div()
##
## Testar funktionen div genom att jämföra returnerade värden med förväntade värden.
##

from p2 import mult, div

#INDATA & FÖRVÄNTADE SVAR
t_in=[100090909,100090909,25,-100090909,-100090909]
n_in=[1,1000909,5,1,-1000909,0]
svar_forv= [100090909,100,5,-100090909,100]

#BERÄKNADE SVAR
k=0
svar_ret=[]
#Lägger in de beräknade svaren i en lista
for i in t_in:
    t=int(i)
    n=int(n_in[k])
    svar_ret.append(div(t,n))   # Lägger till svar_retet sist i listan
    k=k+1

#Kör testprogrammet för de 5 första värdena
k=0
while k < len(svar_forv):
    
    t=int(i)
    n=int(n_in[k])
    svar_ret_r=int(svar_ret[k])
    svar_ret_f=int(svar_forv[k])
    
    #Ifall returnerat- och förväntat svar stämmer överens
    if svar_ret_r-svar_ret_f == 0:
        print("\n Testar ",i,"/",n,"\n","Fick:",svar_ret_r,"\n","Förväntat resultat:",svar_forv[k],"\n","Testet LYCKADES!")
    
    #Ifall returnerat- och förväntat svar skiljer sig
    else:
        print("Testar ",i,"/","\n",",fick ",svar_ret_r,", förväntat resultat ",svar_forv[k],", testet MISSLYCKADES!")

    print("")
    print("")
    k=k+1

#Specialfallet då nämnaren är 0

print("Testar ",t_in[-1],"/",n_in[-1])

try:
    div(t_in[-1],n_in[-1])
    print("Testet MISSLYCKADES")

except ZeroDivisionError:
    print("Fick error - division by zero \nTestet LYCKADES\n")
