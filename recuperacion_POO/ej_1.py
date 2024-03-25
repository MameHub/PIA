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

class Dice:
    def __init__(self, *faces):
        if len(faces) != 6:
            raise ValueError('El dado debe tener al menos dos caras')
        self.faces = faces

    @property
    def sides(self):
        return self.faces
    
    def roll(self):
        import random as rd
        self.side = rd.choice(self.faces)
        return self.side