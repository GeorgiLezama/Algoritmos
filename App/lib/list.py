class List:
    def FIN(self,L):
        return len(L)
    def agregar(self,x):
        file = open("Datos/dato.876")
        L = file.readlines()
        if (self.FIN(L) == 0):
            L.append(x)
        else:
            L.append("")
            for i in range(self.FIN(L)):
                if (L[i] == ""):
                    L[i] = str(x) + "\n"
        file = open("Datos/dato.876", "w")
        for i in L:
            file.write(str(i))
        file.close()
        return L

    


