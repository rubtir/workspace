def LeerFecha():
    dia = int(input("Introduce el día: "))
    mes = int(input("Introduce el mes: "))
    año = int(input("Introduce el año: "))
    return dia, mes, año 
def DiasDelMes(mes, año):
    if mes in (1, 3, 5, 7, 8, 10, 12):
        return 31 
    elif mes in (4, 6, 9, 11):
        return 30 
    elif mes == 2: 
        if EsBisiesto(año): 
            return 29 
        else: 
            return 28 
def EsBisiesto(año):
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0) 
def Calcular_Dia_Juliano(dia, mes, año):
    dias_transcurridos = dia 
    for m in range(1, mes):
        dias_transcurridos += DiasDelMes(m, año) 
    return dias_transcurridos  
dia, mes, año = LeerFecha() 
dia_juliano = Calcular_Dia_Juliano(dia, mes, año) 
print(f"El día juliano es: {dia_juliano}")
