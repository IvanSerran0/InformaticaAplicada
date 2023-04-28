# Señales analógicas
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves

# INGRESO
# archivo = input('archivo de audio: ')
archivo = 'Alarm01.wav'
muestreo, sonido = waves.read(archivo)

# SALIDA - Observacion intermedia
print('frecuencia de muestreo: ', muestreo)
print('dimensiones de matriz: ', np.shape(sonido))
print('datos de sonido: ')
print(sonido)

# segmento de tiempo
canal  = 0
inicia = 2600
termina = 2720

# Extrae el segmento desde sonido
dt = 1/muestreo
ti  = np.arange(inicia*dt,termina*dt,dt)
muestras = len(ti)
segmento = sonido[inicia:inicia+muestras, canal]

#SALIDA
plt.plot(ti,segmento)
plt.xlabel('t segundos')
plt.ylabel('sonido(t)')
plt.show()

############Señales Digitales

# SALIDA - datos del segmento de audio
print(segmento)

# grafica segmento de sonido en forma discreta
ni = np.arange(inicia,inicia+muestras,1)
plt.stem(ni,segmento)
plt.xlabel('n')
plt.ylabel('segmento sonido[n]')
plt.show()