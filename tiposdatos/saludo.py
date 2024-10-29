quieres_saludar = 'S' 
NUM_MAX_SALUDOS=4
num_saludos=0
while  quieres_saludar== 'S':
    print('Hola qué tal!')
    num_saludos +=1
    if num_saludos==NUM_MAX_SALUDOS:
     break
    quieres_saludar = input('¿Quiere otro saludo? [S/N] ')
    while quieres_saludar not in ('S','N'):
       print('Hola qué tal!')
       quieres_saludar = input('¿Quiere otro saludo(solo con estas letras? [S/N] ')
print('Que tenga un buen día')