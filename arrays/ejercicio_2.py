"""
Haz el ejercicio anterior usando numpy y aprovechando sus ventajas.
"""

import numpy as np

number = np.array([])
square = np.array([])
cube = np.array([])

number = np.random.randint(0, 101, 20)
square = np.square(number)
cube = np.power(number, 3)

print(number)
print(square)
print(cube)
