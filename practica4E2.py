import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t,sem
import math

def fdp(x):
    return(4*(x**2)-10)

masimo= max(fdp(2),fdp(3))

def GeDeX(x):
    return(fdp(x)/masimo)

def aceptacionRechazo():
    r1=random.random()
    r2=random.random()
    x=2+(3-2)*r1
    while (r2>GeDeX(x)):
        r1=random.random()
        r2=random.random()
        x=2+(3-2)*r1
    return x

def tiempoDeServicio():
  r = random.uniform(0,1)
  if (r < 0.2):
    return random.uniform(1,2)
  elif (r < 0.55):
    return random.uniform(2,3)
  elif (r < 0.85):
    return random.uniform(3,4)
  else:
    return random.uniform(4,5)

numeroUsuarios = range(0, 50)
numeroDeSimulaciones = range(0, 1000)

promedioTiempoEnTaquilla=[]
promedioTiempoEnSistema=[]
promedioColaUsuario=[]

for simulacion in numeroDeSimulaciones:
    tiempoEnTaquilla= []
    tiempoEnSistema=[]
    tiempoEnCola=[]
    ### Listas auxiliares ###
    tServicioAux=[0]
    horasAuxiliar=[0]
    tiempoSistemaAux=[0]
    ### Fin listas auxiliares ###
    for usuario in numeroUsuarios:
        tiempoLlegada= aceptacionRechazo()
        tiempoServicio= tiempoDeServicio()
        horaLlegada=horasAuxiliar[0]+tiempoLlegada
        tiempoCola=max(0,horaLlegada-tiempoSistemaAux[0])
        horaSalida= horaLlegada+tiempoCola+tiempoServicio
        tiempoSistema= tiempoServicio+tiempoCola
        tServicioAux.insert(0, tiempoServicio)
        horasAuxiliar.insert(0,horaLlegada)
        tiempoSistemaAux.insert(0,tiempoSistema)
        tiempoEnTaquilla.append(tiempoServicio)
        tiempoEnCola.append(tiempoCola)
        tiempoEnSistema.append(tiempoSistema)
    promedioTiempoEnTaquilla.append(np.mean(np.array(tiempoEnTaquilla)))
    promedioTiempoEnSistema.append(np.mean(np.array(tiempoEnSistema)))
    promedioColaUsuario.append(np.mean(np.array(tiempoEnCola)))

print("Los siguientes datos arrojados son en base a 1000 simulaciones de 100 clientes cada una.")    
print('El tiempo promedio en Taquilla es de:',np.mean(np.array(promedioTiempoEnTaquilla)),'minutos')
print('El tiempo promedio en el Sistema es de:',np.mean(np.array(promedioTiempoEnSistema)),'minutos')
print('El tiempo promedio de un usuario en Cola es de:',np.mean(np.array(promedioColaUsuario)),'minutos')

plt.figure(figsize=(10,4))
plt.hist(promedioColaUsuario, color="darkblue", bins=100,alpha=0.75,edgecolor='black',linewidth=0.75)
##plt.xticks(range(30,50))
plt.title("Histograma de frecuencia de los tiempos en cola de un usuario")
plt.xlabel("Tiempos")
plt.ylabel("Frecuencia")
plt.show()
plt.clf()