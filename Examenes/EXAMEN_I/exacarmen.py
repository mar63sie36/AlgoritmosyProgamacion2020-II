#importar archivos
import casos
import time


#Generar lista con números de sucesión de fibonacci
lista = int(input("Ingrese número n:"))
#control de tiempo caso1
inicio = time.time() 
casos.caso1(lista)
tiempo_caso1 = time.time() -inicio
#control de tiempo caso2
inicio = time.time()
casos.caso2(lista)
tiempo_caso2 = time.time() -inicio


#Para generar el resultado del tiempo entre ambos
if tiempo_caso1>tiempo_caso2:
    #Si el tiempo del caso2 es menor
    print("Es mejor el tiempo  del caso 2")
else: 
    #Si el tiempo del caso1 es mejor
    print("Es mejor el tiempo del caso 1")
