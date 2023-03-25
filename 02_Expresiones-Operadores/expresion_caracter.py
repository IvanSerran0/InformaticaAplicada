import re
frase = "juanito96@hotmail.com.mx"
patron = '[0-9]+' #Esta es una expresión regular //////////Esta buscando numeros de cero a nueve
exp_final = re.findall(patron, frase)
print(exp_final) #['96']
print(type(exp_final)) #<class 'list'>
