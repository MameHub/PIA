"""
Crea una función que reciba un número, lo convierta al sistema Morse y lo devuelve en una cadena de caracteres.
Por ejemplo, el 213 es el ..___ .____ ...__ en Morse. Utiliza esta función en un programa para comprobar quefunciona
bien.
Desde la función no se debe mostrar nada por pantalla, solo se debe usar print desde el programa principal.
Los números en Morse los puedes encontrar aquí: https://morsecw.com/alfabeto.html#numeros.
"""


def to_morse(number):
    to_convert = str(number)
    morse_result = ''
    MORSE_1 = ".----"
    MORSE_2 = "..---"
    MORSE_3 = "...--"
    MORSE_4 = "....-"
    MORSE_5 = "....."
    MORSE_6 = "-...."
    MORSE_7 = "--..."
    MORSE_8 = "---.."
    MORSE_9 = "----."
    MORSE_0 = "-----"

    for digit in to_convert:

        morse_result += ' '

        if digit == '1':
            morse_result += MORSE_1
        elif digit == '2':
            morse_result += MORSE_2
        elif digit == '3':
            morse_result += MORSE_3
        elif digit == '4':
            morse_result += MORSE_4
        elif digit == '5':
            morse_result += MORSE_5
        elif digit == '6':
            morse_result += MORSE_6
        elif digit == '7':
            morse_result += MORSE_7
        elif digit == '8':
            morse_result += MORSE_8
        elif digit == '9':
            morse_result += MORSE_9
        elif digit == '0':
            morse_result += MORSE_0

    return morse_result


morse_code = to_morse(231)
print(morse_code)
