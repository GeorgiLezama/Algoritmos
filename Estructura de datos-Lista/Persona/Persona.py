class Personas:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
    
    # Sobreescribimos el toString(str).
    def __str__(self):
        return self.dni+""+self.nombre+""+self.apellido
    
