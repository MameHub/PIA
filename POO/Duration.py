"""
En Python existen clases para manipular duraciones de tiempo (horas:minutos:segundos), pero no nos gustan, vamos a hacer
una nueva que se llamará Duration y será inmutable. Debe permitir:

· Crear duraciones de tiempos.
    · Ejemplo: t = Duration(10,20,56)
    · Ojo!!! (10, 62, 15) se debe guardar como (11, 2, 15)
    · Si no indico la hora, minuto o segundoestos valores son cero:
        · Duration() -> (0, 0, 0)
        · Duration(34) -> (34, 0, 0)
        · Duration(34, 15) -> (34, 15, 0)
        · Duration(34, 61) -> (35, 1, 0)
    · Las duraciones de tiempo se pueden comparar.
    · A las duraciones de tiempo les puedo sumar y restar segundos.
    · Las duraciones de tiempo se pueden sumar y restar.
"""


class Duration:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

