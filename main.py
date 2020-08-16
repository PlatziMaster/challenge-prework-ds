import tkinter as tk
from tkinter.filedialog import askopenfile

import pandas as pd

import numpy as np


def calc_state_temp(data_frame):
    pass

def button_load_csv_clicked( window):
    file_name = askopenfile(
                           filetypes =(("CSV File", "*.csv"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    
    data = pd.read_csv(file_name, sep=',', thousands=',', usecols = lambda column : column not in {"Siglas"}) 

    data_frame = pd.DataFrame(data )
    groups_estado_mes = data_frame[['Estado', 'Mes', 'Número de visitas']].groupby(['Estado', 'Mes']).sum()
    groups_estado_tipovisitante = data_frame[['Estado', 'Tipo de visitantes', 'Número de visitas']].groupby(['Estado', 'Tipo de visitantes']).sum()
    groups_estado_tipovisitante_temporalidad = data_frame[['Estado', 'Tipo de visitantes', 
        'Mes','Número de visitas']].groupby(['Estado', 'Tipo de visitantes', 'Mes']).sum()
    groups_centrotrabajo_temporalidad = data_frame[['Centro de trabajo', 'Mes', 'Año', 
    'Número de visitas']].groupby(['Centro de trabajo', 'Mes', 'Año']).sum()
    groups_centrotrabajo_tipovisitante = data_frame[['Centro de trabajo', 'Tipo de visitantes', 'Número de visitas']].groupby(
        ['Centro de trabajo', 'Tipo de visitantes']).sum()
    groups_promedio_visitantes_estado = data_frame[['Estado', 'Mes' ,'Año', 'Número de visitas']].groupby(
        ['Estado', 'Mes', 'Año']).agg(promedio_visitantes=('Número de visitas', np.mean))
    groups_promedio_vistantes_tipovisitante_estado_temp = data_frame[[
        'Estado', 'Tipo de visitantes' ,'Mes', 'Año', 'Número de visitas']].groupby(['Estado', 'Tipo de visitantes', 'Mes', 'Año']).agg(
            promedio_visitantes=('Número de visitas', np.mean)
        )
    groups_percentage_state_month_workcenter = data_frame[['Estado', 'Centro de trabajo','Mes', 'Año', 'Número de visitas']].groupby([
        'Estado', 'Centro de trabajo', 'Mes', 'Año'
    ]).agg(suma_totales=('Número de visitas', np.sum))
    groups_percentage_state_month_workcenter_calculate = groups_percentage_state_month_workcenter.groupby(level=0).apply(lambda x: 100*x/float(x.sum()))
    
    groups_percentage_visitorstype_month = data_frame[['Tipo de visitantes', 'Mes','Año', 'Número de visitas']].groupby([
        'Mes', 'Año', 'Tipo de visitantes', 
    ]).agg(porcentaje_visitantes=('Número de visitas', np.sum))
    groups_percentage_visitorstype_month_calculate = groups_percentage_visitorstype_month.groupby(level=0).apply(lambda x: 100*x/float(x.sum()))
   
    groups_percentage_visitorstype_workcenter = data_frame[['Tipo de visitantes','Centro de trabajo', 'Mes','Año', 'Número de visitas']].groupby([
        'Centro de trabajo','Tipo de visitantes','Mes', 'Año' 
    ]).agg(porcentaje_visitantes=('Número de visitas', np.sum))
    groups_percentage_visitorstype_workcenter_calculate = groups_percentage_visitorstype_workcenter.groupby(level=0).apply(lambda x: 100*x/float(x.sum()))
    
    
    print(groups_estado_mes)
    print(groups_estado_tipovisitante)
    print(groups_estado_tipovisitante_temporalidad)
    print(groups_centrotrabajo_temporalidad)
    print(groups_centrotrabajo_tipovisitante)
    print(groups_promedio_visitantes_estado)
    print(groups_promedio_vistantes_tipovisitante_estado_temp)
    print(groups_percentage_state_month_workcenter_calculate)
    print(groups_percentage_visitorstype_month_calculate)
    print(groups_percentage_visitorstype_workcenter_calculate)
    """
    table = tk.Text()
    table.config()
    table.place(x=20, y=200, width=1500)
    
    table.insert(tk.INSERT, data_frame.to_string())
"""
    

def run(window):
    
    window.title("Mi primera GUI con python")
    window.geometry("1800x1000")
    lbl = tk.Label( text = "Estadisticas del INAH", font=("Arial Bold", 26))
    lbl.place(x=590, y=0)

    btn_load_csv = tk.Button( text="Buscar archivo", bg="green", fg="white", font=("Arial Bold", 18), command=lambda:button_load_csv_clicked(window))
    #btn_load_csv = tk.Button( text="Buscar archivo", bg="green", fg="white", font=("Arial Bold", 18), command=button_load_csv_clicked)
    btn_load_csv.place(x=660, y=60)
    



if __name__ == '__main__':
    window = tk.Tk()
    run(window)
    window.mainloop()