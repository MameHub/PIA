import requests

API_KEY = "ca0d56370e78ee22cd687def"
coin_source = ""
coin_target = ""
quantity = ""
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{coin_source}/{coin_target}/{quantity}"

coin_source = input("Introduzca la divisa origen: ")
coin_target = input("Introduzca la divisa objetivo: ")
quantity = input("Introduzca la cantidad a convertir: ")


payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

def main():
    print("Aplicación para el cambio de divisas")
    print("Divisas:\n")