# Binärsökning av en lista med låtobjekt
#

def binary_search(sequence, value):
    lo, hi = 0, len(sequence) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sequence[mid].låttitel < value:#ifall mittenelementet är mindre än det värde som söks
            lo = mid + 1#går till den högra dellistan
        elif value < sequence[mid].låttitel:#ifall mittenelementet är större än det värde som söks
            hi = mid - 1#går till den vänsta dellistan
        elif mid == None:#om midelementet är odefinerat
            raise typeError
        else:
            return mid
    return None

