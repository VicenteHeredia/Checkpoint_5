#Cree un bucle For de Python.
print()

alphabet = 'abcdefg'
for letter in alphabet:
    print(letter)
#Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.
print()

numbers = [1, 5, 3]

sum = 0
for item in numbers:
    sum  += item

print(sum)


#Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.
print()

sum = lambda a, b, c: a+b+c

print(sum(1, 5, 3))


#Utilizando la siguiente lista y variable,
#determine si el valor de la variable coincide o no con un valor de la lista.
print()

name = 'Henry'
list_name = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

if name in list_name:
    print(f'{name} is on the list')
else:
    print(f'The name not is on the list')


