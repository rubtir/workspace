def login(usuario,contraseña):
    intentos = 0
    while usuario != 'usuario1' or contraseña != 'asdasd':
        intentos += 1
        print('Prueba otra vez')
        usuario=input('Di el usuario: ')
        contraseña=input('Di la contraseña: ')
    print(f'El usuario y contraseña son correctos, has tardado {intentos} intentos')
usuario=input('Di el usuario: ')
contraseña=input('Di la contraseña: ')
login(usuario,contraseña)