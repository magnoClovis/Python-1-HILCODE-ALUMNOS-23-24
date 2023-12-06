alumnos = []

tam = len(alumnos)

while len(alumnos) < 5:
    alumnos.append(input("Cual es el nombre del alumno? "))

print(alumnos)

#############################################
alumnos = []
fin = False

while fin != True:
    alumnos.append(input("Cual es el nombre del alumno? "))
    res = input("Queda algún alumno más?")
    if res == "no":
        fin = True
print(alumnos)
##############################################
alumnos = []
fin = False

while fin != True:
    alumnos.append(input("Cual es el nombre del alumno? "))
    if input("Queda algún alumno más?") == "no":
        fin = True
print(alumnos)
#################################################
alumnos = []
fin = False

while not fin:
    alumnos.append(input("Cual es el nombre del alumno? "))
    if input("Queda algún alumno más?") == "no":
        fin = True
print(alumnos)




