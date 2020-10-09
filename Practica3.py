import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t,sem

def demandaDiaria():
  r = random.random()
  if (r < 0.12):
    return 25
  elif (r < 0.2):
    return 30
  elif (r < 0.5):
    return 35
  elif (r < 0.75):
    return 40
  elif (r < 0.85):
    return 45
  elif (r < 0.95):
    return 50
  else:
    return 55

pedidosRango = range(25,56)
ventaPeriodico = 1600
compraPeriodico = 1300
retornoEmpresa = 750
dias = 1000

promedioUtilidades = []
listadelistasUtilidades = []

for pedidos in pedidosRango:
    utilidad = 0
    listaUtilidadesDiarias = []
    for dia in range(dias):
        demanda = demandaDiaria()
        diferenciaPeriodicos = pedidos - demanda
        if (diferenciaPeriodicos > 0):
            utilidadDia = (demanda * (ventaPeriodico - compraPeriodico)) - ( diferenciaPeriodicos * (compraPeriodico - retornoEmpresa))
            utilidad+=utilidadDia
        else:
            utilidadDia = (pedidos*(ventaPeriodico-compraPeriodico))
            utilidad+=utilidadDia
        listaUtilidadesDiarias.append(utilidadDia)
    listadelistasUtilidades.append(listaUtilidadesDiarias)
    media= np.mean(np.array(listaUtilidadesDiarias))
    promedioUtilidades.append(media)
    print('utilidades pidiendo',str(pedidos),'periodicos',str(utilidad),'la media fue de',str(media))



#Primera Gráfica:
labels = [str(x) for x in pedidosRango]
ticks = range(len(promedioUtilidades))
indiceMayorUtilidadP = promedioUtilidades.index(max(promedioUtilidades))
params = {
    "ytick.color" : "w",
    "xtick.color": "w",
    "axes.labelcolor" : "w",
    "axes.edgecolor" : "w",
    "text.color" : "w",
    "figure.facecolor": "#2c2c2c"
}
plt.rcParams.update(params)
plt.figure(figsize=(10,5))

y_max = [np.max(promedioUtilidades)]*len(promedioUtilidades)
max_line = plt.plot(ticks, y_max, label = 'Max', color = 'r')

plt.plot(ticks, promedioUtilidades)
plt.title("Utilidad promedio por día")
plt.ylabel("Utildad total promedio")
plt.xlabel("Numero de pedidos")
plt.xticks(ticks, labels)
plt.show()
plt.clf()

print("La mejor cantidad de periodicos que se deberian pedir para un maximo beneficio es:", labels[indiceMayorUtilidadP])
print("Maxima utilidad promedio:", promedioUtilidades[indiceMayorUtilidadP])


######
#Estadística descriptiva

minimo=min(listadelistasUtilidades[indiceMayorUtilidadP])
maximo=max(listadelistasUtilidades[indiceMayorUtilidadP])
media=np.mean(np.array(listadelistasUtilidades[indiceMayorUtilidadP]))
mediana=np.median(np.array(listadelistasUtilidades[indiceMayorUtilidadP]))
desviacionEstandar=np.std(np.array(listadelistasUtilidades[indiceMayorUtilidadP]))

print('El valor minimo es:',minimo)
print('El valor maximo es:',maximo)
print('La media de los datos es:',media)
print('La mediana de los datos es:',mediana)
print('La desviación estandar de la prueba fue:',desviacionEstandar)

#######
#Intervalo de confianza
std_err = sem(listadelistasUtilidades[indiceMayorUtilidadP])
confidence = 0.95
h= std_err*t.ppf((1+confidence)/2,dias-1)
lim_inf = media-h
lim_sup = media+h

intervalo =(round(lim_inf,2),round(lim_sup,2))

print('El valor de H es:',h)
print('El intervalo de confianza para la media de las utilidades con una confianza del 95% es de:',intervalo)