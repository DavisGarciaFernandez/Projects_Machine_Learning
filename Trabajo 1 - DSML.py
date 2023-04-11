#!/usr/bin/env python
# coding: utf-8

# EJERCICIO 1
# 
# Realizar un programa que contenga una lista con 10 valores enteros. Informar de cuántos de ellos son superiores a 100.

# In[7]:


lista = [56, 102, 78, 400, 25, 90, 200, 150, 10, 300]

contador = 0

for valor in lista:
    if valor > 100:
        contador += 1
        
print("Hay", contador, "números mayores que 100 en la lista.")


# EJERCICIO 2
# 
# Una empresa divide el trabajo en dos turnos (mañana y tarde) en las que trabajan 6 empleados (3/turno). Agrupar los sueldos de los empleados en dos listas y mostrar después las listas por consola.

# In[6]:


sueldo = [5000, 6000, 7000, 8000, 9000, 10000]

turno_mañana = sueldo[0:3]
turno_tarde = sueldo[3:6]

print("Sueldos de los empleados del turno mañana: ", turno_mañana)
print("Sueldos de los empleados del turno tarde: ", turno_tarde)


# EJERCICIO 3
# 
# Realizar un programa que permita crear una lista y almacenar los nombres de n países. Ordenar alfabéticamente la lista e imprimirla.

# In[8]:


N = int(input("Ingrese el número de países: "))

paises = []

for i in range(N):
    pais = input("Ingrese el nombre del país: ")
    paises.append(pais)

paises.sort()

print("Lista de paises ordenado alfabeticamente: ")
for pais in paises:
    print(pais)


# EJERCICIO 4
# 
# Realizar un programa que permita cargar una lista de n elementos enteros. Ordenarla de mayor a menor e imprimir los resultados obtenidos. Informar también del número mayor y del número menor.

# In[1]:


n = int(input("Ingrese la cantidad de elementos que quiere ingresar: "))

lista = []

for i in range(n):
    elemento = int(input("Ingrese un elemento: "))
    lista.append(elemento)

lista_ordenada = sorted(lista, reverse=True)

print("La lista ordenada de mayor a menor es:")
print(lista_ordenada)

numero_mayor = max(lista)
numero_menor = min(lista)

print("El número mayor en la lista es:", numero_mayor)
print("El número menor en la lista es:", numero_menor)


# EJERCICIO 5
# 
# Realizar un programa que permita cargar n países y la cantidad de habitantes que residen en cada uno. Imprimir cada país con su número de habitantes correspondiente.

# In[9]:


n = int(input("Ingrese la cantidad de países que quiere ingresar: "))

paises = {}

for i in range(n):
    pais = input("Ingrese un país: ")
    habitantes = int(input("Ingrese la cantidad de habitantes de {}:".format(pais)))
    paises[pais] = habitantes

print("Países y su cantidad de habitantes correspondiente:")
for pais, habitantes in paises.items():
    print("{} - {} habitantes".format(pais, habitantes))

