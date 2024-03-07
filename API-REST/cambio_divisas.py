"""
author: Álvaro Cañas

Enunciado:
Queremos hacer una aplicación que sea capaz de convertir una cantidad de dinero en una moneda a otra moneda,
para ello haremos uso de la API descrita aquí: https://www.exchangerate-api.com/

Al usuario/a le pediremos:

· La moneda desde la que queremos la conversión.
· La moneda a la que queremos convertir.
· La cantidad de dinero que tenemos.

A tener en cuenta:

· Si la consulta da un error hay que indicarlo.
· Al usuario se le mostrarán las diferentes unidades de moneda antes de pedir los datos, estas se pueden obtener
mediante consulta en esta misma API: https://www.exchangerate-api.com/docs/supported-codes-endpoint.
"""

# Importamos la librería requests para realizar las peticiones a la API y json para tratar los datos.
import requests as rq
import json as js

# Método para obtener todas las divisas disponibles mediante la API.
def currencies():
    url = "https://v6.exchangerate-api.com/v6/ca0d56370e78ee22cd687def/codes"
    response = rq.get(url)
    codes = js.loads(response.text)["supported_codes"]
    for code in codes:
        print(code)

# Método para mostrar las opciones del programa.
def menu():
    print("#"*120)
    print("Bienvenido al conversor de divisas.")
    print("A continuación se mostrarán las divisas y su código, deberá de introducir esta última para indicar el cambio.")
    currencies()
    print("#"*120)

# Método para obtener el cambio de divisas.
def foreing_exchange():
    currency_from = input("Introduzca la divisa que desea cambiar: ").upper()
    currency_to = input("Introduzca a que divisa desea cambiar: ").upper()
    amount = float(input("Introduzca la cantidad que desea cambiar: "))
    url = f"https://v6.exchangerate-api.com/v6/ca0d56370e78ee22cd687def/pair/{currency_from}/{currency_to}/{amount}"
    response = rq.get(url)
    conversion = js.loads(response.text)["conversion_result"]
    print(f"{amount} {currency_from} son {conversion:.2f} {currency_to}")

# Llamada a los métodos.
menu()
foreing_exchange()