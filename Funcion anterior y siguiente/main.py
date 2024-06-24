from lib.list import List
objeto = List()
# Funiones anterior y siguiente con 2 argumentos (p,l)
lis = ["2","y",3,4,5]
print(objeto.anterior(2,lis))
print(objeto.siguiente(2,lis))
# Funciones anterior y siguiente con 1 argumento (persistencia de datos) (p)
print(objeto.anterior2(2))
print(objeto.siguiente2(2))
