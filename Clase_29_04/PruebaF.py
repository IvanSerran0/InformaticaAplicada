import numpy as np
from scipy.stats import f_oneway

# Generamos dos muestras aleatorias con diferentes varianzas
muestra1 = np.random.normal(loc=0, scale=1, size=100)
muestra2 = np.random.normal(loc=0, scale=2, size=100)
# Realizamos la prueba F para comparar las varianzas
F, pvalue = f_oneway(muestra1, muestra2)
# Imprimimos los resultados
print("Estadístico F:", F)
print("Valor p:", pvalue)