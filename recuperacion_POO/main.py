'''
1. Crea una clase que modele un dado (Dice) de manera que:

    · El constructor recibe los valores de las caras que tiene el dado. Ejemplo:
        · dice1 = Dice(1, 2, 3, 4, 5, 6)
        · dice2 = Dice('A', 'K', 'Q', 'J', `R`, 'N')
    · Los valores de las caras los obtendremos mediante una propiedad (sides).
    · Dispondremos de un método para tirar el dado (roll) que devolverá el resultado (uno de los valores anteriores), además actualizará una variable
    de instancia privada (side)
    que podrá consultarse mediante una propiedad.
    · Los métodos mágicos __str__() y __repr__() deben de estar cerrados.
    · Puedo usar los operadores == y != para comparar dos dados.
'''

import random as rd

class Dice:
    def __init__(self, *side):
        self.side = side

    @property
    def sides(self):
        return self.side
    
    def roll(self):
        self.side = rd.choice(self.side)
        return self.side
    
    def __str__(self):
        return f'El dado tiene la siguiente cara: {self.side}'
    
    def __repr__(self):
        return f'Dice({self.side})'
    
    def __eq__(self, other):
        return self.side == other.side
    
    def __ne__(self, other):
        return self.side != other.side

'''
2. Crea una clase que modele un dado de póker (PokerDice) de manera que:

    · Los posibles valores del dado son 'A', 'K', 'Q', 'J', 'R' y 'N'.
    · El dado tiene una propiedad (score) que nos da la puntuación del dado (6, 5, 4, 3, 2, 1).
'''

class PokerDice:
    def __init__(self):
        self.values = ['A', 'K', 'Q', 'J', 'R', 'N']
        self.scores = {'A': 6, 'K': 5, 'Q': 4, 'J': 3, 'R': 2, 'N': 1}
        self.current_value = None
        self.current_score = None

    @property
    def value(self):
        return self.current_value

    @property
    def score(self):
        return self.current_score
    
    def roll(self):
        self.current_value = rd.choice(self.values)
        self.current_score = self.scores[self.current_value]
        return self.current_score

'''
3. Crea una clase que modele un dado de parchís (LudoDice) que derive de la clase del apartado 1. Un dado de parchís tiene seis caras que van del 1 al 6
(valores enteros). En esta clase:
    · Tendremos la posibilidad de comparar dados entre sí con los operadores relacionados <, <=, > y >=.
'''

class LudoDice(Dice):
    def __init__(self):
        super().__init__(1, 2, 3, 4, 5, 6)

    def __gt__(self, other):
        return "El dado 1 es mayor que el dado 2", self.side > other.side
    
    def __lt__(self, other):
        return "El dado 1 es menor que el dado 2", self.side < other.side
    
    def __ge__(self, other):
        return "El dado 1 es mayor o igual que el dado 2", self.side >= other.side
    
    def __le__(self, other):
        return "El dado 1 es menor o igual que el dado 2", self.side <= other.side

'''
4. Crea una clase que modele un dado de parchís trucado (TrickedLudoDice) que derive de la clase anterior y que de cuando en cuando nos permita poner el valor
que queramos en la cara del dado (entre 1 y 6), de manera que:
    · No puedo usar el método que pone el valor que queramos en la cara del dado (put) si no he tirado al menos tres veces de forma normal, si lo llamo sin
    haberse cumplido esta excepción lanzaremos una excepción.
    · Ten en cuenta que NO PUEDES cambiar directamente el valor de la cara de un dado ya que se almacena en una variable de instancia privada de una clase de
    la que heredas (Dice) y no tienes acceso.
'''

class TrickedLudoDice(LudoDice):
    def __init__(self):
        super().__init__()
        self.rolls = 0
    
    def roll(self):
        self.rolls += 1
        super().roll()

    def put(self, value):
        if self.rolls >= 3:
            self.current_value = value
            self.current_score = self.scores[value]
        else:
            raise ValueError ("Para trucar el dado debes de tirarlo antes 3 veces como mínimo.")

'''
5. Crea una clase que modele un cubilete de dados (DiceCup) de manera que:
    · Al construirla le paso una serie de dados. Ejemplos:
        · cup = DiceCup(LudoDace(), LudoDace(), LudoDace())
    · Dispondremos de una propiedad que devuelva los dados (dices) y otra que devuelva el número de dados que contiene (size).
    · Dispondremos de un método para añadir un dado (add).
    · Dispondremos de un método para quitar un dado (remove) pasándole el dado concreto que queremos quitar.
    · Debes estar creado el método mágico __str__().
'''
 
class DiceCup:
    def __init__(self, *dices):
        self._dices = list(dices)
 
    @property
    def dices(self):
        return self._dices
     
    @property
    def size(self):
        return len(self._dices)
    
    def add(self, dice):
        self._dices.append(dice)
        print(f"Se ha añadio un dado con valor {dice.sides}.")

    def remove(self, dice):
        if dice in self._dices:
            self.dices.remove(dice)
            print(f"Se ha eliminado un dado con valor {dice.sides}.")
        else:
            print("El dado indicado no se encuentra en el cubilete.")
 
    def __str__(self):
        return f"Tenemos un cubilete con {self.size} dados y con valores {self.dices}."

