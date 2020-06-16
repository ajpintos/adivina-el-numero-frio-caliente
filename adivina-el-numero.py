import random
import numpy as np

# genero un numero random del 1 al 100
x = random.randint(1,100)
oportunidades = 6
while oportunidades > 0:
    # Convierto el numero ingresado por el usuario en entero
    u = int(input("Ingrese un número del 1 al 100: "))
    # Quito una oportunidad en cada pasaje del bucle
    oportunidades = oportunidades - 1
    # Genero la lista Temperatura para que Numpy calcule la diferencia entre una variable y la otra
    temperatura = [x, u]
    # Numpy hace el calculo de diferencia y lo guardo en la variable temp
    temp = np.diff(temperatura)
    #print("La diferencia queda en", temp)
    #Paso el contenido de temp de lista a entero
    temp = int(temp)
    #COnvierto los resultados negativos en positivos
    temp = abs(temp)
    #print("En entero queda en ", temp)
    if temp == 0:
        print("FELICITACIONES!")
    if temp >= 1 and temp <= 10:
        print("Muy Caliente!!!")
    if temp >= 10 and temp <= 20:
        print("Caliente!")
    if temp >= 20 and temp <= 30:
        print("Tibio")
    if temp > 30:
        print("Frío")
    if u<x:
       #print("El numero Random es",x)
       print("El número es MAYOR, intente de nuevo")
       print("Te quedan", oportunidades, "oportunidades")
    if u>x:
       #print("El numero Random es", x)
       print("El número es MENOR, intente de nuevo")
       print("Te quedan", oportunidades, "oportunidades")
    if u == x:
       print("ACERTASTE!!!")
       break
if oportunidades == 0:
    print("Se te acabaron las oportunidades!")
