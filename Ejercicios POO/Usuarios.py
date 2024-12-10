class Usuario:
    def __init__(self, nombre, apellido, email, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.edad = edad
        self.intentos_inicio = 0

    def describir_usuario(self):
        print(f"Usuario: {self.nombre} {self.apellido}, Email: {self.email}, Edad: {self.edad}")

    def saludar_usuario(self):
        print(f"Hola, {self.nombre}! Bienvenido/a.")

    def incrementar_intentos_inicio(self):
        self.intentos_inicio += 1
        print(f"Los intentos de inicio de sesión de {usuario1.nombre} son: {usuario1.intentos_inicio}")
    def restablecer_intentos_inicio(self):
        self.intentos_inicio = 0
        print(f"Intentos restablecids a {usuario1.intentos_inicio}")
usuario1 = Usuario("Raúl", "Pérez", "r.perez@gmail.com", 30)
usuario2 = Usuario("Luis", "García", "luis.garcia@gmail.com", 25)
usuario3 = Usuario("Silia", "Rodríguez", "marta.rodriguez@gmail.com", 28)

usuario1.describir_usuario()
usuario1.saludar_usuario()

usuario2.describir_usuario()
usuario2.saludar_usuario()

usuario3.describir_usuario()
usuario3.saludar_usuario()

usuario1.incrementar_intentos_inicio()
usuario1.incrementar_intentos_inicio()
usuario1.incrementar_intentos_inicio()
usuario1.restablecer_intentos_inicio()
