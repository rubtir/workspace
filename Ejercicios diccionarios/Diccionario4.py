diccionario = {'a': 100, 'b': 200, 'c': 300}
num = int(input('Dígame un número: '))
if num in diccionario.values():
    print('True')
else:
    print('False')