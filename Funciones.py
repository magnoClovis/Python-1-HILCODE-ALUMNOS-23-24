
numero = 6

if numero % 2 == 0:
    print("El numero",numero,"es par.")
else:
    print("El numero",numero,"es impar.")

#############################################################
# Definición y uso de función sin parametros o return
def par_o_impar():
    numero = int(input("Escribe un número "))
    if numero % 2 == 0:
        print("El numero",numero,"es par.")
    else:
        print("El numero",numero,"es impar.")

par_o_impar()

#############################################################
# Definición y uso de función con return, sin parametros

def par_o_impar1():
    numero = int(input("Escribe un número "))
    if numero % 2 == 0:
        print("El numero",numero,"es par.")
    else:
        print("El numero",numero,"es impar")

    return numero

numero = par_o_impar1()
print("El numero es:",numero)

#############################################################
# Definición y uso de función con return y parámetros
def par_o_impar(numero):
    if numero % 2 == 0:
        print("El numero",numero,"es par.")
    else:
        print("El numero",numero,"es impar.")


n = int(input("Escribe un número "))
par_o_impar(numero=n)

##############################################################

def registro():
    nombre = input("Cuál es tu nombre?")
    apellido = input("Cuál es tu apellido?")

    return nombre, apellido

n, a = registro()

print(n)
print(a)

def resta(num1, num2):
    resultado = num1 - num2
    return resultado

resultado = resta(num2 = 5, num1 = 8)
print(resultado)
















