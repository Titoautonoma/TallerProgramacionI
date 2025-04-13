class Motor:
    """
    Clase que representa un motor para ser usado por un vehículo.
    """

    def __init__(self, potencia, tipo):
        """
        Constructor del motor.
        :param potencia: Potencia del motor en HP.
        :param tipo: Tipo de motor (ej: 'gasolina', 'eléctrico').
        """
        self.potencia = potencia
        self.tipo = tipo
