#Programa para calcular tu IMC
masa=float(input('Introduce tu masa: '))
altura=float(input('Introduce tu altura(si hay decimales pon punto en vez de coma): '))
IMC=round((masa/altura**2),2)
print(f"Tu IMC es de {IMC}")
if(IMC<18.5):
    print("Tienes insuficiencia ponderal")
elif(18.5<IMC<24.9):
    print("Tienes un índice de masa corporal normal ")
elif(24.9<IMC<29.9):
    print("Tienes sobrepeso")
else:
    print("Tienes obesidad")