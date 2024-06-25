# Una empresa desea desarrollar una libreria con las siguientes funciones:
# 1.Agregar(x), esta funcion recibe un objeto x de tipo automovil que tiene los siguientes
#                   atributos: Marca, Modelo, año
# Esta libreria debe servir como almacen de datos, para esto se debe guardar la informacion
# en un archivo con extension .876
from lib.list import List
from lib.Automovil import Automovil
lista = List()
Auto1 = Automovil("Toyota","Tacoma", "2024")
Auto2 = Automovil("Honda","Civic","2019")
Auto3 = Automovil("Ford","Mustang", "2021")
print(lista.agregar(Auto3))

