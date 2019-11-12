def hashf(key,m):
    key=key.strip(" ")
    string=''
    hash=0
    for c in key:
        tal=ord(c)
        string=string+str(tal)
        hash=int(string)%m
    return hash
