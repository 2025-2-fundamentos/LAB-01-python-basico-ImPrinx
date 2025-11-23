"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    traductor = {'aaa': 0, 'bbb': 1, 'ccc': 2, 'ddd': 3, 'eee':4, 'fff':5 , 'ggg':6, 'hhh':7, 'iii':8, 'jjj':9}
    minimos = len(traductor) * [float('inf')]
    maximos = len(traductor) * [( -1 * float('inf'))]

    with open('files/input/data.csv', 'r') as file:
        for linea in file:
            datos = linea.split()
            codificados = datos[4]
            lista_de_diccionario = codificados.split(',')
            for diccionario in lista_de_diccionario:
                clave, valor = diccionario.split(':')
                valor = int(valor)
                
                if valor > maximos[traductor[clave]]:
                    maximos[traductor[clave]] = valor

                if valor < minimos[traductor[clave]]:
                    minimos[traductor[clave]] = valor

    res = [(clave, minimos[i], maximos[i]) for i , clave in enumerate(traductor.keys())]

    return res