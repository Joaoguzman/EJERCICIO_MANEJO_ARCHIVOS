import csv
import json
from tabulate import tabulate
import pandas as pd
import time

with open ("data/mpg.csv", "r") as archivo:
    datos = csv.reader(archivo)
    datos = list(datos)


#print(  tabulate(datos))



with open ("data/mpg.json", "r") as archivo:
    data = json.load(archivo)
#print(datos_json)



#Agoritmo para transformar un diccionario a Lista de listas
# *** formato Json *** 

lista = []
recolector= []
for elementos in data.values():
    lista.append(elementos)
    
for elementos in lista:
    if type(elementos) == dict:
        auxiliar= []
        auxiliar2 = []
        for i,j in elementos.items():
            auxiliar.append(i)
            auxiliar2.append(j)
        recolector.append(auxiliar)
        recolector.append(auxiliar2)

a = ['manufacturer', 'model', 'displ', 'year', 'cyl', 'trans', 'drv', 'cty', 'hwy', 'fl', 'class']
otro_recolector = []
otro_recolector.append(a) #el titulo
for i in recolector:
    #Agrega solo si es difente al titulo
    if i != a:
        otro_recolector.append(i)
    
        

print(tabulate(otro_recolector))






#print(datos_lista)
#print(tabulate(list(datos_json)))
'''
print(len(datos_json))
#tabulate(datos_json)
df = pd.DataFrame(datos_json)
#print(df)
df = df.T 
print(df.head())'''