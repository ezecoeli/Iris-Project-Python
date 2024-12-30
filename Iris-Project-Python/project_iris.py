## Objetivo:
""" Aplicación que permite realizar un análisis estadístico básico del conjunto de datos Iris. 
    El análisis incluye el cálculo del promedio y la desviación estándar para las características de las flores, 
    (longitud y ancho del sépalo, longitud y ancho del pétalo) para cada especie de Iris."""

import csv
import math

def cargar_datos(file_path):
    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)
        dataset = [row for row in csv_reader if row] # Excluye filas vacías
    return dataset

def agrupar_por_especie(datos):
    agrupados = {}
    for fila in datos:
        especie = fila[-1]
        caracteristicas = list(map(float, fila[:-1]))  # Convierte a float todas menos la especie
        if especie not in agrupados:
            agrupados[especie] = {'longitud_sepalo': [],
                                  'ancho_sepalo': [],
                                  'longitud_petalo': [],
                                  'ancho_petalo': []}
        agrupados[especie]['longitud_sepalo'].append(caracteristicas[0])
        agrupados[especie]['ancho_sepalo'].append(caracteristicas[1])
        agrupados[especie]['longitud_petalo'].append(caracteristicas[2])
        agrupados[especie]['ancho_petalo'].append(caracteristicas[3])
    return agrupados

class Flor:
    def __init__(self, longitud_sepalo, ancho_sepalo, longitud_petalo, ancho_petalo):
        #Inicializa la Flor con listas de sus características.
        self.longitud_sepalo = longitud_sepalo
        self.ancho_sepalo = ancho_sepalo
        self.longitud_petalo = longitud_petalo
        self.ancho_petalo = ancho_petalo

    def promedio(self, datos):
        #Calcula el promedio de una lista de números.
        return sum(datos) / len(datos)

    def desviacion_estandar(self, datos):
        # Calcula la desviación estándar de una lista
        prom = self.promedio(datos)
        varianza = sum((x - prom) ** 2 for x in datos) / len(datos)
        return math.sqrt(varianza)

    def analisis(self):
        # Devuelve el análisis de la flor: promedio y desviación estándar para cada característica.
        analisis = {
            'longitud_sepalo': {'promedio': self.promedio(self.longitud_sepalo),
                                'desviacion_estandar': self.desviacion_estandar(self.longitud_sepalo)},
            'ancho_sepalo': {'promedio': self.promedio(self.ancho_sepalo),
                             'desviacion_estandar': self.desviacion_estandar(self.ancho_sepalo)},
            'longitud_petalo': {'promedio': self.promedio(self.longitud_petalo),
                                'desviacion_estandar': self.desviacion_estandar(self.longitud_petalo)},
            'ancho_petalo': {'promedio': self.promedio(self.ancho_petalo),
                             'desviacion_estandar': self.desviacion_estandar(self.ancho_petalo)}
        }
        return analisis

datos = cargar_datos("Projects/iris.data.csv")
Flores = agrupar_por_especie(datos)

Iris_setosa = Flor(Flores['Iris-setosa']['longitud_sepalo'],
                   Flores['Iris-setosa']['ancho_sepalo'],
                   Flores['Iris-setosa']['longitud_petalo'],
                   Flores['Iris-setosa']['ancho_petalo'])

print(f"El análisis de Iris Setosa es el siguiente:\n {Iris_setosa.analisis()}")

Iris_versicolor = Flor(Flores['Iris-versicolor']['longitud_sepalo'],
                   Flores['Iris-versicolor']['ancho_sepalo'],
                   Flores['Iris-versicolor']['longitud_petalo'],
                   Flores['Iris-versicolor']['ancho_petalo'])

print(f"El análisis de Iris Versicolor es el siguiente:\n {Iris_versicolor.analisis()}")

