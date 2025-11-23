"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from collections import defaultdict


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    ocurrencias = defaultdict(int)

    with open('files/input/data.csv', 'r') as file:
        for linea in file:
            datos = linea.split()
            codificados = datos[4]
            lista_de_diccionario = codificados.split(',')
            for diccionario in lista_de_diccionario:
                clave, valor = diccionario.split(':')
                ocurrencias[clave] +=1

    return dict(sorted(ocurrencias.items()))