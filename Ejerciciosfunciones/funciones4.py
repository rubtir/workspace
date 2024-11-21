def circumferencia(radio):
    area=3.14*radio**2
    perimetro=2*3.14*radio
    print(f'El área es {area} y el perímetro es {perimetro}')
radio= int(input('Dime el radio: '))
circumferencia(radio)