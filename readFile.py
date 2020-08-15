import pandas as pd
import numpy as np
import datetime
from datetime import date

df = pd.read_csv('INAH_detallado_2019.csv', sep=',', encoding='latin-1')

data_frame = pd.DataFrame(df, columns = ['Estado', 'Clave SIINAH', 'Centro de trabajo', 'Año', 'Mes', 'Tipo de visitantes', 'Número de visitas', 'Nacionalidad'])

print(data_frame)