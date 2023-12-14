"""
Escribe un programa que lea 5 números por teclado y que los almacene en una lista. Rota los elementos de esa lista, es
decir, el elemento de la posición 0 debe pasar a la posición 1, el de la 1 a la 2, etc. El número que se encuentra en la
última posición debe pasar a la posición 0. Finalmente, muestra el contenido de la lista.
"""

list = []

for i in range(5):
    list.append(int(input("Introduzca un número: ")))



for i in range(len(list)):
    print(list[i])