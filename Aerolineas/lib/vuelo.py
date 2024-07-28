class Vuelo:
    def __init__(self, id, origen, destino,npasajeros,piloto):
        self.id = id
        self.origen = origen
        self.destino = destino
        self.npasajeros = npasajeros
        self.piloto = piloto
    
    def toJson(self):
        return {'Id':self.id,'Origen':self.origen,'destino':self.destino,'No. pasajeros':self.npasajeros,
                'Piloto':self.piloto}
