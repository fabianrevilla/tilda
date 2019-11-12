#Sorterar låtobjekt med avseende på låttitel

def quicksort(lista):
    sista = len(lista) - 1
    qsort(lista, 0, sista)

def qsort(lista, low, high):
    pivotindex = (low+high)//2
    # flytta pivot till kanten
    lista[pivotindex], lista[high] = lista[high], lista[pivotindex]  
    
    # damerna först med avseende på pivotlista
    pivotmid = partitionera(lista, low-1, high, lista[high].låttitel)
    
    # flytta tillbaka pivot
    lista[pivotmid], lista[high] = lista[high], lista[pivotmid]       
    
    if pivotmid-low > 1:
        qsort(lista, low, pivotmid-1)
    if high-pivotmid > 1:
        qsort(lista, pivotmid+1, high)

def partitionera(lista, v, h, pivot):
    while True:
        v = v + 1
        while lista[v].låttitel < pivot:
            v = v + 1
        h = h - 1
        while h != 0 and lista[h].låttitel > pivot:
            h = h - 1
        lista[v], lista[h] = lista[h], lista[v]
        if v >= h: 
            break
    lista[v], lista[h] = lista[h], lista[v]
    return v


