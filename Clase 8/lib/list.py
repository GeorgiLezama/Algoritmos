class List:
    def FIN(self,L):
        return len(L)
    def insertar(self,x,p,L):
        if self.FIN(L)==0:
            L.append(x)
        elif p > self.FIN(L):
            return None
        else:
            L.append(None)
            for i in range(self.FIN(L)-1, p,-1):
                L[i] = L[i-1]
            L[p] = x

        return L
    
    def inserta2(self,x,p):
        file = open("Data/data.txt")
        L = file.readlines()

        if self.FIN(L)==0:
            L.append(x)
        elif p > self.FIN(L):
            return None
        else:
            L.append(None)
            for i in range(self.FIN(L)-1, p,-1):
                L[i] = L[i-1]
            L[p] = x

        return L