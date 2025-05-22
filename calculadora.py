def sumar(a, b):
    """Función que suma dos números"""
    return a + b

def restar(a, b):
    """Función que resta dos números"""
    return a - b

def multiplicar(a, b):
    """Función que multiplica dos números"""
    return a * b

def dividir(a, b):
    """Función que divide dos números"""
    if b==0:
        print("La variable b no puede ser cero")
    else:
        return a / b



resultado1=sumar(5,3)
print(resultado1)

resultado2=restar(5,3)
print(resultado2)