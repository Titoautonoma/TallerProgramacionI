from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Clase abstracta que define el comportamiento de un animal.
    """

    @abstractmethod
    def hacerSonido(self):
        """Método abstracto que debe implementar el sonido del animal."""
        pass


class Perro(Animal):
    """Clase concreta que representa un perro."""

    def hacerSonido(self):
        print("El perro ladra: ¡Guau, guau!")


class Gato(Animal):
    """Clase concreta que representa un gato."""

    def hacerSonido(self):
        print("El gato maúlla: ¡Miau, miau!")
