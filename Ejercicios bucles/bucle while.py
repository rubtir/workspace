import random
valor_minimo= int(input('Introduce el valor mínimo: '))
valor_maximo= int(input('Introduce el valor máximo: '))
secreto = random.randint(valor_minimo,valor_maximo)
print(f'A ver si adivinas un número entre {valor_minimo} y {valor_maximo}')
intentos=1
num= int(input('Escribe un número: '))
while num!= secreto:
    if num < secreto:
        num= int(input('Demasiado pequeño, di otro: '))
    elif num > secreto:
        num= int(input('Demasiado grande, di otro: '))
    intentos+=1
print(f'Lo acertaste en {intentos}')