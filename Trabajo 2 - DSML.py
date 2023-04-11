#!/usr/bin/env python
# coding: utf-8

# EJERCICIO 1
# 
# Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla una serie con los datos de las ventas indexada por los años, antes y después de aplicarles un descuento del 10%.

# In[1]:


import pandas as pd

inicio = int(input('Introduce el año inicial: '))
fin = int(input('Introduce el año final: '))
ventas = {}
for i in range(inicio, fin+1):
    ventas[i] = float(input('Introduce las ventas del año ' + str(i) +': '))
ventas = pd.Series(ventas)
print('Ventas\n', ventas)
print('Ventas con descuento\n', ventas*0.9)


# EJERCICIO 2
# 
# Escribir una función que reciba un diccionario con las notas de los alumno de un curso y devuelva una serie con la nota mínima, la máxima, media y la desviación típica.

# In[5]:


import pandas as pd

def estadistica_notas(notas):
    notas = pd.Series(notas)
    estadisticos = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], index=['Min', 'Max', 'Media', 'Desviación típica'])
    return estadisticos

notas = {'Juan': 9, 'María': 6.5, 'Pedro': 4, 'Carmen': 8.5, 'Luis': 5}
print(estadistica_notas(notas))


# EJERCICIO 3
# 
# Escribir una función que reciba un diccionario con las notas de los alumnos de un curso y devuelva una serie con las notas de los alumnos aprobados ordenadas de mayor a menor.

# In[4]:


import pandas as pd

def notas_aprobados(notas):
    df = pd.DataFrame.from_dict(notas, orient="index", columns=["nota"])
    df_aprobados = df[df["nota"] >= 5]
    df_aprobados_sorted = df_aprobados.sort_values("nota", ascending=False)
    return df_aprobados_sorted["nota"]

notas = {"David": 10, "Ivonne": 10.5, "Billy": 12, "Estrella": 18.5, "Jadher": 15}
print(notas_aprobados(notas))

