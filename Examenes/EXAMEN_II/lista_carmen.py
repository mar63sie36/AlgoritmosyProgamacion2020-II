import numpy as np
import random
import time
import burbuja
import insercion
import mezcla

n = int(input("Ingrese el tamaño de la lista: "))
lista = []*n
for i in range(n):
    lista.append(random.randint(300, 1230))



lista_desordenada = lista
lista_desordenada_2 = lista
lista_desordenada_3 = lista
inicio = time.time()
burbuja.ordenamiento_burbuja(lista)
final_burbuja = time.time()-inicio

inicio = time.time()
insercion.ordenamiento_por_insercion(lista_desordenada)
final_insercion = time.time()-inicio


inicio = time.time()
mezcla.ord_por_mezcla(lista_desordenada_2)
final_mezcla = time.time()-inicio

inicio = time.time()
lista_desordenada_3.sort()
final_python = time.time()-inicio

print(f"el tiempo final de burbuja es {final_burbuja} y el de insercion {final_insercion} el tiempo final de mezcla {final_mezcla} y el final de python es {final_python}")