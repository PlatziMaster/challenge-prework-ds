from IPython.display import display

import pandas as pd
import numpy as np
import plotly.express as px

import argparse

from utils import Utils
from utils import Query


def run(path):
    utils = Utils()
    df = utils.load_csv(path)
    query = Query(df)

    group_state_date = ['Estado', 'Ano', 'Mes']
    group_state_visit_type = ['Estado', 'Tipo de visitantes']
    group_state_date_visit_type = group_state_date + ['Tipo de visitantes']
    group_workcenter_date = ['Centro de trabajo', 'Ano', 'Mes']
    group_workcenter_date_visit_type = group_workcenter_date + ['Tipo de visitantes']
    group_workcenter_date_visit_type.remove('Mes')

    #  - Totales por Estado por temporalidad (Mes y Año)
    state_date = query.get_total(group_state_date)

    # - Totales por Estado por tipo de visitante
    state_visit_type = query.get_total(group_state_visit_type)

    # - Totales por Estado por tipo de visitante y temporalidad (Mes y Año)
    state_date_visit_type = query.get_total(group_state_date_visit_type)

    # - Totales por Centro de trabajo y temporalidad (Mes y año)    
    workcenter_date = query.get_total(group_workcenter_date)

    # - Totales por Centro de trabajo por tipo de visitante (Año)
    workcenter_date_visit_type = query.get_total(group_workcenter_date_visit_type)
    
    # - Promedio de visitantes totales por estado (Mes y Año)
    state_date_mean = query.get_average(group_state_date)

    # - Promedio de visitantes por tipo de visitante, por estado (Mes y Año)
    state_date_visit_type_mean = query.get_average(group_state_date_visit_type)

    # - Porcentaje de visitantes por Recinto en visitantes por estado (total por mes).
    query.get_percentage(['Estado', 'Mes'], ['Centro de trabajo'])
    
    # - Porcentaje de tipo de visitantes por mes y año
    query.get_percentage(['Ano', 'Mes'], ['Tipo de visitantes'])
    
    # - Porcentaje de tipo de visitantes por recinto (Mes y Año)
    query.get_percentage(['Centro de trabajo', 'Ano', 'Mes'], ['Tipo de visitantes'])


    # - Totales por Estado por temporalidad (Mes y Año)
    utils.plot_map(state_date, 'Visits per state')

    # - Promedio de visitantes totales por estado (Mes y Año)
    utils.plot_map(state_date_mean, 'Average of visits per state')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Challenge of DataScience for PlatziMaster')

    parser.add_argument('-f', '--file', required=True, help='Path to CSV')
    args = parser.parse_args()

    path = args.file
    run(path)
