# Escribe tu código aquí :-)
"""
numeros = [1,2,3,4,5]
nombres = ["Daniel", "Ricardo", "Alvaro", "Enrique","Hugo"]
registros = ["registro1", 1, "registro2", 2]

#.pop() .remove() .index() .append()
# len()

lista = []
otra_lista = list()

'''
# comanto list() : Conversion para tipo list
palabra = "palabra"
print(type(palabra))
listaPalabra = list(palabra)

print("Tipo de la variable palabra:", type(palabra))
print("Tipo de la variable listaPalabra:", type(listaPalabra))

print("Valor de la variable palabra:", palabra)
print("Valor de la variable listaPalabra:",listaPalabra)
'''
# comando .append() : Añadir nuevo elemento
lista = list()
print(lista)
lista.append(20)
print(lista)

# comando len() : Consultar la longitud de una lista
palabra = "palabra"
print(type(palabra))
listaPalabra = list(palabra)
longitud = len(palabra)
print(listaPalabra)
print("Longitud de listaPalabra", longitud)

#.pop() : elimina por la posición

listaPalabra.pop(2)
print("Lista palabra despues del .pop(): ",listaPalabra)

#.remove() : elimina por el valor del elemento
listaPalabra.remove("b")
print("Lista palabra despues del .remove(): ",listaPalabra)

#.index() : mirar en que posicion de la lista se encuntra un elemento
print("Posición del elemento 'a' en la lista: ", listaPalabra.index("a"))
"""
###############################
nombre = "Ricardo"
print(type(nombre))
listaNombre = list(nombre)
# ["D", "a", "n", "i", "e", "l"]
for i in range(0,len(listaNombre)):
    print(listaNombre[i])

for letra in listaNombre:
    print(letra)

nombre = "Clovis Magno"
print(type(nombre))
listaNombre = list(nombre)
print(listaNombre)

l = "o"










