alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def codifica(texto, desplazam, direccion):
    cifrado=""
    if direccion == 'decodifica':
        desplazam *= -1
    for letra in texto:
        posicion= alfabeto.index(letra)
        nuevaposicion=(posicion+desplazam)%27
        nuevaletra=alfabeto[nuevaposicion]
        cifrado+=nuevaletra
    print(f'El texto codificado es {cifrado}')
'''
def codifica(texto, desplazam):
    cifrado=""
    for letra in texto:
        posicion= alfabeto.index(letra)
        nuevaposicion=(posicion+desplazam)%27
        nuevaletra=alfabeto[nuevaposicion]
        cifrado+=nuevaletra
    print(f'El texto codificado es {cifrado}')
def decodifica(texto, desplazam):
    cifrado=""
    for letra in texto:
        posicion= alfabeto.index(letra)
        nuevaposicion=(posicion-desplazam)%27
        nuevaletra=alfabeto[nuevaposicion]
        cifrado+=nuevaletra
    print(f'El texto codificado es {cifrado}')
'''
direccion = input("Escribe 'codifica' para codificar o 'decodifica' para decodificar: ")
texto = input("Escribe tu mensaje: ").lower()
desplazam = int(input("Escribe un número para el desplazamiento: "))
codifica(texto,desplazam,direccion)
'''
if direccion == 'codifica':
    codifica(texto,desplazam)
elif direccion == 'decodifica':
    decodifica(texto,desplazam)
'''
#TODO-1: Crea una funcion llamada 'codifica' que coja el 'texto' y 'desplazamiento' como entradas.

    #TODO-2: Dentro de la función 'codifica', desplaza cada letra del 'texto' hacia adelante en el alfabeto
    # la cantidad desplazam e imprime el texto codificado.  
    #ejemplo: 
    #texto_plano = "hola"
    #desplazamiento = 5
    #texto_cifrado = "mtqf"
    #print output: "El texto codificado es mtqf"
# Ayuda: indice de una lista en Python: https://www.w3schools.com/python/ref_list_index.asp  

#TODO-3: Llama a la función codifica y pasa lo que ha introducido el usuario. 
# Deberías ser capaz de probar el código y codificar un mensaje. 