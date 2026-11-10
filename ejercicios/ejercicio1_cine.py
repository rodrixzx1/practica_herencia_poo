class Boleto:
    def __init__(self, cliente, funcion, precio_base=90):
        self.cliente = cliente
        self.funcion = funcion
        self.precio_base = precio_base

    def calcular_precio(self):
        return self.precio_base

    def ticket(self):
        return f"{self.cliente} - {self.funcion}: ${self.calcular_precio():,.2f}"


class BoletoEstudiante(Boleto):
    def __init__(self, cliente, funcion):
        super().__init__(cliente, funcion)

    def calcular_precio(self):
        return self.precio_base * 0.70


class BoletoCortesia(Boleto):
    def __init__(self, cliente, funcion):
        super().__init__(cliente, funcion, precio_base=0)

    def calcular_precio(self):
        return 0


# Reto: BoletoTerceraEdad (con 50% de descuento)
class BoletoTerceraEdad(Boleto):
    def __init__(self, cliente, funcion):
        super().__init__(cliente, funcion)

    def calcular_precio(self):
        return self.precio_base * 0.50


# Datos de prueba para exportar
boletos = [
    Boleto("Andrea", "Sala 2, 18:00"),
    BoletoEstudiante("Bruno", "Sala 2, 18:00"),
    BoletoCortesia("Carla", "Sala 5, 20:30"),
    BoletoTerceraEdad("Diana", "Sala 1, 16:00")
]