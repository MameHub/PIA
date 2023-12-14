"""
· Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cinco opciones: sumar, restar,
  multiplicar, dividir y terminar. Cada opción llama a una función a la que se le pasan las dos variables y muestra
  el resultado de la operación. Si se introduce una opción incorrecta se muestra un mensaje de error. El menú se
  volverá a mostrar, a menos que no se de a la opción terminar.

· Modifica el programa anterior para que la introducción de las variables sea una opción del menú (la primera).
  Las variables se inicializan a cero.

· Modifica el programa anterior para que si no se introducen las dos variables desde la opción correspondiente no se
  puedan ejecutar el resto de las opciones.

· Crea una función para gestionar menús: recibe una lista de opciones, las muestra numeradas, pide una opción
  (por su número) y devuelve la opción escogida. Modifica el último programa para que use esta función.
"""


def calculator1():
    end = True

    while end:

        n1 = float(input("Introduzca el primer número: "))
        n2 = float(input("Introduzca el segundo número: "))

        option = int(
            input("Introduzca que desea hacer:\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Terminar\n"))

        match option:
            case 1:
                total = n1 + n2
                print(f"El total de la suma es {total:.2f}")
            case 2:
                total = n1 - n2
                print(f"El total de la resta es {total:.2f}")
            case 3:
                total = n1 * n2
                print(f"El total de la multiplicación es {total:.2f}")
            case 4:
                try:
                    total = n1 / n2
                    resto = n1 % n2
                    print(f"El total de la división es {total:.2f} y el resto es {resto:.2f}")
                except ZeroDivisionError:
                    print("No es posible dividir entre 0.")
            case 5:
                end = False


def calculator2():
    end = True
    n1 = 0
    n2 = 0

    while end:

        option = int(
            input("Introduzca que desea hacer:\n1. Introducir números\n2. Sumar\n"
                  "3. Restar\n4. Multiplicar\n5. Dividir\n6. Terminar\n"))

        match option:
            case 1:
                n1 = float(input("Introduzca el primer número: "))
                n2 = float(input("Introduzca el segundo número: "))
            case 2:
                if n1 and n2 == 0:
                    print("Debe de introducir un valor para poder realizar la operación.")
                    break
                else:
                    total = n1 + n2
                    print(f"El total de la suma es {total:.2f}")
            case 3:
                total = n1 - n2
                print(f"El total de la resta es {total:.2f}")
            case 4:
                total = n1 * n2
                print(f"El total de la multiplicación es {total:.2f}")
            case 5:
                try:
                    total = n1 / n2
                    resto = n1 % n2
                    print(f"El total de la división es {total:.2f} y el resto es {resto:.2f}")
                except ZeroDivisionError:
                    print("No es posible dividir entre 0.")
            case 6:
                end = False


def calculator3():
    end = True
    n1, n2 = 0, 0

    while end:

        option = int(
            input("Introduzca que desea hacer:\n1. Introducir números\n2. Sumar\n"
                  "3. Restar\n4. Multiplicar\n5. Dividir\n6. Terminar\n"))

        match option:
            case 1:
                n1 = float(input("Introduzca el primer número: "))
                n2 = float(input("Introduzca el segundo número: "))
            case 2:
                if n1 == 0 and n2 == 0:
                    print("Debe de introducir un valor para poder realizar la operación.")
                    break
                else:
                    total = n1 + n2
                    print(f"El total de la suma es {total:.2f}")
                    n1, n2 = 0, 0
            case 3:
                if n1 == 0 and n2 == 0:
                    print("Debe de introducir un valor para poder realizar la operación.")
                    break
                else:
                    total = n1 - n2
                    print(f"El total de la resta es {total:.2f}")
                    n1, n2 = 0, 0
            case 4:
                if n1 == 0 and n2 == 0:
                    print("Debe de introducir un valor para poder realizar la operación.")
                    break
                else:
                    total = n1 * n2
                    print(f"El total de la multiplicación es {total:.2f}")
                    n1, n2 = 0, 0
            case 5:
                try:
                    if n1 == 0 and n2 == 0:
                        print("Debe de introducir un valor para poder realizar la operación.")
                        break
                    else:
                        total = n1 / n2
                        resto = n1 % n2
                        print(f"El total de la división es {total:.2f} y el resto es {resto:.2f}")
                        n1, n2 = 0, 0
                except ZeroDivisionError:
                    print("No es posible dividir entre 0.")
            case 6:
                end = False


def menu(option_1, option_2, option_3, option_4, option_5, option_6):
    options = [option_1, option_2, option_3, option_4, option_5, option_6]

    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        try:
            selection = int(input("Elige una opción por su número: "))
            if 1 <= selection <= 6:
                return selection
            else:
                print("Opción no válida. Introduce un número válido (1-6).")
        except ValueError:
            print("Por favor, introduce un número válido (1-6).")


def calculator4():
    end = True
    n1 = 0
    n2 = 0

    while end:

        option = menu("introducir valores", "sumar", "restar", "multiplicar", "dividir", "salir",)

        match option:
            case 1:
                n1 = float(input("Introduzca el primer número: "))
                n2 = float(input("Introduzca el segundo número: "))
            case 2:
                total = n1 + n2
                print(f"El total de la suma es {total:.2f}")
            case 3:
                total = n1 - n2
                print(f"El total de la resta es {total:.2f}")
            case 4:
                total = n1 * n2
                print(f"El total de la multiplicación es {total:.2f}")
            case 5:
                try:
                    total = n1 / n2
                    resto = n1 % n2
                    print(f"El total de la división es {total:.2f} y el resto es {resto:.2f}")
                except ZeroDivisionError:
                    print("No es posible dividir entre 0.")
            case 6:
                end = False


calculator4()
