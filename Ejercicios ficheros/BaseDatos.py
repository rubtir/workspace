# Proyecto sobre estructuras de datos en python: Listas, tuplas, usuarioss y conjuntos 
# Sistema de Bases de Datos para almacenar información de usuarios
# En este proyecto usarás listas y usuarioss
# Partiremos de la definición del usuarios para almacenar la base de datos (usuarios).
# De cada usuario se guardará su apellido y 4 campos: nombre, ocupacion, aficiones y edad

#Empieza definiendo el usuarios "usuarios"
usuarios={
    'Tirado':{
        'Nombre':'Rubén',
        'Ocupación': 'Estudiante',
        'Aficiones':['Peliculas', 'Videojuegos','Mates'],
        'Edad':17
    }
}
# A continuación habrá un bucle en donde se evalúe la entrada del usuario 
# Dentro del bucle se le darán al usuario 4 opciones: listar usuarios, añadir un usuario, borrar un usuario, buscar un usuario
# Dependiendo de lo que conteste el usuario se hará lo que dice esa opción.

while True:
    elige_opcion = input("1 - listar usuarios, 2 - añadir un usuario, 3 - borrar un usuario, 4 - buscar un usuario, 5 - guardar en el fichero, 6 - salir: ")
    match elige_opcion:
        case '1':
            print('Listado de todos los usuarios')
            print(f'{usuarios}')
        case '2':
            apellido=input('Di el apellido del usuario: ')
            if apellido in usuarios:
                print('El usuario ya existe')
            else:
                nombre = input('Di el nombre del usuario: ')
                ocupacion=input('Di la ocupación del usuario: ')
                Aficiones=input('Di las aficiones del usuario separadas pr comas: '). split(',')
                edad =input('Di la edad del usuario: ')
                usuarios[apellido]= {
                    'Nombre':nombre,
                    'Ocupación': ocupacion,
                    'Aficiones':Aficiones,
                    'Edad':edad                   
                }
        case '3':
            borrar= input('Que usuario deseas borrar: ')
            if borrar in usuarios:
                del usuarios[borrar]
            else:
                print('Este usuario no está')
        case '4':
            buscar = input ('Que usuario deseas buscar: ')
            if buscar in usuarios:
                print(f'{usuarios[buscar]}')
            else:
                print('No está este usuario')
        case '5':
            
        case '6':
            break