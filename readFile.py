import pandas as pd
import numpy as np
import scipy
import scipy.stats

# Reading the document from CSV file in the directory
df = pd.read_csv('INAH_detallado_2019.csv', sep=',', encoding='latin-1')

# Getting the columns that will used in this development
data_frame = pd.DataFrame(df, columns = ['Estado', 'Clave SIINAH', 'Centro de trabajo', 'Año', 'Mes', 'Tipo de visitantes', 'Número de visitas', 'Nacionalidad'])
data_frame2 = pd.DataFrame(df, columns = ['Estado', 'Mes', 'Número de visitas'])

#Getting all the data from column 'Estado'
# Getting the unique result from column 'Estado'
# Getting the total states in their column
data_states = pd.DataFrame(df, columns = ['Estado'])
data_states_unique = df['Estado'].unique()
data_states_qty = len(data_states_unique)

# Getting months with unique results from their column
# Getting the quantity of months
data_months = df['Mes'].unique()
data_months_qty = len(data_months)

# Getting years with unique results from their column
# Getting the quantity of years
data_years = df['Año'].unique()
data_years_qty = len(data_years)

# Getting visitors with unique results from their column
# Getting the quantity of visitors
data_visitors = df['Tipo de visitantes'].unique()
data_visitors_qty = len(data_visitors)

# Converting the data types
df = df.convert_dtypes()

# Total per state per month and per year
total_state_by_month = df.groupby(['Estado', 'Mes'])['Número de visitas'].aggregate([np.sum])
total_state_by_year = df.groupby(['Estado', 'Año'])['Número de visitas'].aggregate([np.sum])

# Total per kind of visitor
total_state_by_kind_visitor = df.groupby(['Estado', 'Tipo de visitantes'])['Número de visitas'].aggregate([np.sum])

# Total per kind of visitor and time (year and month)
total_state_by_kind_visitor_year = df.groupby(['Estado', 'Tipo de visitantes' , 'Año'])['Número de visitas'].aggregate([np.sum])
total_state_by_kind_visitor_month = df.groupby(['Estado', 'Tipo de visitantes', 'Mes'])['Número de visitas'].aggregate([np.sum])

# Total per kind of work type and time (year and month)
total_state_by_kind_work_year = df.groupby(['Estado', 'Centro de trabajo' , 'Año'])['Número de visitas'].aggregate([np.sum])
total_state_by_kind_work_month = df.groupby(['Estado', 'Centro de trabajo', 'Mes'])['Número de visitas'].aggregate([np.sum])

# Total per kind of work type and kind of visitor
total_state_by_kind_work_visitor_year = df.groupby(['Estado', 'Centro de trabajo' , 'Tipo de visitantes', 'Año'])['Número de visitas'].aggregate([np.sum])

# Average per state
average_state = df.groupby(['Estado'])['Número de visitas'].aggregate([np.mean])

# Average per state and kind of visitors
average_state_visitors = df.groupby(['Estado', 'Tipo de visitantes'])['Número de visitas'].aggregate([np.mean])

# percentage per kind of visitor by month per state
percentage_visitors = total_state_by_kind_work_month / len(df)

# percentage per kind of work type and time (year and month)
percentage_visitors_month = df.groupby(['Tipo de visitantes', 'Mes'])['Número de visitas'].aggregate([np.sum]) / len(df)
percentage_visitors_year = df.groupby(['Tipo de visitantes', 'Año'])['Número de visitas'].aggregate([np.sum]) / len(df)

# percentage visitor per kind of work
percentage_visitors_work = df.groupby(['Tipo de visitantes', 'Centro de trabajo'])['Número de visitas'].aggregate([np.sum]) / len(df)

print(percentage_visitors_work)

""" for i in range(0, data_states_qty):
  for j in range(0, data_months_qty):
    data = data_frame2[data_frame2['Estado'] == data_states_unique[i]].mean()
    print(data.head(20))
    for k in range(0, len(df)):
      print(data_states_unique[i])
      print(data_months[j])
      print(data_frame[k]) """