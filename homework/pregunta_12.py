"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from collections import defaultdict

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    suma_por_letra = defaultdict(int)

    with open('files/input/data.csv', 'r') as file:
        for linea in file:
            datos = linea.split()
            letra = datos[0]
            codificados = datos[4]
            lista_de_diccionario = codificados.split(',')
            for diccionario in lista_de_diccionario:
                clave, valor = diccionario.split(':')
                suma_por_letra[letra] +=int(valor)

    return dict(sorted(suma_por_letra.items()))

pregunta_12()