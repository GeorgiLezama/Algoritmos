class List:
    def FIN(self,l):
        return len(l)
    
    # Para 2 argumentos, con listas.
    def localiza(self,x,l):
        for i in range(len(l)-1):
            if x == l[i]:
                return i
        return None
    

    # Para 1 argumento, con persistencia de datos
    def localiza2(self,x):
        file = open("Dato/dato.georgi")
        l = file.readlines()
        for i in range(len(l)):
            if (x.strip() == l[i].strip()):
                return i
        return None
    