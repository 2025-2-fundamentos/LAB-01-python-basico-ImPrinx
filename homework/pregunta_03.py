"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from collections import defaultdict

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    suma_por_letra = defaultdict(int)
    with open('files/input/data.csv', 'r') as file:
        for linea in file:
            letra ,numero = linea.split()[0:2] 
            suma_por_letra[letra] += int(numero)

    return sorted(suma_por_letra.items(), key = lambda x: x[0])
pregunta_03()