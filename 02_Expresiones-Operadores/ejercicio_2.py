# Expresiones y Operadores

## Expresiones.
'''
Las expresiones son combinaciones de constantes, variables, símbolos de operación, paréntesis y nombres de funciones especiales.

Una expresión consta de operandos y operadores. Según sea el tipo de objetos que manipulan, las expresiones se clasifican en: 

* aritméticas 
* relacionales
* lógicas
* carácter

El resultado de la expresión aritmética es de tipo numérico; el resultado de la expresión relacional y de una expresión lógica es de tipo lógico; el resultado de una expresión carácter es de tipo carácter.

Las expresiones aritméticas son análogas a las fórmulas matemáticas. Las variables y constantes son numéricas (real o entera) y las operaciones son las aritméticas.

* `+` - Este es el operador de suma y realiza la función de adicionar un operando al otro. 
* `-` - Este es el operador de resta y realiza la función de sustraer un operando de otro.
* `*` - Este es el operador de multiplicación y realiza la función de aumentar un operando en función de otro operando.
* `/` - Este es el operador de división y realiza la función de seccionar un operando en función de otro operando.
* `%` - Este es el operador de módulo y realiza la función de regresar el residuo de una división.
* `**` - Este es el operador de exponencial y permite obtener la potencia de un operando en función de otro operando.

A continuación se presentan algunos ejemplos de los operadores en código Python.
'''
### Operador +.

#python
print("-------Suma-------")
a = 7 + 3
print("a = 7 + 3 = ", a) #10
print("a ", type(7+3)) #<class 'int'>
a = 5
print("a = ", a)
b = 3
print("b = ",b)
c = a + b
print("c = 5 + 3 =", c) #8
print("c", type(5+3)) #<class 'int'>
print("3 + 4 = ", 3+4) #7
print(type(3+4)) #<class 'int'>


### Operador -.

#python
print("-------Resta-------")
a = 6 - 2
print("a =", 6-2) #4
print("a ", type(6-2) ) #<class 'int'>
a = 5
b = 3
c = a - b
print("c = 5 - 3 =", c) #
print("c", type(5-3)) #<class 'int'>
print(2-6)
print(type(2-6)) #<class 'int'>
#


### Operador *.

#python
print("-------Multiplicación-------")
a = 3 * 4
print("a = 3 * 4 =", a)
print("a ", type(a))
a = 6
b = 3
c = a * b
print("c = 6 * 3 =", c) #
print("c", type(5*7)) #<class 'int'>
print(5*7)
print(type(5*7)) #<class 'int'>
#


### Operador /.

#python
print("-------División-------")
a = 6 / 2
print("a = 6 / 2 =", a)
print("a ", type(a))
a = 5
b = 3
c = a / b
print("c = 5 / 3 =", c) #
print("c", type(5*7)) #<class 'int'>
print(10/3)
print(type(10/3)) #<class 'int'>
#

### Operador %.

#python
print("-------Residuo-------")
a = 8 % 4

print("a = 8 % 4 =", a)
print("a ", type(a))
a = 9
b = 2
c = a % b
print("c = 9 % 2 =", c) #
print("c", type(c)) #<class 'int'>
print(6%3)
print(type(6%3)) #<class 'int'>

#

### Operador **.

#python
print("-------Potencia-------")
a = 3 ** 3
print("a = 3 ** 3 =", a)
print("a ", type(a))
a = 2
b = 4
c = a ** b
print("c = 2 ** 4 =", c) #
print("c", type(c)) #<class 'int'>
print(4**3)
print(type(4**3)) #<class 'int'>
#

