### Ejercicios

#1. Declare an empty list

vacia = list()
print(vacia) #[]

#2. Declare a list with more than 5 items
lista = ['Azul', 'Rojo', 'Verde','Morado','Rosa'] 

#3. Find the length of your list
print(len(lista)) # 5

#4. Get the first item, the middle item and the last item of the list
primer_color=lista[0]
print(primer_color) #Azul
middle_color=lista[2]
print(middle_color) #Verde
ultimo_color=lista[4]
print(ultimo_color) #Rosa

#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=["Iván",21,1.67,"Soltero","Av. del marquez"]
print(mixed_data_types)

#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, manzana, IBM, Oracle and Amazon.
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

#7. Print the number of companies in the list
print(len(it_companies)) #7

#8. Print the first, middle and last company
first=it_companies[0]
middle=it_companies[3]
last=it_companies[6]
print(first) #Facebook
print(middle) #Apple
print(last) #Amazon

#9. Reverse the list in descending order using reverse() method
precios=[500,550,600,650,700,750,800]
precios.reverse()
print(precios) #[800, 750, 700, 650, 600, 550, 500]

#10. Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']

back_end = ['Node','Express', 'MongoDB']

Union=back_end+front_end

print(Union) #['Node', 'Express', 'MongoDB', 'HTML', 'CSS', 'JS', 'React', 'Redux']