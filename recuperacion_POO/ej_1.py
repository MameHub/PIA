'''
Crea una clase que modele un dado (Dice) de manera que:

    · El constructor recibe los valores de las caras que tiene le dado. Ejemplo:
        · dice1 = Dice(1, 2, 3, 4, 5, 6)
        · dice2 = Dice('A', 'K', 'Q', 'J', `R`, 'N')
    · Los valores de las caras los obtendremos mediante una propiedad (sides).
    · Dispondremos de un método para tirar el dado (roll) que devolverá el resultado (uno de los valores anteriores), además actualizará una variable de instancia privada (side)
    que podrá consultarse mediante una propiedad.
    · Los métodos mágicos __str__() y __repr__() deben de estar cerrados.
    · Puedo usar los operadores == y != para comparar dos dados.
'''

# Creamos la clase Dice, esta no tendrá permitido introducir un número de caras que no sea igual a 6.
class Dice:
    def __init__(self, *side):
        if len(side) != 6:
            raise ValueError('El dado debe tener al menos dos caras')
        self.side = side

    # Propiedad para obtener las caras del dado.
    @property
    def sides(self):
        return self.side
    
    # Método para tirar el dado y obtener un valor de cualquiera de sus caras.
    def roll(self):
        import random as rd
        self.side = rd.choice(self.side)
        return self.side
    
    # Método mágico __str__().
    def __str__(self):
        return f'El dado tiene las siguientes caras: {self.side}'
    
    # Método mágico __repr__().
    def __repr__(self):
        return f'Dice({self.side})'
    
    # Método de comparacións.
    # Metodo mágico __eq__().
    def __eq__(self, other):
        return self.side == other.side
    
    # Método mágico __ne__().
    def __ne__(self, other):
        return self.side != other.side

# Creamos dos dados con los valores de las caras.
dice1 = Dice(1, 2, 3, 4, 5, 6)
dice2 = Dice(1, 2, 3, 4, 5, 6)
# Mostramos las caras de los dados.
print(f"Dado 1: {dice1.sides}")
print(f"Dado 2: {dice2.sides}")
# Tiramos los dados e imprimimos los resultados por pantalla.
print(f"Dado 1: {dice1.roll()}")
print(f"Dado 2: {dice2.roll()}")
# Comparación de dados.
print(dice1 == dice2)
print(dice1 != dice2)