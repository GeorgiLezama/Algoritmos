class List:
    def FIN(self,L):
        return len(L)
    
    # Con listas ya dadas
    def insertar(self,x,p,L):
        if self.FIN(L)==0:
            L.append(x)
        elif p > self.FIN(L):
            return None
        else:
            L.append(None)
            for i in range(self.FIN(L)-1, p,-1):
                L[i] = L[i-1]
            L[p] = x+"\n"
        return L
    
    # Para datos guardados en texto
    def inserta2(self,x,p):
        file = open("Data/data.txt")
        L = file.readlines()

        if self.FIN(L)==0:
            L.append(x)
            file.close()
        elif p > self.FIN(L):
            return None
        else:
            L.append(None)
            for i in range(self.FIN(L)-1, p,-1):
                L[i] = L[i-1]
            L[p] = str(x) + "\n"
        file = open("Data/data.txt", "w")
        for i in L:
            file.write(str(i))
        file.close()
        return L
    
    # Para trabajar con objetos.
    def inserta3(self, x, p):
        import csv
        file = open("CSV/prueba.csv")
        reader = csv.reader(file)
        L = list(reader)

        if self.FIN(L)==0:
            L.append(x)
            file.close()
        elif p > self.FIN(L):
            return None
        else:
            L.append(None)
            for i in range(self.FIN(L)-1, p,-1):
                L[i] = L[i-1]
            L[p] = [x]
        
        file = open("CSV/prueba.csv", mode='w', newline='')
        writer = csv.writer(file)
        writer.writerows(L)
        file.close()
        return L
    
    # Metodo para obtener los objetos como listas.
    def obtener_atributos(self, mi_lista):
        import csv
        file = open("CSV/prueba.csv")
        l = csv.reader(file)
        for i in l:
            mi_lista.append(i)
        file.close()
        return mi_lista
        
    
    

        


                

