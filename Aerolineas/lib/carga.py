class Carga:
    def __init__(self,peso,ancho,profundidad):
        self.peso = peso
        self.ancho = ancho
        self.profundiad = profundidad
    
    def toJson(self):
        return {'Peso':self.peso,'Ancho':self.ancho,'Profundidad':self.profundiad}