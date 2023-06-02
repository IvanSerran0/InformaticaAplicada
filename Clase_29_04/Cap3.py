import numpy as np
import statistics as stat
print("----------------------------------------------------")
# Creamos una lista de datos
datos = np.array([10, 12, 15, 18, 20, 22, 24, 28, 30, 30])
# Calculamos la media
media = np.mean(datos)
# Calculamos la mediana
mediana = np.median(datos)
# Calculamos la moda
# moda = np.mode(datos)
moda = stat.mode(datos)
# Calculamos la desviación estándar
desv_estandar = np.std(datos)
# Calculamos la varianza
varianza = np.var(datos)
# Imprimimos los resultados
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)
print("Desviación estándar:", desv_estandar)
print("Varianza:", varianza)
print("----------------------------------------------------")
datos1 = np.array([5, 7, 8, 9, 10, 11, 12, 14, 15, 16])
media1 = np.mean(datos1)
print("Media ehjercicio 1:", media1)
mediana1 = np.median(datos1)
print("Mediana ejercicio 1:", mediana1)
desv_estandar1 = np.std(datos1)
print("Desviación estándar ejercicio 1:", desv_estandar1)
print("----------------------------------------------------")
#2. Calcular el coeficiente de variación de un conjunto de datos:
datos2 = np.array([5, 7, 8, 9, 10, 11, 12, 14, 15, 16,17,18,19,20])
media2=np.mean(datos2)
desv_estandar2=np.std(datos2)
CV=(desv_estandar2/media2)*100
print("Coeficiente de variación:", CV)