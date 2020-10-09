import random as r
import matplotlib.pyplot as plt
import numpy as np

NumeroDeIntentos = 2000

gano=0                                              #Entendemos ganar por quedar con utilidades >0
perdio=0                                            #Entendemos perder por quedar con utilidades <0
empato=0                                            #Entendemos empate cuando la utilidad =0
ganancias=0                                         #Cuánto dinero se ganó después de todas las simulaciones
perdidas=0                                          #Cuánto dinero se perdió después de todas las simulaciones
tirosTotales=0
totaldinero=[]
utilidadTotal=0
totaltiros=[]

for intento in range(NumeroDeIntentos):             #Se ejecutan las N simulaciones
    utilidad=0                                      #Utilidad en cada simulación
    cara=0                                          #N° de caras
    sello=0                                         #N° de sellos
    diferencia=abs(cara-sello)                      #Diferencia entre caras y sellos
    numeroDeTiros=0                                 #Tiros en la simulacion
    while diferencia < 3:
        numeroDeTiros+=1
        x= r.random()
        if x < 0.5:
            cara+=1
        else:
            sello+=1
        diferencia=abs(cara-sello)
        utilidad-=1
    utilidad+=8
    tirosTotales+=numeroDeTiros
    utilidadTotal+=utilidad
    totaldinero.append(utilidadTotal)
    totaltiros.append(numeroDeTiros)

    if utilidad > 0:
        gano+=1
        ganancias+=utilidad
    elif utilidad < 0:
        perdio+=1
        perdidas+=utilidad
    else:
        empato+=1

porcentajegano=str(round((gano/NumeroDeIntentos)*100,2))
porcentajeperdio=str(round((perdio/NumeroDeIntentos)*100,2))
porcentajeempato=(empato/NumeroDeIntentos)*100 #Esta variable luego de varias pruebas nunca tomó un valor diferente de 0. Si se cambia la condición de diferencia por 2, sí cambia
porcentajes=[porcentajegano,porcentajeperdio]
x=[porcentajegano,porcentajeperdio]
media=np.mean(np.array(totaltiros))

print('ganó:',gano,'con una probabilidad del:',porcentajegano,'%','con una ganancia de:',ganancias)
print('perdió:',perdio,'con una probabilidad del:',porcentajeperdio,'%','con una perdida de:',perdidas)
print('empató:',empato,'con una probabilidad del:',porcentajeempato,'%')
print('el total de tiros en las',NumeroDeIntentos,'simulaciones, fueron:',tirosTotales)
print('la utilidad total al hacer las',NumeroDeIntentos,'fue de ',utilidadTotal)

plt.pie(porcentajes,labels=x,shadow=True)
plt.title("Probabilidad de ganar el juego")
plt.legend(['Probabilidad de ganar %', 'Probabilidad de perder %'],loc="center left")
plt.xlabel("Las probabilidades están calculadas en base a "+str(NumeroDeIntentos)+" simulaciones")
plt.show()
plt.clf()

y= np.array(totaldinero)
x= np.array(range(1,len(y)+1))
plt.title("Dinero acumulado vs tiempo en "+str(NumeroDeIntentos)+ " simulaciones")
plt.ylabel("Dinero acumulado")
plt.xlabel("Simulaciones")
plt.plot(x,y, color="g")
plt.show()
plt.clf()

ejex=np.arange(0,NumeroDeIntentos)
ejey=np.array(totaltiros)
plt.bar(ejex,ejey,color="g")
plt.axhline(media,xmin=0,xmax=NumeroDeIntentos,color="r")
plt.legend(["Media de tiros: "+str(media) , "Cantidad de tiros"])
plt.show()

