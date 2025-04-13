from abc import ABC, abstractmethod

class Volador(ABC):
    """
    Interfaz para clases que pueden volar.
    """

    @abstractmethod
    def volar(self):
        """Método que debe ser implementado para definir cómo vuela el objeto."""
        pass


class Pajaro(Volador):
    """Clase concreta que representa un pájaro."""

    def volar(self):
        print("El pájaro vuela alto en el cielo.")


class Avion(Volador):
    """Clase concreta que representa un avión."""

    def volar(self):
        print("El avión despega y vuela a gran velocidad.")
