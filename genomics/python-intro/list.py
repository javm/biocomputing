#!/usr/bin/python

"""
List: Lista es una estructura de datos nativa de python en la cuál puedes almacenar datos de cualquier tipo.
Es el equivalente a los arreglos en otros lenguajes de programación.
Cada elemento en la lista es referenciado por un índice que inicia en cero 0
"""

l = ['a', 'b', 'c', 'una cadena', 0, 1, 2, 'otra cadena']

# Para obtener la longitud o tamaño de la lista usamos la función:
n = len(l)
print(n)
# 8

#Obtenemos el último elemento de la lista usando el índice.
ultimo = l[len(l) - 1]
print(ultimo)
# 'otra cadena'

print(l[- 1])
# 'otra cadena'

# Obtenemos el primer elemento
print(l[0])

# Obtén el tercer elemento:
# tu código

"""
Después de que hemos almacenado nuestros datos en una lista
nuestro propósito es trabajar sobre esta colección de datos
comúnmente aplicando alguna operación sobre cada uno de sus datos.
A esta operación le llamamos iteración.
"""

#Iteración con 'for'
# Pensemos al keyword 'for' con el enunciado lógico 'para cada / for each'
a = ['a', 'b', 'c', 'd', 'e']
# para cada letra en la lista a, imprime...
for letra in a:
    print(letra)

# Otra forma es iterar usando los índices del arreglo ayudándonos de la función range
print("Usando 'range()'...")
for i in range(len(a)):
    print(i, a[i])

#Imprimiendo sólo los índices pares usando 'if'
print("Sólo índices pares...")
# Ejercicio: ejecuta en el REPL 'print(*range(len(a))) para ver el interior del range'
for i in range(len(a)):
    if(i%2 == 0):
        print(i, a[i])
# Índices impares
print("Sólo indices impares...")
for i in range(len(a)):
    if(i%2 != 0):
        print(i, a[i])

# Ejercicio: ver diferencias entre tupla y lista, i.e [] y ()
# Ejercicio: Inverstigar formas de multiplicar tuplas y listas

"""
'while' es otra forma de iterar sobre listas, depende de una condición que sea verdadera para ejecutar el bloque.
Puede leerse 'mientras ocurra mi codición haz lo siguiente'
"""
print("Iteración con while...")
i = 0
while(i < len(a)):
    print(a[i])
    i = i + 1

#control de un ventilador
#while(ventilador.prendido):
#  ventilador.gira()
#  if (ventilador.caliente):
#    # Apágalo
#    ventilador.prendido = false
