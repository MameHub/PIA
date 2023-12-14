"""
Escibe un programa que genere 20 números enteros entre 100 y 999. Estos números se deben introducir en una lista de 4
filas por 5 columnas. El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo
se tratará. La suma total debe aparecer en la esquina inferior derecha.
"""

import random as ran

list = []

for n in range(20):
    list.append(ran.randint(100, 999))

print(list)