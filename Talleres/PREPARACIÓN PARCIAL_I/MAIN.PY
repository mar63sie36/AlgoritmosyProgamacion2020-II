import codigos
import time

lista =[2,3,4,5,6,2,7]
inicio = time.time() 
codigos.caso1(lista)
tiempo_caso1 = time.time() -inicio
inicio = time.time() 
codigos.caso2(lista)
tiempo_caso2 = time.time() -inicio

if tiempo_caso1>tiempo_caso2:
  print("Es mejor el caso 2")
else: 
  print("Es mejor el caso 1")

mensaje = "Hola todo el mundo este mensaje es normal"
inicio = time.time() 
codigos.caso3(mensaje)
tiempo_caso3 = time.time() -inicio
inicio = time.time() 
codigos.caso4(mensaje)
tiempo_caso4 = time.time() -inicio


if tiempo_caso3>tiempo_caso4:
  print("Es mejor el caso 4")
else: 
  print("Es mejor el caso 3")
