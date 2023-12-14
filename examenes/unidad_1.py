# Autor: Álvaro Cañas

def pitagoras(x1, x2, y1, y2):

    result = (((x2-x1)**2)+((y2-y1)**2))**0.5

    return result


points = [
    ((2, 3), 1),
    ((4, 2), 1),
    ((3, 5), 2),
    ((6, 3), 2),
    ((5, 1), 1),
    ((4, 4), )
]

# point = (4, 4)

# print(f"Lista completa de puntos y sus clases: {points}")
# print(f"Solo punto y clase: {points[2]}")
# print(f"Solo punto: {points[2][0]}")
# print(f"Dos puntos: {points[0][0], points[1][0]}")
# print(f"La distancia entre el punto {points[0][0]} y el punto {points[1][0]} es de "
#       f"{pitagoras(points[0][0], points[1][0]):.2f}")
print(f"La distancia entre el punto {points[0][0]} y el punto {points[5][0]} es de "
      f"{pitagoras(points[0][0][0], points[5][0][0], points[0][0][1], points[5][0][1])}")