'''
6. Crea una clase que modele un cubilete de dados de póker (PokerDiceCup) que derive de la clase anterior de manera que tenga una
propiedad (score) que devuelva la puntuación total del cubilete (la suma de la de cada dado).
'''

class PokerDiceCup(DiceCup):
    def __init__(self, *dices):
        super().__init__(*dices)

    # @property
    # def score(self):
    #     total = 0
    #     for dice in len(list):
    #         total += dice._dices
    #     return total

    def score(self):
        # total = sum(list)
        return sum(self.dices)
    
# # Pruebas
# print("Ejercicio 1.")
# # Creamos dos dados con los valores de las caras.
# dice1 = Dice(1, 2, 3, 4, 5, 6)
# dice2 = Dice(1, 2, 3, 4, 5, 6)
# # Mostramos las caras de los dados.
# print(f"Dado 1: {dice1.sides}")
# print(f"Dado 2: {dice2.sides}")
# # Tiramos los dados e imprimimos los resultados por pantalla.
# dice1.roll()
# print(f"Dado 1: {str(dice1)}")
# dice2.roll()
# print(f"Dado 2: {repr(dice2)}")
# # Comparación de dados.
# print("Los dados son iguales:", dice1 == dice2)
# print("Los dados son diferentes:", dice1 != dice2)
# print()

# print("Ejercicio 2.")
# # Creamos el dado de poker.
# poker_Dice1 = PokerDice()
# # Realizamos una tirada del dado.
# poker_Dice1.roll()
# # Mostramos la puntuación obtenida.
# print(f"Valor del dado de póker: {poker_Dice1.value}")
# print(f"Puntuación del dado de póker: {poker_Dice1.score}")
# print()

# print("Ejercicio 3.")
# Creamos los dados de parchís.
# ludo_Dice1 = LudoDice()
# ludo_Dice2 = LudoDice()
# Realizamos las tiradas.
# print(f"Dado parchís 1: {ludo_Dice1.roll()}")
# print(f"Dado parchís 2: {ludo_Dice2.roll()}")
# Realizamos las comparaciones.
# print(f"{ludo_Dice1.sides} > {ludo_Dice2.sides}: {ludo_Dice1 > ludo_Dice2}")
# print(f"{ludo_Dice1.sides} < {ludo_Dice2.sides}: {ludo_Dice1 < ludo_Dice2}")
# print(f"{ludo_Dice1.sides} >= {ludo_Dice2.sides}: {ludo_Dice1 >= ludo_Dice2}")
# print(f"{ludo_Dice1.sides} <= {ludo_Dice2.sides}: {ludo_Dice1 <= ludo_Dice2}")
# print()

# print("Ejercicio 4.")
# Creamos el dado de trucado.
# TrickedLudoDice1 = TrickedLudoDice()
# Realizamos las tiradas.
# for i in range(3):
#     TrickedLudoDice1.roll()
#     print(f"Tirada {i+1}: {TrickedLudoDice1.sides}")
# TrickedLudoDice1.roll()
# print(TrickedLudoDice1)
# TrickedLudoDice1.put(3)
# Mostramos el dado.
# print(TrickedLudoDice1)
# # Trucamos el dado y mostramos el resultado.
# for _ in range(3):
#     TrickedLudoDice1.roll()
# TrickedLudoDice1.put(3)
# print(TrickedLudoDice1.value)
# print()

# print("Ejercicio 5.")
# # Creamos tres dados de parchís y tiramos los dados para ver que funcionan.
Ludo_Dice1 = LudoDice()
Ludo_Dice2 = LudoDice()
Ludo_Dice3 = LudoDice()
# Ludo_Dice4 = LudoDice()
print(f"Dado parchís 1: {Ludo_Dice1.roll()}.")
print(f"Dado parchís 2: {Ludo_Dice2.roll()}.")
print(f"Dado parchís 3: {Ludo_Dice3.roll()}.")
# print(f"Dado parchís 4: {Ludo_Dice4.roll()}.")
# # Creamos el cubilete de dados.
DiceCup1 = DiceCup(Ludo_Dice1, Ludo_Dice2, Ludo_Dice3)
print(DiceCup1)
# # Mostramos los dados que tenemos en el cubilete.
# print(f"En el cubilete tenemos los siguientes dados: {DiceCup1.dices}.")
# print(f"Hay {DiceCup1.size} dados en el cubilete.")
# DiceCup1.add(Ludo_Dice4)
# print(DiceCup1.dices)
# print(DiceCup1)
# DiceCup1.remove(Ludo_Dice4)
# print(DiceCup1.dices)
# print(DiceCup1)
# print()

print("Ejercicio 6")
# Realizamos la suma del contenido del cubilete de dados.
pkc = PokerDiceCup(DiceCup1)
score = pkc.score
print(score)