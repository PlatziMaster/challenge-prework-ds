# Importando librerias
import os
import sys
import pathlib
import pandas as pd
import numpy as np



# Definición de funciones
def buscar_archivo():
        ruta_actual = os.getcwd()
        extension = ".csv"
        for idx, archivo in enumerate(os.listdir(ruta_actual)):
                if archivo.endswith(extension):
                        print(archivo+'\n')
                        return archivo

def cargar_archivo_df(archivo):
        # ruta_actual = os.getcwd()
        archivo = pd.read_csv(archivo)
        archivo_DF = archivo[['Estado','Clave SIINAH','Centro de trabajo','Año','Mes','Tipo de visitantes','Numero de visitas','Nacionalidad']]
        print(archivo_DF)
        return archivo_DF

def presentacion():
        print('-----------------------------------')
        print('Calculos de parámetros estadisticos')
        print('-----------------------------------')
        print('[1]-Totales por Estado por temporalidad (Mes y Año)')
        print('[2]-Totales por Estado por tipo de visitante')
        print('[3]-Totales por Estado por tipo de visitante y temporalidad (Mes y Año)')
        print('[4]-Totales por Centro de trabajo y temporalidad (Mes y año)')
        print('[5]-Totales por Centro de trabajo por tipo de visitante (Año)')
        print('[6]-Promedio de visitantes totales por estado (Mes y Año)')
        print('[7]-Promedio de visitantes por tipo de visitante, por estado (Mes y Año)')
        print('[8]-Porcentaje de visitantes por Recinto en visitantes por estado (total por mes).')
        print('[9]-Porcentaje de tipo de visitantes por mes y año')
        print('[10]-Porcentaje de tipo de visitantes por recinto (Mes y Año)')
        print('')
        proceso = int(input('\_: '))
        return proceso

# Programa Principal
if __name__ == '__main__':
        dir_actual = os.getcwd()
        print('\n*********************************************')
        print('GUARDAR EL ACHIVO EN EL SIGUIENTE DIRECTORIO:')
        print(len(dir_actual)*'-')
        print(dir_actual)
        print(len(dir_actual)*'-')
        # print('\n')
        archivo = buscar_archivo()
        df = cargar_archivo_df(archivo)
        
        seleccion = presentacion()

        if seleccion == 1:
                Estado_Tempralidad = df.groupby(['Estado', 'Año', 'Mes'])['Numero de visitas'].count()
                print(Estado_Tempralidad)
        elif seleccion == 2:
                Estado_Visitante = df.groupby(['Estado', 'Tipo de visitantes'])['Numero de visitas'].count()
                print(Estado_Visitante)
        elif seleccion == 3:
                Estado_Visitante_mes = df.groupby(['Estado', 'Tipo de visitantes', 'Año', 'Mes'])['Numero de visitas'].count()
                print(Estado_Visitante_mes)
        elif seleccion == 4:
                Centro_Temporalidad = df.groupby(['Centro de trabajo', 'Año', 'Mes'])['Numero de visitas'].sum()
                print(Centro_Temporalidad)
        elif seleccion == 5:
                Centro_TipoVisitante = df.groupby(['Centro de trabajo', 'Tipo de visitantes'])['Numero de visitas'].count()
                print(Centro_TipoVisitante)
        elif seleccion == 6:
                Prom_visitantes_Estados = df.groupby(['Estado', 'Mes', 'Año', 'Tipo de visitantes'])['Numero de visitas'].mean()
                print(Prom_visitantes_Estados)
        elif seleccion == 7:
                Prom_visitantes_Estados = df.groupby(['Tipo de visitantes', 'Estado', 'Mes', 'Año', 'Numero de visitas']).mean()
                print(Prom_visitantes_Estados)
        elif seleccion == 8:
                pass
        elif seleccion == 9:
                pass
        elif seleccion == 10:
                pass
        else:
                print('No escojiste un menu de la lista')
