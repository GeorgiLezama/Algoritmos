class List:
    def FIN(self,l):
        return len(l)
    
    # Para funciones con listas como argumentos.
    def siguiente(self,p,l):
        if (p >= (self.FIN(l)-1)):
            return None
        elif (p < 0):
            return None
        else:
            for i in range(self.FIN(l)):
                if (i == p):
                    return l[i+1]
                
    def anterior(self,p,l):
        if (p > (self.FIN(l)-1)):
            return None
        elif (p <= 0):
            return None
        else:
            for i in range(self.FIN(l)):
                if (i == p):
                    return l[i-1]
                
    # Para persistencia de datos, con 1 argumentos:
    def siguiente2(self,p):
        file = open("Datos/datos.georgi")
        l = file.readlines()
        if (p >= (self.FIN(l)-1)):
            return None
        elif (p < 0):
            return None
        else:
            for i in range(self.FIN(l)):
                if (i == p):
                    return l[i+1].strip()
    def anterior2(self,p):
        file = open("Datos/datos.georgi")
        l = file.readlines()
        if (p > (self.FIN(l)-1)):
            return None
        elif (p <= 0):
            return None
        else:
            for i in range(self.FIN(l)):
                if (i == p):
                    return l[i-1].strip()
    