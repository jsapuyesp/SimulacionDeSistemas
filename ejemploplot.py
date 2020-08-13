import random
import matplotlib.pyplot as plt

intentos=int(input('Casos de prueba: '))
gana=0
pierde=0

for i in range(intentos):
  cara=0
  sello=0
  paga=0
  while(abs(cara-sello)!=3):
    n = random.random()
    paga+=1
    if(n<0.5):
      cara+=1
    else:
      sello+=1
  if(8-paga>0):
    gana+=1
  elif(8-paga<0):
    pierde+=1
  
fig = plt.figure(u'Gráfica de resultados') # Figure
ax = fig.add_subplot(111) # Axes

labels = ['Gana','Pierde']
datos = [gana,pierde]
xx = range(len(datos))

ax.bar(xx, datos, width=0.8, align='center')
ax.set_xticks(xx)
ax.set_xticklabels(labels)

plt.show()