class Automovil:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def __str__(self):
        return self.marca+","+self.modelo+","+self.año
    