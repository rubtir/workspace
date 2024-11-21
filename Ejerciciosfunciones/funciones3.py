def histograma(lista):
    for i in lista:
        print(f'*'*int(i))
lista=input('Dime unos números separados por comas: ').split(',')
histograma(lista)
