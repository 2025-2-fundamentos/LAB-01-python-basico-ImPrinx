"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from collections import defaultdict

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    suma_por_letra = defaultdict(int)

    with open('files/input/data.csv', 'r') as file:
        for linea in file:
            datos = linea.split()
            valor = int(datos[1])

            for letra in datos[3].split(','):
                suma_por_letra[letra] +=valor

    return dict(sorted(suma_por_letra.items()))
pregunta_11()