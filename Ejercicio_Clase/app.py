# Crear una libreria que contenga las siguientes funciones
# Calculo de potencia (recursividad)
# Dada una lista de numeros retorne la suma
# Dada una lista de numeros retorne el promedio
# Dada una lista de numeros retorne la moda

class math:
    # potencia
    def potencia(self,x,y):
        if (y == 0):
            return 1
        else:
            return x * self.potencia(x,(y-1))
    # Suma
    def suma(self,list):
        if (len(list) == 1):
            return list[0]
        else:
            return list[0] + self.suma(list[1:])
    # Promedio
    def promedio(self,lista):
        promedio = self.suma(lista)/len(lista)
        return promedio
    # moda
    def moda(self, lista):

        cant_datos = [0] * len(lista)
        
        for i in range(len(lista)):
            for j in range(len(lista)):
                if lista[i] == lista[j]:
                    cant_datos[i] += 1
        
        cant_max = cant_datos[0]
        moda = lista[0]
        for i in range(1, len(cant_datos)):
            if cant_datos[i] > cant_max:
                cant_max = cant_datos[i]
                moda = lista[i]
        
        return moda

from app import math
objeto = math()
print(objeto.potencia(2,4))
print(objeto.suma([3,4,6,3,1]))
print(objeto.promedio([3,4,6,3,1]))
print(objeto.moda([6,1,6,4,8,4,3,4]))
