"""
author: Álvaro Cañas
date: 2024-03-06

El FBI tiene un recorte de personal informático y solicitan nuestra ayuda, quieren saber cuantos fugitivos
tienen registrados en cada una de sus oficinas, para ello han habilitado una API a la que puedes acceder
desde aqui: https://www.fbi.gov/wanted/api

El programa debe mostrar el nombre de cada oficina (ordenado) y la cantidad de fugitivos registrados.
También debe mostrar la cantidad de fugitivos no registrados en ninguna oficina.

Ten en cuenta que cada consulta muestra un número limitado de registros, vas a tener que hacer consultas
iterativas enviando como parámetro la página de la consulta hasta que ya no queden páginas que consultar.
"""

import requests as rq
import json as js


response = rq.get('https://api.fbi.gov/wanted/v1/list')
data = js.loads(response.content)
print(data['total'])
print(data['items'][0]['title'])