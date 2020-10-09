import random as r
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t,sem

numeroSimulaciones=1000
costoHab=125000
utilidades=[]
multa=200000
reservasMin=90
reservasMax=110
capMaxima=100
utilidadHabs=[]
penalizacionesXCantidad=[]
utilidadxreservas=[]


for reservas in range(reservasMin,reservasMax+1):
    utilidadSim=0
    for simulacion in range(numeroSimulaciones+1):
        habitacionesUso=0
        costoVariable= round((r.random()*20000)+10000)        
        utilidad=0
        penalizaciones=0
        for persona in range(0,reservas+1):
            personallega=r.random()
            if (personallega>0.05) and (habitacionesUso<capMaxima) :
                costoPer=costoHab-costoVariable
                habitacionesUso+=1
                utilidad+= costoPer
            elif (personallega>0.05) and (habitacionesUso>=capMaxima):
                costoPer= costoHab-multa
                utilidad+= costoPer
                penalizaciones+=1
            elif (personallega<=0.05):
                utilidad+=costoHab
        utilidadSim+=utilidad
    utilidadHabs.append(utilidadSim)
    penalizacionesXCantidad.append(penalizaciones)
    print("El promedio de utilidades con",str(reservas),"reservas fue de", str(utilidadSim/numeroSimulaciones))
    utilidadxreservas.append(utilidadHabs)

mayorUtilidad= utilidadHabs.index(max(utilidadHabs))



#Grafica
labels = [str(x) for x in range(reservasMin,reservasMax+1)]
print("la mayor cantidad de reservas que puede aceptar son:", labels[mayorUtilidad])
ticks = range(len(utilidadHabs))
params = {"ytick.color" : "w",
          "xtick.color" : "w",
          "axes.labelcolor" : "w",
          "axes.edgecolor" : "w",
          "text.color": "w",
          "figure.facecolor": "#2c2c2c"}
plt.rcParams.update(params)
plt.figure(figsize=(8,3))

y_max=[np.max(utilidadHabs)]*len(utilidadHabs)
max_line= plt.plot(ticks, y_max, label="Max", color="y")

plt.plot(ticks, utilidadHabs)
plt.title("Utilidad total por numero de reservas")
plt.ylabel("Utilidad total")
plt.xlabel("Numero de reservas")
plt.legend("Utilidades", "Utilidad máxima")
plt.xticks(ticks, labels)
plt.show()
plt.clf()

#######################################################################################
resultados= np.array(utilidadxreservas[mayorUtilidad])
plt.figure(figsize=(8,3))
plt.title("Utilidades Diarias")
plt.ylabel("Numero de repeticiones")
plt.xlabel("Utilidad")
plt.hist(resultados, linewidth=1, rwidth=0.75, color="g")
plt.show()
plt.clf()
print(mayorUtilidad)

#######################################################################################

minimo= min(utilidadxreservas[mayorUtilidad])
maximo= max(utilidadxreservas[mayorUtilidad])
media=np.mean(np.array(utilidadxreservas[mayorUtilidad]))
mediana=np.median(np.array(utilidadxreservas[mayorUtilidad]))
desviacionEstandar= np.std(np.array(utilidadxreservas[mayorUtilidad]))

print("La minima utilidad diaria fue:", minimo)
print("La máxima utilidad diaria fue:", maximo)
print("La media de las utilidades diarias fue:",media)
print("La mediana de las utilidades diarias fue:",mediana)
print("La desviacion estandar de las utilidades diarias fue:",desviacionEstandar)

##########################################################################################

std_err= sem(utilidadxreservas[mayorUtilidad])
confidence =0.95
h= std_err * t.ppf((1+confidence)/2,numeroSimulaciones-1)
lim_inf=media-h
lim_sup=media+h
print("Valor de h:",h)
print("Intervalo de confianza para la media de las utilidades con una confianza del 95%: (",round(lim_inf,2),",",round(lim_sup,2), ")")





