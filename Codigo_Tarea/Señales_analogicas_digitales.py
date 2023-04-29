# Señales analógicas vamos a trabajar señales analogicas en esta primera parte
import numpy as np #cargamos la libreria numpy para procesamiento numerico y la cargamos como np
import matplotlib.pyplot as plt #cargamos la libreria para poder graficar en python y la cargamos como plt
import scipy.io.wavfile as waves #libreria para lectura de archivos de audio tipo wav y la importamos como waves

# INGRESO
archivo = 'Alarm01.wav' #Se procesa un archivo de audio (cabe recalcar que hay que poner el nombre del archivo y extension)
muestreo, sonido = waves.read(archivo) #hay que obtener la veloccidad de muestreo y el sonido que obtenemos mediante la funcion waves del archivo

# SALIDA - Observacion intermedia
print('frecuencia de muestreo: ', muestreo) #Nos mostrará la frecuencia del sonido guardado en la variable muestreo 22050
print('dimensiones de matriz: ', np.shape(sonido)) #Nos mostrará cuantos canales de audio existen (122868,2)
print('datos de sonido: ')
print(sonido) #[[0 0]]

# segmento de tiempo para visualizar en una gráfica
canal  = 0 #canal que observaremos
inicia = 2600 #desde que punto inicia nuestra observacion
termina = 2720 #y donde termina la observacion

# Extrae el segmento desde sonido para visualizar en unidades de tiempo ya que lña señal es analogica
dt = 1/muestreo #1/22050=4.5351
ti  = np.arange(inicia*dt,termina*dt,dt) #Para interpretar los elementos de tiempo utilizamos este arreglo 
muestras = len(ti) #La cantidad de muestras que vamos a observar corresponde al tamaño del vector ti
segmento = sonido[inicia:inicia+muestras, canal] #El segmento del sonido que se va a observar corresponde al numero de muestras desde donde inicia hasta inicia+muestras, utilizando el canal seleccionado

#SALIDA
plt.plot(ti,segmento) #La grafica se obtiene con esta instruccion utilizando los valores de ti y el degmento seleccionado
plt.xlabel('t segundos') #Etiqueta para el eje de las x
plt.ylabel('sonido(t)') #Etiqueta para el eje y
plt.show() #Es para observar en pantalla la gráfica y se observa una gráfica una señal que varia de forma oscilatoria del sonido en el segmento seleccionado

# SALIDA - datos del segmento de audio
print(segmento) #Se observan los valores de la gráfica del segmento seleccionado

############Señales Digitales

# grafica segmento de sonido en forma discreta
ni = np.arange(inicia,inicia+muestras,1)
plt.stem(ni,segmento) #Nos muestra la gráfica sin unir los puntos por una linea
plt.xlabel('n')
plt.ylabel('segmento sonido[n]')
plt.show()