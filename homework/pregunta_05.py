"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    traductor = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E':4}
    minimos = len(traductor) * [float('inf')]
    maximos = len(traductor) * [( -1 * float('inf'))]


    with open('files/input/data.csv', 'r') as file:
        for linea in file:
            datos = linea.split()
            letra = datos [0]
            valor = int(datos[1])

            if valor > maximos[traductor[letra]]:
                maximos[traductor[letra]] = valor

            if valor < minimos[traductor[letra]]:
                minimos[traductor[letra]] = valor

    res = [(letra, maximos[i], minimos[i]) for i, letra in enumerate(traductor.keys())]
    return res