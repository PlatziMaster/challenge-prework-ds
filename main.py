import pandas as pd
import numpy as np

def read_csv(name):
  # 1 Read file by name
  data_frame = pd.read_csv(name)    
  # 2 Cleaning data frame
  data_frame = data_frame.convert_dtypes()    
  data_frame[["Estado","Año","Mes","Tipo de visitantes","Nacionalidad","Centro de trabajo"]] = data_frame[["Estado","Año","Mes","Tipo de visitantes","Nacionalidad","Centro de trabajo"]].astype("category")    
  data_frame["Número de visitas"] = pd.to_numeric(data_frame["Número de visitas"], errors="coerce")  
  # Fields to use: Estado, Clave SIINAH, Centro de trabajo, Año, Mes, Tipo de visitantes, Número de visitas y Nacionalidad
  fields_to_use = ['Estado', 'Clave SIINAH','Centro de trabajo', 'Año', 'Mes', 'Tipo de visitantes','Número de visitas','Nacionalidad']
  return data_frame[fields_to_use]

def totals_by_state_and_year(data_frame):
  # 3.1 Totals by state, month and year
  data_copy = data_frame.copy(deep=True)
  data_copy = data_copy.set_index(['Estado','Año', 'Mes']).sort_index()
  print("Totals by state, month and year")
  print(data_copy.head(5))

def totals_by_state_and_visitor(data_frame):
  # 3.2 Totals by state and visitor
  data_copy = data_frame.copy(deep=True)
  data_copy = data_copy.set_index(['Estado','Tipo de visitantes']).sort_index()
  print("Totals by state and visitor")
  print(data_copy.head(5))

def totals_by_state_visitor_and_year(data_frame):
  # 3.3 Totals by state, visitor, year and month
  data_copy = data_frame.copy(deep=True)
  data_copy = data_copy.set_index(['Estado','Tipo de visitantes','Año','Mes']).sort_index()
  print("Totals by state, visitor, year and month")
  print(data_copy.head(5))

def totals_by_workplace_and_year(data_frame):
  # 3.4 Totals by workplace, year and month
  data_copy = data_frame.copy(deep=True)
  data_copy = data_copy.set_index(['Centro de trabajo','Año','Mes']).sort_index()
  print("Totals by workplace, year and month")
  print(data_copy.head(5))

def totals_by_workplace_and_visitor(data_frame):
  # 3.5 Totals by workplace and visitors
  data_copy = data_frame.copy(deep=True)
  data_copy = data_copy.set_index(["Centro de trabajo", "Tipo de visitantes"]).sort_index()
  print("Totals by workplace and visitors")
  print(data_copy.head(5))

def run():
  data_frame = read_csv("INAH_detallado_2019.csv")
  totals_by_state_and_year(data_frame)  
  totals_by_state_and_visitor(data_frame)
  totals_by_state_visitor_and_year(data_frame)
  totals_by_workplace_and_year(data_frame)
  totals_by_workplace_and_visitor(data_frame)  

if __name__ == '__main__':
  run()