class DictHash:
    def __init__(self):
        self.lista={}#skapar tom lista som heter
    
    def __contains__(self,nyckel):
        try:
            self.lista[nyckel]
            return True
        except KeyError:
            return False
    
    def store(self,nyckel,data):
        self.lista[nyckel]=data#lagrar data i listan dic med nyckeln "nyckel"

    def search(self,nyckel):
        if nyckel in lista:
            return x
        else:
            raise KeyError
