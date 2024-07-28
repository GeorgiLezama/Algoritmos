# Una aerolinea desea crear una estructura de datos que permita gestionar los vuelos a 
# diferentes partes del mundo, para ellos se debe crear una libreria con las siguinetes 
# funciones:

# 1. registrar_vuelos(v): registra un vuelo con la informacion como origen, destino, no. pasajeros
# y nombre del piloto. Esto entra a un orden de despliegue segun el registro.
# 2. registrar_pasajeros(p,v)
# 3. obtener_proximo_vuelo()
# 4. registrar_carga(c,v)
# 5. descargar_carga(v)

from lib.lib import lib
from lib.vuelo import Vuelo
from lib.pasajero import Pasajero
pasajero1 = Pasajero(1,123,"Jorge")
pasajero2 = Pasajero(2,1234,"Alejandro")
pasajero3 = Pasajero(3,12345,"Anny")
vuelo1 = Vuelo(1,"Honduras","España",7,"Karelia")
vuelo2 = Vuelo(2,"Nicaragua","Inglaterra",7,"Allisson")
vuelo3 = Vuelo(3,"Argentina","Portugal",7,"Henry")
lib = lib()
lib.registrar_pasajeros(pasajero3,vuelo2)