'''Expresiones relacionales

* `<` - Este es el operador de menor que, y se utiliza en las expresiones relacionales para saber si un operando es menor a otro operando.
* `>` - Este es el operador de mayor que, y se utiliza en las expresiones relacionales para saber si un operando es mayor a otro operando.
* `==` - Este es el operador de igual que, y se utiliza en las expresiones relacionales para saber si un operando es igual a otro operando.
* `!=` - Este es el operador desigual que, y se utiliza en las expresiones relacionales para saber si un operando es diferente a otro operando.
* `<=` - Este es el operador de menor igual que, y se utiliza en las expresiones relacionales para saber si un operando es menor o igual a otro operando.
* `>=` Este es el operador de mayor igual que, y se utiliza en las expresiones relacionales para saber si un operando es mayor igual a otro operando.

NOTA: Como resultado de la aplicación de las expresiones relacionales, se obtendrá como resultado una salida booleana, es decir `TRUE` o `FALSE`.

A continuación se presentan algunos ejemplos de las expresiones relacionales en código Python.
'''
### Operador <.

#python
print("-----Operador <-----")
a = 3 < 3
print(a) #False
print(type(a)) #<class 'bool'>
a = 2
b = 4
c = a < b
print(c) #True
print(4<3) #False
#

### Operador >.

#python
print("-----Operador >-----")
a = 4 > 2
print(a) #True
print(type(a)) #<class 'bool'>
a = 5
b = 7
c = a > b
print(c) #False
print(9>2) #True
#

### Operador ==.

#python
print("----- Operador == -----")
a = 5 == 5
print(a) #True
print(type(a)) #<class 'bool'>
a = 6
b = 9
c = a == b
print(c) #False
print(6==2) #False
#

### Operador !=.

#python
print("-----Operador != -----")
a = 4 != 2
print(a)#True
print(type(a))#<class 'bool'>
a = 5
b = 3
c = a != b
print(c)#True
print(8!=8)#False
#

### Operador <=.


#python
print("-----Operador <= -----")
a = 5 <= 3
print(a)#False
print(type(a))#<class 'bool'>
x = 7
y = 5
z = x <= y
print(z)#False
print(9<=4)#False
#

### Operador >=.

#python
print("-----Operador >= -----")
a = 2 >= 8
print(a)#False
print(type(a))#<class 'bool'>
a = 3
b = 4
c = a >= b
print(c)#False
print(7>=3)#True
#


## Expresiones lógicas.

'''
* `not` - Este es el operador lógico para realizar una negación, si el operando no se encuentra en el otro operando, la expresión se cumple y resulta en True, caso contrario, si la expresión no se cumple el resultado es False.
* `and` - Este es el operador lógico para realizar una conjugación, si cualquiera de los operandos presentes no se cumple en la expresión lógica, esta resulta en False, caso contrario, si toda la expresión lógica de conjugación se cumple el resultado es True.
* `or` - Este es el operador lógico para realizar una conjugación, si cualquiera de los operandos presentes no se cumple en la expresión lógica, esta resulta en False, caso contrario, si toda la expresión lógica de conjugación se cumple el resultado es True.
'''
### Operador and.

#python
print("-----AND-----")
print(4-1==3 and 5>6)#False
print(6+7 > 11 and 3==3)#True
print(type(6+7 > 11 and 3==3))#<class 'bool'>
#

### Operador or.

#python
print("-----OR-----")
print(4-1==3 or 5>6) #True
print(6+7 > 11 or 3==3)#True
#
print(type(6+7 > 11 or 3==3))#<class 'bool'>
### Operador not.

#python
print("-----NOT-----")
print(not 5>6) #True
print(not 5>4)#False
#
print(type(not 5>6))#<class 'bool'>
## Expresiones de carácter

'''A diferencia de las demás expresiones no existe un operador estático sino una búsqueda de secuencias, números o caracteres dentro de una variable.

Estas expresiones de búsqueda comúnmente llamadas expresiones regulares, sirven para captar ciertos elementos o patrones dentro de un valor.

Ejemplo:'''

#python
print("------------------------------------------------")
import re
frase = "Tengo 2 hijos que tienen 15 y 11 años"
patron = '[0-9]+' #Esta es una expresión regular
encontrado=re.findall(patron, frase)
print(encontrado) #['2', '15', '11']
print(type(encontrado)) #<class 'list'>

#
