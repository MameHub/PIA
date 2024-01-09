"""
Escribe un programa que genere 20 números enteros aleatorios entre 0 y 100 y que los almacene en un array de numpy. El
programa debe ser capaz de pasar todos los números pares a las primeras posiciones del array (del 0 en adelante) y todos
los números impares a las celdas restantes. Utiliza arrays auxiliares si es necesario.
"""

import numpy as np

arr = np.array([np.random.randint(0, 101, 20)])
number = np.array([])
pairs = np.array([])
odd = np.array([])

print(arr)

for n in arr:
    if n % 2 == 0:
        pairs = np.append(pairs, [n])
    else:
        odd = np.append(odd, [n])

print(pairs)
print(odd)

number = np.concatenate((pairs, odd))
print(number)

