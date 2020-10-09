import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t,sem

## Todo es uniforme


##### Funciones para tiempos aleatorios
def prepararhuevos():
    descascarar= random.uniform(2,4)
    batir = random.uniform(2,4)
    cocinar = random.uniform(2,4)
    tiempoTotal = descascarar+batir+cocinar
    return tiempoTotal
def prepararPan():
    tostarPan = random.uniform(3,6)
    untarMantequilla = random.uniform(3,6)
    tiempoTotal = tostarPan+untarMantequilla
    return tiempoTotal
def cocinarTocineta():
    freirTocineta = random.uniform(6,12)
    return freirTocineta
#####
#####

numeroSimulaciones =range(0, 1000)
listaCaminoCritico=[]
listaTiempos=[]


for simulacion in numeroSimulaciones:
    huevos = prepararhuevos()
    pan= prepararPan()
    tocineta = cocinarTocineta()
    tiempoDesayuno = max(huevos,pan,tocineta)
    listaTiempos.append(tiempoDesayuno)
    if tiempoDesayuno == huevos:
        listaCaminoCritico.append("Preparar Huevos")
    elif tiempoDesayuno == pan:
        listaCaminoCritico.append("Preaparar pan Tostado")
    else:
        listaCaminoCritico.append("Cocinar Tocineta")

## Punto 1 . Calculos estadísticos
media = np.mean(listaTiempos)
maximoEstadistico = np.max(listaTiempos)
minimoEstadistico = np.min(listaTiempos)
print("Media:",media,"Maximo:",maximoEstadistico,"Minimo:",minimoEstadistico)