import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t,sem
import math

def exponencial(lam):
    r= random.random()
    return (-1/lam)*math.log(1-r)

def normal(media, desviacion):
    u1=random.random()
    u2=random.random()
    x1=math.sqrt(-2*math.log(u1))*math.cos(2*math.pi*u2)
    x2=math.sqrt(-2*math.log(u1))*math.sin(2*math.pi*u2)
    x1p=media+desviacion*x1
    x2p=media+desviacion*x2
    return max(x1p,x2p)

numeroUsuarios = range(0, 100)
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
        tiempoLlegada= exponencial(0.8)
        tiempoServicio= normal(2,1)
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
plt.xticks(range(15,50))
plt.title("Histograma de frecuencia de los tiempos en cola de un usuario")
plt.xlabel("Tiempos")
plt.ylabel("Frecuencia")
plt.show()
plt.clf()