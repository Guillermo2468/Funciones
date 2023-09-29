import random
import string

def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def siguiente_primo(n):
    primo_siguiente = n + 1
    while True:
        if primo(primo_siguiente):
            return primo_siguiente
        primo_siguiente += 1

def contraseña():
    longitud = random.randint(7, 10)
    caracteres = string.printable[33:94]  # Caracteres de la tabla ASCII entre 33 y 126
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def hipotenusa(lado1, lado2):
    hipotenusa = (lado1**2 + lado2**2)**0.5
    return hipotenusa

def calcular_mediana(a, b, c):
    numeros = [a, b, c]
    numeros.sort()  # Ordenar los números de menor a mayor
    mediana = numeros[1]  # El número del medio es la mediana
    return mediana
