class lista:
    def FIN(L):
        return(L)
    
    def insertar(self,x,p,L):
        if self.FIN == 0:
            L.append(x)
        elif self.FIN == 1:
            for i in L:
                if (i == p):
                    auxiliar = L[i]
                    L[i+1] = auxiliar
                    L[i] = x
                else:
                    L[i] = x
        elif self.FIN > 0:
            for i in range(0,len(L)-1):
                if (i >= p):
                    auxiliar = L[i]
                    L[i+1] = auxiliar
                    L[i] = x
        elif self.FIN < p:



                


