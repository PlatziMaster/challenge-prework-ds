import pandas as pd

data = pd.read_csv("INAH_detallado_2019.csv")
data_frame = pd.DataFrame(data)

# Totales por Estado por temporalidad (Mes y Año)
state_month = data_frame[['Estado', 'Mes', 'N�mero de visitas']].groupby(['Mes', 'Estado']).sum()
print(state_month)

#Totales por Estado por tipo de visitante
state_year = data_frame[['Estado', 'A�o', 'N�mero de visitas']].groupby(['A�o', 'Estado']).sum()
print(state_year)

#Totales por Estado por tipo de visitante y temporalidad (Mes y Año)
visitor_temp = data_frame[['Estado', 'Tipo de visitantes', 'N�mero de visitas']].groupby(['Tipo de visitantes', 'Estado'])
print(visitor_temp)

# Totales por Centro de trabajo y temporalidad (Mes y año)
job_temp_month = data_frame[['Centro de trabajo', 'Mes', 'N�mero de visitas']].groupby(['Mes', 'Centro de trabajo']).sum()
print(job_temp_month)

# Totales por Centro de trabajo por tipo de visitante (Año)
job_temp_year = data_frame[['Centro de trabajo', 'A�o', 'N�mero de visitas']].groupby(['A�o', 'Centro de trabajo']).sum()
print(job_temp_year)

# Promedio de visitantes totales por estado (Mes y Año)
job_visitor = data_frame[['Centro de trabajo', 'A�o', 'Tipo de visitantes', 'N�mero de visitas']].groupby(['A�o', 'Tipo de visitantes', 'Centro de trabajo']).sum()
print(job_visitor)

# Promedio de visitantes por tipo de visitante, por estado (Mes y Año)
visitors_per_year = data_frame[['Estado', 'Mes', 'N�mero de visitas']].groupby(['Mes', 'Estado']).sum().mean()
print(state_month)