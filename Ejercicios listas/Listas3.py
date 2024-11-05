cantidad=int(input('Dígame cuántas palabras tiene la lista: '))
nom=[]
for i in range (1,cantidad+1):
    nombre=input(f'Dígame la palabra {i}: ')
    nom.append(nombre)
print(f'La lista creada es: {nom}')   
print(f'La lista ordenada es: {sorted(nom)} ')