"""
Crea una biblioteca de funciones numéricas que contenga las siguientes funciones. Recuerda que puedes usar unas dentro
de otras si es necesario.
Observa bien lo que hace cada función ya que, si las implementas en el orden adecuado, te puedes ahorrar mucho trabajo.
Por ejemplo, la función is_palindromic() resulta trivial teniendo turn() y la función next_prime() también es muy fácil
de implementar teniendo is_prime().
Está prohibido usar funciones de conversión del número a una cadena.
· is_palindromic: devuelve verdadero si el número que se pasa como parámetro es capicúa y falso en caso contrario.
· is_prime: devuelve verdadero si el número que se pasa como parámetro es primo y falso en caso contrario.
· next_prime: devuelve el menor primo que es mayor al número que se pasa como parámetro.
· digits: devuelve el número de dígitos de un número entero.
· turn: le da la vuelta a un número.
· digit_n: devuelve el dígito que está en la posición n de un número entero. Se empieza contando por el 0 y de izquierda
a derecha.
· digit_position: da la posición de la primera ocurrencia de un dígito dentro de un número entero. Si no se encuentra,
devuelve -1.
· remove_behind: le quita a un número n dígitos por detrás (por la derecha).
· remove_ahead: le quita a un número n dígitos por delante (por la izquierda).
· paste_behind: añade un dígito a un número por detrás.
· paste_ahead: añade un dígito a un número por delante.
· piece_of_number: toma como parámetros las posiciones inicial y final dentro de un número y devuelve el trozo
correspondiente.
· put_numbers_together: pega dos números para formar uno.
Haz el programa de manera que al ejecutarse pruebe cada una de las funciones.
"""


def is_palindromic(n):

    capicua = False
    number = n
    turn(n)

    if number == n:
        capicua = True

    return capicua


def is_prime(n):

    prime = False

    for i in range(n):

        if (i+1) % n == 0:
            prime = True

    return prime

#def next_prime():


def digits(n):
    number = n

    for digit in number:
        print(digit)


def turn(n):

    number = str(n)
    inverter = ''

    for digit in reversed(number):
        inverter += digit

    return inverter


print(is_palindromic(122))

# def digit_n():


# def digit_position():


# def remove_behind():


# def remove_ahead():


# def paste_behind():


# def paste_ahead():


# def piece_of_number():


# def put_numbers_together():