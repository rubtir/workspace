class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.numero_servido = 0
    def describir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} se especializa en cocina {self.tipo_cocina}.")
    def abrir_restaurante(self):
        print("¡Estamos abiertos! Bienvenidos a disfrutar de nuestros platillos.")
    def establecer_como_servido(self, numero):
        self.numero_servido = numero
        print(f"Número de clientes servidos por {restaurante1.nombre_restaurante}: {restaurante1.numero_servido}")
    def incrementar_numero_servido(self, incremento):
        self.numero_servido += incremento
        print(f"Número de clientes servidos por {restaurante1.nombre_restaurante}: {restaurante1.numero_servido}")
restaurante1 = Restaurante("Italia", "tradicional italiana")
restaurante2 = Restaurante("La creperia", "crepes")
restaurante3 = Restaurante("bigBurger", "Hamburguesas")
restaurante1.describir_restaurante()
restaurante2.describir_restaurante()
restaurante3.describir_restaurante()
restaurante1.establecer_como_servido(20)
restaurante1.incrementar_numero_servido(4)