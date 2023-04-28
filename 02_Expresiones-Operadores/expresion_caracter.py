import re
frase = "juanito@hotmail.com.mx"
patron = '[a-z]+' #Esta es una expresión regular //////////Esta buscando numeros de cero a nueve
exp_final = re.findall(patron, frase)
print(exp_final) #['96']
print(type(exp_final)) #<class 'list'>



import numpy as np