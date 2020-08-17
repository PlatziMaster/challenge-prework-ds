import pandas as pd
import numpy as np

def extracting(csv_file):
    df = pd.read_csv(csv_file, encoding='utf-8')

    df.rename(columns={ 'Clave SIINAH' : 'clave',
                        'Centro de trabajo': 'centro_trabajo',
                        'A�o':'year', 
                        'Tipo de visitantes':'tipo_visitante',
                        'N�mero de visitas':'numero_visitas'}, inplace=True)

    df_work = df.copy(deep=True)
    df_work.drop(['Siglas'], axis=1, inplace=True)

    df_work['numero_visitas'] = df_work['numero_visitas'].str.replace(',', '')
    df_work['numero_visitas']=df_work['numero_visitas'].astype(int)

    return df_work

def operation(df, filas, columnas, valores, operacion):
    
    table = pd.pivot_table(df, index=filas, values=valores, columns=columnas, aggfunc=operacion)

    if operacion == 'sum':
        table['totales']=table.sum(axis=1)
    
    print(table)


def run():
    df_work = extracting('INAH_detallado_2019.csv')

    variables = list(df_work)

    print(f'''
    Bienvenid@
    
    Este es un programa para analizar los datos del Instituto Nacional de Antrología e Historia.

    Las variables con las que disponemos son:

    {variables}

    Para realizar una consulta responde las preguntas con los nombres exactos de la variable que deseas analizar.

    ''')    

    
    filas = [input('¿Qué variable quieres ver? ')]
    columnas = [input('¿Bajo que variable quieres filtrar? ')]
    valores = ['numero_visitas']
    operacion = 'sum'

    operation(df_work, filas, columnas, valores, operacion)



if __name__ == '__main__':
    run()