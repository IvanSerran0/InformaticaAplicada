print("-----------------------------------------------------")
fact='Esto es una cadena'
fact_two=fact+ ' esto es otra cadena'
print(fact_two
)

print("-----------------------------------------------------")
a='Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.'.replace('Celsius', 'C')
print(a)
print("-----------------------------------------------------")
cad='The "near side" is the part of the Moon that faces the Earth'
print(cad)
print("-----------------------------------------------------")
frase="""We only see about 60% of the Moon's surface, this is known as the "near side"."""
print(frase)

print("-----------------------------------------------------")
multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)

print("------------------Metodos String-----------------------------------")
print('temperatures and facts about the moon'.title())

heading = 'temperatures and facts about the moon'
heading.title()

print("------------------Dividir una cadena-----------------------------------")
temperatures = '''Daylight: 260 F
... Nighttime: -280 F'''
print(temperatures .split())

print("-------------------Ciclo FOR----------------------------------")
mars_temperature = 'The highest temperature on Mars is about 30 C'

for item in mars_temperature.split():
    if item.isnumeric():
        print(item)
