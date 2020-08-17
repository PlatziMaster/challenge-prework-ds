# coding=utf-8
import pandas as pd
import numpy as np
import sys
#Tomamos el nombre del archivo pasado como argumento
file_name = sys.argv[1]

data = pd.read_csv(file_name)
to_drop = ['Siglas']
data.drop(to_drop, inplace=True, axis=1)
df = pd.DataFrame (data, columns = ['Estado','Mes', 'Año'])
print("Totales por Estado por temporalidad")
print(df)

dfV = pd.DataFrame (data, columns = ['Estado','Tipo de visitantes'])
print("Totales por Estado por tipo de visitante")
print(dfV)


dfTemp = pd.DataFrame (data, columns = ['Estado','Tipo de visitantes', 'Mes', 'Año'])
print("Totales por Estado por tipo de visitante y temporalidad (Mes y Año)")
print(dfTemp)

dfCenter = pd.DataFrame (data, columns = ['Centro de trabajo', 'Mes', 'Año'])
print("Totales por Centro de trabajo y temporalidad (Mes y año)")
print(dfCenter)

dfCenterTypo = pd.DataFrame (data, columns = ['Centro de trabajo','Tipo de visitantes', 'Año'])
print("Totales por Centro de trabajo por tipo de visitante (Año)")
print(dfCenterTypo)