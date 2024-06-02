# Creamos funcion para sumar todos los numeros desde i hasta s.
def suma_recursiva(i,s):
    if (i > s):
        return 0
    else:
       return i + suma_recursiva(i+1,s) 

print(suma_recursiva(0,100))