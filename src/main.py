import pandas as bd
import sys

# sys.argv[1]
datos = bd.read_csv(sys.argv[1], encoding='latin-1')
del datos['Siglas']
print(datos)

print(datos[['Estado', 'Año', 'Mes', 'Número de visitas']])
print(datos[['Estado', 'Número de visitas']])
print(datos[['Estado', 'Año', 'Mes', 'Tipo de visitantes']])
print(datos[['Centro de trabajo', 'Tipo de visitantes']])


