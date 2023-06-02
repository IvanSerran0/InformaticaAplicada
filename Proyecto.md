```python
import pandas as pd
import statistics
import matplotlib .pyplot as plt
import numpy as np

base=pd.read_csv('iris.csv')
longitud_sepalo=base['sepal.length']
ancho_sepalo=base['sepal.width']
longitud_petalo=base['petal.length']
ancho_petalo=base['petal.width']
tipo=base['variety']
```

## Análisis estadístico de datos de la flor Iris


### I.Introduccion




'''
II.Variables y tipos de datos
A. Descripcion de las variables utilizadas en el conjunto de datos de Iris
B. Tipos de datos utilizados en el conjunto de datos de Iris (numéricos y categóricos)
'''

'''
III. Análisis estadístico con el conjunto de datos de Iris
A. Presentación del conjunto de datos de Iris y sus características.
'''
print("----------Conjunto de datos acerca de la longitud del Sépalo de la flor Iris:----------")
print(longitud_sepalo)
print("----------Conjunto de datos acerca del ancho del Sépalo de la flor Iris:----------")
print(ancho_sepalo)
print("----------Conjunto de datos acerca de la longitud del Petalo de la flor Iris:----------")
print(longitud_petalo)
print("----------Conjunto de datos acerca del ancho del Petalo de la flor Iris:----------")
print(ancho_petalo)
print("----------Conjunto de datos acerca del tipo de la flor Iris:----------")
print(tipo)

'''
B. Estadística descriptiva. Cálculo de medidas: promedio, desviación estándar,
mínimos y máximos.
'''


mean_sep1 = statistics.mean(base['sepal.length'])
mean_sep2 = statistics.mean(base['sepal.width'])
mean_pet1 = statistics.mean(base['petal.length'])
mean_pet2 = statistics.mean(base['petal.width'])

print("--------Promedio de los datos---------")
print("El promedio de la longitud del Sépalo de la flor Iris es: ", mean_sep1)
print("El promedio del ancho del Sépalo de la flor Iris es: ", mean_sep2)
print("El promedio de la longitud del Pétalo de la flor Iris es: ", mean_pet1)
print("El promedio del ancho del Pétalo de la flor Iris es: ", mean_pet2)

desv_sep1 = statistics.pstdev(base['sepal.length'])
desv_sep2 = statistics.pstdev(base['sepal.width'])
desv_pet1 = statistics.pstdev(base['petal.length'])
desv_pet2 = statistics.pstdev(base['petal.width'])

print("--------Desviacion estandar de los datos---------")
print("La desviación estandar de la longitud del Sépalo de la flor Iris es: ", desv_sep1)
print("La desviación estandar del ancho del Sépalo de la flor Iris es: ", desv_sep2)
print("La desviación estandar de la longitud del Pétalo de la flor Iris es: ", desv_pet1)
print("La desviación estandar del ancho del Pétalo de la flor Iris es: ", desv_pet2)

print("--------Minimos y máximos de los datos---------")
print("El valor mínimo de la longitud del Sépalo de la flor Iris es: ", min(base['sepal.length']))
print("El valor máximo de la longitud del Sépalo de la flor Iris es: ", max(base['sepal.length']))

print("El valor mínimo del ancho del Sépalo de la flor Iris es: ", min(base['sepal.width']))
print("El valor máximo del ancho del Sépalo de la flor Iris es: ", max(base['sepal.width']))

print("El valor mínimo de la longitud del Pétalo de la flor Iris es: ", min(base['petal.length']))
print("El valor máximo de la longitud del Pétalo de la flor Iris es: ", max(base['petal.length']))

print("El valor mínimo del ancho del Pétalo de la flor Iris es: ", min(base['petal.width']))
print("El valor máximo del ancho del Pétalo de la flor Iris es: ", max(base['petal.width']))

'''
IV. Visualización de datos
A. Uso de gráficos y visualizaciones para representar los datos de Iris.
B. Creación de gráficos de dispersión e histogramas, para revelar patrones y
distribuciones de los datos. Para cubrir el inciso (B), mínimo presentar los siguientes
tres gráficos:

    1. Histograma de las longitudes de pétalos para cada especie de Iris.
    2. Diagrama de dispersión de longitud del sépalo vs. ancho del sépalo
    3. Correlación entre las variables
'''


setosa=base[0:50]
versicolor=base[50:100]
virginica=base[101:150]
#--------HISTOGRAMAS--------
plt.hist(setosa['petal.length'],bins=50)
plt.title('Longitud de pétalo de la especie "Setosa" de Iris')
plt.xlabel('Longitud de pétalo')
plt.ylabel('Frecuencia')
plt.show()

plt.hist(versicolor['petal.length'],bins=50)
plt.title('Longitud de pétalo de la especie "Versicolor" de Iris')
plt.xlabel('Longitud de pétalo')
plt.ylabel('Frecuencia')
plt.show()

plt.hist(versicolor['petal.length'],bins=50)
plt.title('Longitud de pétalo de la especie "Virginica" de Iris')
plt.xlabel('Longitud de pétalo')
plt.ylabel('Frecuencia')
plt.show()

#--------Diagrama de dispersion--------

plt.scatter(base['sepal.length'],base['sepal.width'])
plt.title('Longitud del Sépalo vs. Ancho del Sépalo')
plt.xlabel('Longitud del Sépalo')
plt.ylabel('Ancho del Sépalo')
plt.show()

#--------Correlación de los datos de la longitud y el anocho del Sépalo--------
corr=np.corrcoef(base['sepal.length'],base['sepal.width'])[0,1]

plt.scatter(base['sepal.length'],base['sepal.width'])
plt.title(f'Coeficiente de correlación del Sépalo: {corr:.2f}')
plt.xlabel('Longitud del Sépalo')
plt.ylabel('Ancho del Sépalo')
plt.show()

#--------Correlación de los datos de la longitud y el anocho del Pépalo--------
corr2=np.corrcoef(base['petal.length'],base['petal.width'])[0,1]
plt.scatter(base['petal.length'],base['petal.width'])
plt.title(f'Coeficiente de correlación del Pétalo: {corr2:.2f}')
plt.xlabel('Longitud del Pétalo')
plt.ylabel('Ancho del Pétalo')
plt.show()

print("")