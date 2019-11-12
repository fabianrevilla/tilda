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

c=mult(3,3)
#print("sum=",c)

