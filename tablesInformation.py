import pandas as pd
import numpy as np

def dfTable():
    return pd.read_csv('INAH_detallado_2019.csv', sep=',', encoding='latin-1')

def tblDataFrame():
    df = dfTable()
    return pd.DataFrame(df, columns = ['Estado', 'Clave SIINAH', 'Centro de trabajo', 'Año', 'Mes', 'Tipo de visitantes', 'Número de visitas', 'Nacionalidad'])

def dfConvert():
    df = dfTable()
    return df.convert_dtypes()

def total_state_by_month():
    df = dfConvert()
    total_state_by_month = df.groupby(['Estado', 'Mes'])['Número de visitas'].aggregate([np.sum])
    return total_state_by_month

def total_state_by_year():
    df = dfConvert()
    total_state_by_year = df.groupby(['Estado', 'Año'])['Número de visitas'].aggregate([np.sum])
    return total_state_by_year

def total_state_by_kind_visitor():
    df = dfConvert()
    total_state_by_kind_visitor = df.groupby(['Estado', 'Tipo de visitantes'])['Número de visitas'].aggregate([np.sum])
    return total_state_by_kind_visitor

def total_state_by_kind_visitor_year():
    df = dfConvert()
    total_state_by_kind_visitor_year = df.groupby(['Estado', 'Tipo de visitantes' , 'Año'])['Número de visitas'].aggregate([np.sum])
    return total_state_by_kind_visitor_year

def total_state_by_kind_visitor_month():
    df = dfConvert()
    total_state_by_kind_visitor_month = df.groupby(['Estado', 'Tipo de visitantes', 'Mes'])['Número de visitas'].aggregate([np.sum])
    return total_state_by_kind_visitor_month

def total_state_by_kind_work_year():
    df = dfConvert()
    total_state_by_kind_work_year = df.groupby(['Estado', 'Centro de trabajo' , 'Año'])['Número de visitas'].aggregate([np.sum])
    return total_state_by_kind_work_year

def total_state_by_kind_work_month():
    df = dfConvert()
    total_state_by_kind_work_month = df.groupby(['Estado', 'Centro de trabajo', 'Mes'])['Número de visitas'].aggregate([np.sum])
    return total_state_by_kind_work_month

def total_state_by_kind_work_visitor_year():
    df = dfConvert()
    total_state_by_kind_work_visitor_year = df.groupby(['Estado', 'Centro de trabajo' , 'Tipo de visitantes', 'Año'])['Número de visitas'].aggregate([np.sum])
    return total_state_by_kind_work_visitor_year

def average_state_month():
    df = dfConvert()
    average_state_month = df.groupby(['Estado', 'Mes'])['Número de visitas'].aggregate([np.mean])
    return average_state_month

def average_state_year():
    df = dfConvert()
    average_state_year = df.groupby(['Estado', 'Año'])['Número de visitas'].aggregate([np.mean])
    return average_state_year

def average_state_visitors_month():
    df = dfConvert()
    average_state_visitors_month = df.groupby(['Estado', 'Tipo de visitantes', 'Mes'])['Número de visitas'].aggregate([np.mean])
    return average_state_visitors_month

def average_state_visitors_year():
    df = dfConvert()
    average_state_visitors_year = df.groupby(['Estado', 'Tipo de visitantes', 'Año'])['Número de visitas'].aggregate([np.mean])
    return average_state_visitors_year

def percentage_visitors():
    df = dfConvert()
    percentage_visitors = total_state_by_kind_work_month() / len(df)
    return percentage_visitors

def percentage_visitors_month():
    df = dfConvert()
    percentage_visitors_month = df.groupby(['Tipo de visitantes', 'Mes'])['Número de visitas'].aggregate([np.sum]) / len(df)
    return percentage_visitors_month

def percentage_visitors_year():
    df = dfConvert()
    percentage_visitors_year = df.groupby(['Tipo de visitantes', 'Año'])['Número de visitas'].aggregate([np.sum]) / len(df)
    return percentage_visitors_year

def percentage_visitors_work_month():
    df = dfConvert()
    percentage_visitors_work_month = df.groupby(['Tipo de visitantes', 'Centro de trabajo', 'Mes'])['Número de visitas'].aggregate([np.sum]) / len(df)
    return percentage_visitors_work_month

def percentage_visitors_work_year():
    df = dfConvert()
    percentage_visitors_work_year = df.groupby(['Tipo de visitantes', 'Centro de trabajo', 'Año'])['Número de visitas'].aggregate([np.sum]) / len(df)
    return percentage_visitors_work_year


def percentage_visitors_work_year2():
    df = dfConvert()
    percentage_visitors_work_year = df.groupby(['Tipo de visitantes', 'Centro de trabajo', 'Año'])['Número de visitas'].aggregate([np.sum])
    return percentage_visitors_work_year




