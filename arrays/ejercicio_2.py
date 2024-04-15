"""
Haz el ejercicio anterior usando numpy y aprovechando sus ventajas.
"""

import numpy as np

number = np.random.randint(0, 101, 20)
square = np.square(number)
cube = np.power(number, 3)

number_list = number.tolist()
square_list = square.tolist()
cube_list = cube.tolist()

columns = zip(number_list, square_list, cube_list)

for num in columns:
    print(f"{num[0]}\t{num[1]}\t{num[2]}")
