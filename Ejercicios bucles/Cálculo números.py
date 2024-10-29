numeros=int(input('Cuántos números vas a introducir?: '))
numero=int(input('Introduce el número 1:'))
menor=numero
mayor=numero
suma=numero
for i in range(2,numeros+1):
    numero=int(input(f'Dime el número {i}: '))
    suma+=numero
    if numero> mayor:
        mayor=numero
    elif numero< menor:
        menor=numero
print(f'El número más pequeño es: {menor}')
print(f'El número más grande es: {mayor}')
print(f'La media de los numeros es: {suma/numeros}')