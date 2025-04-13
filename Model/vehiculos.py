from excepciones import ExcesoVelocidadException

class Vehiculo:
    """
    Clase base para representar un vehículo genérico.
    """

    def __init__(self, velocidad=0):
        """
        Constructor de Vehiculo.
        :param velocidad: Velocidad inicial del vehículo.
        """
        self.velocidad = velocidad

    def acelerar(self, incremento):
        """
        Aumenta la velocidad del vehículo.
        :param incremento: Valor a aumentar.
        """
        self.velocidad += incremento
        print(f"Velocidad actual: {self.velocidad} km/h (Vehiculo)")


class CocheHerencia(Vehiculo):
    """
    Clase que hereda de Vehiculo y representa un coche más completo.
    """

    def __init__(self, marca, modelo, año, velocidad=0, motor=None):
        """
        Constructor de CocheHerencia.
        :param marca: Marca del coche.
        :param modelo: Modelo del coche.
        :param año: Año de fabricación.
        :param velocidad: Velocidad inicial.
        :param motor: Objeto motor asociado.
        """
        super().__init__(velocidad)
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.motor = motor

    def describir(self):
        """Imprime una descripción del coche con su velocidad y motor."""
        info = (f"CocheHerencia: {self.__marca} {self.__modelo}, Año: {self.__año}, "
                f"Velocidad: {self.velocidad} km/h")
        if self.motor:
            info += f", Motor: {self.motor.potencia} HP, Tipo: {self.motor.tipo}"
        print(info)

    def acelerar(self, incremento):
        """
        Aumenta la velocidad con un 10% adicional.
        :param incremento: Valor base del incremento.
        """
        self.velocidad += incremento * 1.1
        print(f"El coche acelera a {self.velocidad:.1f} km/h (sobreescritura en CocheHerencia)")

    def incrementarVelocidad(self, incremento):
        """
        Aumenta la velocidad y lanza una excepción si supera el límite.
        :param incremento: Valor a aumentar.
        """
        self.velocidad += incremento
        if self.velocidad > 200:
            raise ExcesoVelocidadException(f"Exceso de velocidad: {self.velocidad} km/h (límite 200 km/h)")
        print(f"Velocidad del coche: {self.velocidad} km/h")


class Bicicleta(Vehiculo):
    """
    Clase que representa una bicicleta y hereda de Vehiculo.
    """

    def __init__(self, tipo, velocidad=0):
        """
        Constructor de Bicicleta.
        :param tipo: Tipo de bicicleta (ej. montaña, ruta).
        :param velocidad: Velocidad inicial.
        """
        super().__init__(velocidad)
        self.tipo = tipo

    def acelerar(self, incremento):
        """
        Aumenta la velocidad con un 80% del incremento.
        :param incremento: Valor base del incremento.
        """
        self.velocidad += incremento * 0.8
        print(f"La bicicleta acelera a {self.velocidad:.1f} km/h")

    def hacer_caballito(self):
        """Realiza una maniobra de caballito."""
        print("¡La bicicleta hace un caballito!")
