# Importamos el paquete typeguard de la libreria typechecked
from typeguard import typechecked

# Chequeamos en toda la clase los tipos de datos, al estar sobre la clase, se aplicará a toda esta.
@typechecked
class Stack:
    # Creamos una variable de clase indicando el tamaño máximo de la pila, este será de tipo entero.
    default_max_size: int = 5

    # Creamos y definimos el constructor de la clase.
    # Es posible utilizar una lista como parámetro en vez de un número indeterminado de valores, "values: List = []"
    def __init__(self, *values: int): # El asterisco delante del parámetro indica un número indeterminado de valores de entrada.
        if len(values) > Stack.default_max_size:
            raise MemoryError(f"Se supera el tamaño permitido de la pila: {Stack.default_max_size} elementos.")
        self.__values = list(values)

    # 
    def __str__(self):
        str_ = ""       # El nombre es "str_" porque "str" es una palabra reservada
        for n in self.__values:
            str_ += f"{n}\n"
        return str(self.__values)
    
    # 
    def __repr__(self):
        return f"{self.__class__.__name__}({self.__values})"
    
    # Creámos el método "push()" para insertar datos en la pila.
    def push(self, value: int):
        self.__values.insert(0, value)

    # Creámos el método "pop()" para eliminar datos en la pila.
    def pop(self):
        return self.__values.pop(0)
    
    # 
    def top(self):
        return self.__values[0]
    
    # Creámos el método para obtener el tamaño de la pila.
    def size(self):
        return len(self.__values)
    
    # Creámos el método para saber si la pila esta vacía.
    def is_empty(self):
        return self.size() == 0
    
    # Creámos el método para vaciar la pila.
    def clear(self):
        self.__values.clear()