"""
Crea una clase, y pruébala, que modele fracciones. Debe permitir:
    · Crear fracciones indicando numerador y denominador.
        · Ejemplo: f = Fraction(2, 3)
        · Ojo!!! No se puede tener un denominador cero.
    · Las fracciones pueden operar entre sí.
        · Sumar, multiplicar, dividir, restar.
        · Ojo!!! esto se puede hacer: f + 1,5 * f
    · Las fracciones se pueden comparar.
        · = =, <, < =, >, > =, ! =
        · Ojo!!! estas dos fracciones son iguales: 1/2 y 2/4
        · Ojo!!! esto se puede hacer 1 < 1/2
"""


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ZeroDivisionError("No se puede realizar una división entre 0")
        self._numerator = numerator
        self._denominator = denominator

    @property
    def numerador(self):
        return self._numerador

    @numerator.setter
    def numerator(self, value):
        self._numerator = value

