def es_primo(numero):
    # Caso especial para números menores o iguales a 1
    if numero <= 1:
        return False
    
    # Comprobar divisibilidad desde 2 hasta la mitad del número
    for i in range(2, numero // 2 + 1):
        if numero % i == 0:
            return False
    
    return True

def es_compuesto(numero):
    # Un número es compuesto si no es primo
    return not es_primo(numero)

# Ejemplo de uso
numero = int(input('Ingrese el numero: '))
if es_compuesto(numero):
    print(f'{numero} es un número compuesto')
else:
    print(f'{numero} no es un número compuesto')
