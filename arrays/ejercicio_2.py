"""
Haz el ejercicio anterior usando numpy y aprovechando sus ventajas.
"""

import numpy as np

number = np.array([np.random.randint(0, 101, 20)])
square = np.array([np.square(number)])
cube = np.array([np.power(number, 3)])

print(number)
print(square)
print(cube)
