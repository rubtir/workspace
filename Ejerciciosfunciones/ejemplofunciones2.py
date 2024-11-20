def min(a, b):
    if a < b:
        print(f'El mínimo es: {a}')
    elif a >b:
        print(f'El mínimo es: {a}')
    else:
        print('Los dos números son iguales')
a = int(input('Introduce el número 1: '))
b = int(input('Introduce el número 2: '))
min(a,b)