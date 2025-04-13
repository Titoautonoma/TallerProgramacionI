"""
Archivo principal que ejecuta los 10 ejercicios del taller práctico de Programación I.
Se prueba la creación de clases, encapsulamiento, constructores, herencia, polimorfismo,
clases abstractas, interfaces, composición y manejo de excepciones personalizadas.
"""

from coche import Coche
from vehiculos import CocheHerencia, Bicicleta, Vehiculo
from motor import Motor
from excepciones import ExcesoVelocidadException
from animal import Perro, Gato
from volador import Pajaro, Avion

def main():
    """
    Función principal que ejecuta los ejercicios del taller.
    """
    
    # Ejercicios 1, 2 y 3: Clase básica, encapsulamiento, constructores
    print("=== Ejercicio 1, 2 y 3: Clase Coche (Básica, Encapsulamiento y Constructores) ===")
    coche1 = Coche("Toyota", "Corolla", 2020)
    coche2 = Coche("Ford", "Fiesta", 2019)
    coche1.describir()
    coche2.describir()

    print("Modificando marca de coche1:")
    print("Marca original:", coche1.get_marca())
    coche1.set_marca("Honda")
    print("Marca modificada:", coche1.get_marca())

    print("\n=== Ejercicio 3: Constructores (Creando otro coche) ===")
    coche3 = Coche("Chevrolet", "Spark", 2018)
    coche3.describir()

    # Ejercicios 4, 5 y 6: Herencia, sobreescritura, polimorfismo
    print("\n=== Ejercicio 4, 5 y 6: Herencia, Sobreescritura y Polimorfismo ===")
    motor1 = Motor(150, "gasolina")
    cocheH = CocheHerencia("Nissan", "Sentra", 2021, velocidad=50, motor=motor1)
    cocheH.describir()
    cocheH.acelerar(20)

    bici = Bicicleta("Montaña", velocidad=10)
    print("\nBicicleta antes de acelerar:")
    print(f"Velocidad: {bici.velocidad} km/h")
    bici.acelerar(10)
    bici.hacer_caballito()

    # Polimorfismo con lista de objetos
    print("\nPolimorfismo: Lista de Vehículos (CocheHerencia y Bicicleta)")
    vehiculos = [cocheH, bici]
    for v in vehiculos:
        v.acelerar(5)

    # Ejercicio 7: Clases abstractas
    print("\n=== Ejercicio 7: Clases Abstractas ===")
    animales = [Perro(), Gato()]
    for animal in animales:
        animal.hacerSonido()

    # Ejercicio 8: Interfaces
    print("\n=== Ejercicio 8: Interfaces (Volador) ===")
    voladores = [Pajaro(), Avion()]
    for v in voladores:
        v.volar()

    # Ejercicio 9: Composición
    print("\n=== Ejercicio 9: Composición ===")
    coche_con_motor = Coche("Kia", "Rio", 2022, motor=Motor(120, "eléctrico"))
    coche_con_motor.describir()

    # Ejercicio 10: Manejo de excepciones
    print("\n=== Ejercicio 10: Manejo de Excepciones y Clases Personalizadas ===")
    try:
        cocheH.incrementarVelocidad(160)
    except ExcesoVelocidadException as e:
        print("Excepción capturada:", e)

if __name__ == "__main__":
    main()


