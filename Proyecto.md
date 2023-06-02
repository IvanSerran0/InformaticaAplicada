

## Análisis estadístico de datos de la flor Iris

### I.Introduccion

La planta de iris comúnmente conocida como lirio es una planta de la familia de las Ridáceas. Ésta es originaria del continente europeo y cuenta con hojas largas en forma de cinta que pueden medir unos 40 cm.  Estas hojas se presentan erguidas y son verdes en tonos claros.

Las flores del lirio ofrecen bastante perfume y también un gran tamaño. Normalmente se presentan en grupos de unas seis flores y son de color violeta o purpura. Además de estos colores también se puede encontrar en colores amarillos, blancos, rojos y también en flores jaspeadas.

Dentro de los usos del iris está el decorativo, aunque en sus raíces ésta tiene un jugo que puede darse como purgante. [1]

En el presente proyecto se analizará estadisticamente en Python una base de datos que contiene datos importantes de la flor Iris y sus variantes.

### II.Variables y tipos de datos

- Variables numéricas
Son variables que se utilizan para almacenar y operar con todo tipo de números. 

- Variables de texto (cadenas)
En estas variables se almacenan datos referentes a caracteres o cadenas de texto, como pueden ser palabras,
frases o cadenas de texto que contengan letras y números

En el presente proyecto se estarán manejando variables como la longitud y el ancho del Sépalo y Pétalo de la flor Iris, este tipo de variables serán numéricos.

El tipo de flor Iris será otro tipo de variable, en este caso será una variable de texto o cadena.

##### Importando librerias
```python

import pandas as pd
import statistics
import matplotlib .pyplot as plt
import numpy as np
```
##### Declarando variables globales para el uso de los diferentes datos del dataset
```python
base=pd.read_csv('iris.csv')
longitud_sepalo=base['sepal.length']
ancho_sepalo=base['sepal.width']
longitud_petalo=base['petal.length']
ancho_petalo=base['petal.width']
tipo=base['variety']
```
'''
III. Análisis estadístico con el conjunto de datos de Iris
A. Presentación del conjunto de datos de Iris y sus características.
'''
print("----------Conjunto de datos acerca del tipo de la flor Iris:----------")
print(tipo)
print("----------Conjunto de datos acerca de la longitud del Sépalo de la flor Iris:----------")
print(longitud_sepalo)
print("----------Conjunto de datos acerca del ancho del Sépalo de la flor Iris:----------")
print(ancho_sepalo)
print("----------Conjunto de datos acerca de la longitud del Petalo de la flor Iris:----------")
print(longitud_petalo)
print("----------Conjunto de datos acerca del ancho del Petalo de la flor Iris:----------")
print(ancho_petalo)

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

'''

V. Conclusiones
A. Reflexión sobre la importancia de comprender variables, tipos de datos,
expresiones y operadores en el análisis estadístico

El presente proyecto contiene muchas líneas de código pero el previo conocimiento de las herramientas es lo que hace que utilizar una base de datos se vuelva fácil y comprendible
para los demás colaboradores.

El conocimiento del tipo de datos y herramientas que se utilizan es demasiado importante debido a que gracias a esto el análisis se vuelve mucho más fácil de lo que parece. El
uso de los diferentes tipos de variables se usa dia a dia en una carrera como al Ingeniería Electrónica, es algo con lo que se está constantemente asociado, asimismo los diferentes tipos
de operadores y expresiones lógicas por lo que este proyecto ayuda a retomar lo que se está acostumbrado dia con dia como Ingeniero Electrónico y refuerza los conceptos para poder 
llevarlos a cabo en el análisis estadístico y comprender como los diferentes tipos de datos proporcionan informacion importante para lo que se está investigando.



VI. Referencias:

[1] "Iris". Flores Pedia. https://www.florespedia.com/iris (accedido el 20 de mayo de 2023).
[2] "Variables". PORTAL DE ACCESO a los servicios de la UM. https://webs.um.es/ldaniel/iscyp17-18/04a-variables.html#:~:text=Las%20variables%20numéricas,%20que%20son,quilos%20que%20pesa%20una%20persona. (accedido el 26 de mayo de 2023).
'''