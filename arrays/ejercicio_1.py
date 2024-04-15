"""
Define tres listas de 20 números enteros cada uno, con nombres number, square y cube. Carga la lista number con valores
aleatorios entre 0 y 100. En la lista square se deben almacenar los cuadrados de los valores que hay en number. En la
lista cube se deben almacenar los cubos de los valores que hay en number. A continuación, muestra el contenido de las
tres listas dispuesto en tres columnas.
"""
import random as ran

number = []
square = []
cube = []

for i in range(20):
    number.append(ran.randint(0, 100))

square = [n**2 for n in number]
cube = [n**3 for n in number]

columns = zip(number, square, cube)

for num in columns:
    print(f"{num[0]}\t{num[1]}\t{num[2]}")
