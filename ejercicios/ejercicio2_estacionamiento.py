class Estancia:
    def __init__(self, placa, horas):
        # Reto: Validación centralizada de horas
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores que cero")
        self.placa = placa
        self.horas = horas

    def cobrar(self):
        return self.horas * 20

    def ticket(self):
        return f"{self.placa} ({self.horas} h): ${self.cobrar():,.2f}"


class EstanciaPension(Estancia):
    def __init__(self, placa):
        super().__init__(placa, horas=24)

    def cobrar(self):
        return 250


class EstanciaNocturna(Estancia):
    def __init__(self, placa, horas):
        super().__init__(placa, horas)

    def cobrar(self):
        return super().cobrar() + 50


# Datos de prueba para exportar
estancias = [
    Estancia("ABC-123", 3),
    EstanciaPension("XYZ-789"),
    EstanciaNocturna("JKL-456", 5)
]