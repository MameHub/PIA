'''
Crea una clase que modele un dado de parchís trucado (TrickedLudoDice) que derive de la clase anterior y
que de cuando nos permita poner el valor que queramos en la cara del dado (entre 1 y 6), de manera que:
    · No puedo usar el método que pone el valor que queramos en la cara del dado (put) si no he tirado
    al menos tres veces de forma normal, si lo llamo sin haberse cumplido esta excepción lanzaremos una
    excepción.
    · Ten en cuenta que NO PUEDES cambiar directamente el valor de la cara de un dado ya que se almacena
    en una variable de instancia privada de una clase de la que heredas (Dice) y no tienes acceso.
'''

