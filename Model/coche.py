from motor import Motor

class Coche:
    """
    Clase que representa un coche con atributos básicos y un motor (composición).
    """

    def __init__(self, marca, modelo, año, motor=None):
        """
        Constructor de la clase Coche.
        :param marca: Marca del coche.
        :param modelo: Modelo del coche.
        :param año: Año de fabricación.
        :param motor: Objeto Motor asociado al coche.
        """
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.motor = motor

    def get_marca(self):
        """Devuelve la marca del coche."""
        return self.__marca

    def set_marca(self, marca):
        """Establece la marca del coche."""
        self.__marca = marca

    def get_modelo(self):
        """Devuelve el modelo del coche."""
        return self.__modelo

    def set_modelo(self, modelo):
        """Establece el modelo del coche."""
        self.__modelo = modelo

    def get_año(self):
        """Devuelve el año del coche."""
        return self.__año

    def set_año(self, año):
        """Establece el año del coche."""
        self.__año = año

    def describir(self):
        """Imprime una descripción del coche, incluyendo detalles del motor si está presente."""
        info = f"Coche: {self.__marca} {self.__modelo}, Año: {self.__año}"
        if self.motor:
            info += f", Motor: {self.motor.potencia} HP, Tipo: {self.motor.tipo}"
        print(info)

    def acelerar(self, incremento):
        """
        Método de aceleración básico.
        :param incremento: Valor a aumentar en la velocidad.
        """
        print(f"El coche acelera en {incremento} km/h (versión básica)")

    def incrementarVelocidad(self, incremento):
        """
        Aumenta la velocidad del coche y lanza una excepción si se supera el límite.
        :param incremento: Valor a incrementar.
        :raises ExcesoVelocidadException: Si la velocidad supera los 200 km/h.
        """
        if not hasattr(self, 'velocidad'):
            self.velocidad = 0
        self.velocidad += incremento
        from excepciones import ExcesoVelocidadException
        if self.velocidad > 200:
            raise ExcesoVelocidadException(f"Exceso de velocidad: {self.velocidad} km/h (límite 200 km/h)")
        print(f"Velocidad actual del coche: {self.velocidad} km/h")




