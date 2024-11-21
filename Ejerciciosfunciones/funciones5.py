def tiempo_horas(segundos_1):
    min=segundos_1%3600
    hora=(segundos_1-min)/3600
    sec=min%60
    minut=(min-sec)/60
    print(f'Són {hora} horas, {minut} minutos y {sec} segundos')
def tiempo_segundos(horas,minutos,segundos):
    total=horas*3600+minutos*60+segundos
    print(f'Són {total} segundos')
opcion=input('Si quieres que calcule una cantidad de segundos, para dertelo en horas, minutos y segundos di si. Si quieres que te de una cantidad de segundos, a partir de horas, minutos y segundos di otra cosa: ')
if opcion == 'si':
    segundos_1= int(input('Dime los segundos: '))
    tiempo_horas(segundos_1)
else:
    horas= int(input('Dime las horas: '))
    minutos= int(input('Dime los minutos: '))
    segundos= int(input('Dime los segundos: '))
    tiempo_segundos(horas,minutos,segundos)
