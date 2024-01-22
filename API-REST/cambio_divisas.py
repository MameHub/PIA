import requests as rq
import json as js

def mostrar_divisas():
    url = "https://v6.exchangerate-api.com/v6/ca0d56370e78ee22cd687def/latest/EUR"
    dic_divisas = js.loads(url)

url = "https://v6.exchangerate-api.com/v6/ca0d56370e78ee22cd687def/latest/EUR"
headers = {}
payload = {}
response = rq.request('GET', url, headers=headers, data=payload)
dicc_div = {response.text}
print(response.text)
print(dicc_div)