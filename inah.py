import pandas as pd
import numpy as np

def df_readcsv():
    return pd.read_csv('INAH_detallado_2019.csv')
    
def data_frame():
    df = df_readcsv()
    return pd.DataFrame(df, columns = ['Estado', 
                                      'Clave SIINAH', 
                                      'Centro de trabajo', 
                                      'Año', 
                                      'Mes', 
                                      'Tipo de visitantes', 
                                      'Número de visitas', 
                                      'Nacionalidad'])