class Pasajero:
    def __init__(self, id, pasaporte, nombre):
        self.id = id
        self.pasaporte = pasaporte
        self.nombre = nombre

    def toJson(self):
        return {'id':self.id,'Pasaporte':self.pasaporte,'Nombre':self.nombre}
        