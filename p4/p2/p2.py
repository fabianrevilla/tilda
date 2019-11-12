###################################################################
##       Definierar funktionen mult
##
## IN  - Två heltal x & y
##
## OUT - Produkten av de två heltalen, avrundat till närmsta heltal
##
## GÖR - Adderar |x| till sig själv under |y| st varv
##

def mult(x,y):
    
    n = 0
    sum=0
    x=int(x)
    y=int(y)
    if abs(x) > abs(y):
        while n < abs(y):
            sum=sum+abs(x)
            n = n + 1

    else:
        while n < abs(x):
            sum=sum+abs(y)
            n = n + 1
    
    if  x < 0 and y > 0 or x > 0 and y < 0:
        sum =-sum
        return sum

    elif x < 0 and y < 0:
        return sum
    
    else:
        return sum



def deldiv(t,n):
    prod=0
    x=1
    t=int(t)
    n=int(n)
    while  prod<abs(t):
        prod=mult(x,abs(n))
        x=x+1
    
    # Beräknar svar & rest
    if prod==abs(t):
        rest=0
        svar=x-1
    
    else:
        rest=abs(t)-mult(x-2,abs(n))
        svar=x-2
    
    return (rest,svar)

#####################################################################
##       Definierar funktionen div
##
## IN  - Två heltal t&n
##
## OUT - Kvoten mellan de två heltalen, avrundat till närmsta heltal
##
## GÖR - Delar upp kvoten och utför en division för varje enskilt tal i täljaren.
##       För varje deldivision kan det uppkomma en rest. Denna rest adderas till nästa deldivision
##       i programmet. Slutligen adderas alla termer av rest & delkvoter vilket ger svaret.
##

def div(t,n):
    t_int=int(abs(t))
    t_str=str(abs(t))
    n_int=int(abs(n))
    n_str=str(abs(n))
    
    i=0
    rest=0
    svar=''

    if n_int==0:
        svar='UNDEFINED'
        print("ERROR-DIVISION BY 0")
        raise ZeroDivisionError
    
    else:
        #Stegar igenom varje position i talet
        while i < len(t_str):
    
            del_str=str(rest)+t_str[i]        #Lägger ihop nästa tal i i täljare med rest
            del_t=int(del_str)                #Deltäljare
            (rest,delsvar)=deldiv(del_t,n_int)#Beräknar rest x & trunkerad kvot
            svar=str(svar)+str(delsvar)       #Lägger ihop svar & delsvar
            svar=int(svar)                    #Omvandlar svaret från sträng till integer
            i=i+1

    if t < 0 and n > 0 or t > 0 and n < 0:
        svar=-svar
        return svar

    elif t and n < 0:
        return svar
    else:
        return svar

c=div(1000200,50)
print("c = ",c)
