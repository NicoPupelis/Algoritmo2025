
import random
import string

cola_principal = []

todos_los_caracteres = string.ascii_letters + string.digits + string.punctuation + " "

for _ in range(50000):
    caracter = random.choice(todos_los_caracteres)
    cola_principal.append(caracter)

cola_digitos = []
cola_restantes = []

for caracter in cola_principal:
    if caracter.isdigit():
        cola_digitos.append(caracter)
    else:
        cola_restantes.append(caracter)

cantidad_letras = 0

for caracter in cola_restantes:
    if caracter.isalpha():
        cantidad_letras += 1

tiene_signo_pregunta = False
tiene_numeral = False

for caracter in cola_restantes:
    if caracter == "?":
        tiene_signo_pregunta = True
    if caracter == "#":
        tiene_numeral = True

print("Cantidad de caracteres totales:", len(cola_principal))
print("Cantidad de dígitos:", len(cola_digitos))
print("Cantidad de caracteres no dígitos:", len(cola_restantes))
print("Cantidad de letras en la segunda cola:", cantidad_letras)
print("¿Está el caracter '?':", tiene_signo_pregunta)
print("¿Está el caracter '#':", tiene_numeral)
