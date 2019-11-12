# Binary Search
# Letar efter ett givet artistnamn i en lista med låtobjekt
# IN: Lista med låtobjekt
# UT: Listindexet för det sökna artistnamnet
def binary_search(array, needle_element):
    mid = int(len(array) / 2)
    if not len(array):
        raise ValueError
    
    if needle_element == array[mid].artistnamn:
        return mid#returnerar objektet
    elif needle_element > array[mid].artistnamn:
        return mid + binary_search(array[mid:],needle_element)
    elif needle_element < array[mid].artistnamn:
        return binary_search(array[:mid],needle_element)
    else:
        raise RecursionError

