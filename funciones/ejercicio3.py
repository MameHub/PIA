"""
Crea una función que reciba un número, lo convierta al sistema de palotes y lo devuelva en una cadena de caracteres.
Por ejemplo, el 470213 en decimal es el | | | | - | | | | | | | - - | | - | - | | | en el sistema de palotes.
Utiliza esta función en un programa para comprobar que funciona bien. Desde la función no se debe mostrar nada por
pantalla, solo se debe usar print desde el programa principal.
"""


def to_sticks(number):
    to_convert = str(number)
    sticks_result = ''
    STICKS_1 = "|"
    STICKS_2 = "||"
    STICKS_3 = "|||"
    STICKS_4 = "||||"
    STICKS_5 = "|||||"
    STICKS_6 = "||||||"
    STICKS_7 = "|||||||"
    STICKS_8 = "||||||||"
    STICKS_9 = "|||||||||"
    STICKS_0 = ""

    for digit in to_convert:

        sticks_result += ' - '

        if digit == '1':
            sticks_result += STICKS_1
        elif digit == '2':
            sticks_result += STICKS_2
        elif digit == '3':
            sticks_result += STICKS_3
        elif digit == '4':
            sticks_result += STICKS_4
        elif digit == '5':
            sticks_result += STICKS_5
        elif digit == '6':
            sticks_result += STICKS_6
        elif digit == '7':
            sticks_result += STICKS_7
        elif digit == '8':
            sticks_result += STICKS_8
        elif digit == '9':
            sticks_result += STICKS_9
        elif digit == '0':
            sticks_result += STICKS_0

    return sticks_result


sticks_code = to_sticks(942014630)
print(sticks_code)
