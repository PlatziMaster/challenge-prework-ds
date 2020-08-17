"""Importante librerias a usar"""


import tkinter as tk
from tkinter.filedialog import askopenfile

import pandas as pd

import numpy as np
import plotly.express as px

"""graficar_stackeds, using plotly lib
takes the dataframe, axis x, y, label and title as params"""

def draw_plot_stacked(df,x,y,color, nombre):
    fig2 = px.bar(df, x=x, y=y, color=color, title=nombre)
    fig2.show()

"""Function called the button is clicked"""
def button_load_csv_clicked( window):
    file_name = askopenfile(
                           filetypes =(("CSV File", "*.csv"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    #reading csv, specifies that the comma is the separator and also that in case of numbers, separates thousands. Excludes column siglas
    data = pd.read_csv(file_name, sep=',', thousands=',', usecols = lambda column : column not in {"Siglas"}) 
    #converting the raw data to a pandas dataframe
    data_frame = pd.DataFrame(data )


    #in this section I create a subdataframe for each statistic requiriment, I make use of the groupby() method, as well as sum and mean
    groups_state_temp = data_frame[['Estado', 'Mes', 'Número de visitas']].groupby(['Estado', 'Mes'], as_index=False).sum()
    groups_state_visitorstype = data_frame[['Estado', 'Tipo de visitantes', 'Número de visitas']].groupby(['Estado', 'Tipo de visitantes'], as_index=False).sum()
    groups_state_visitorstype_temp = data_frame[['Estado', 'Tipo de visitantes', #
        'Mes','Número de visitas']].groupby(['Estado', 'Tipo de visitantes', 'Mes'], as_index=False).sum()
    groups_workcenter_temp = data_frame[['Centro de trabajo', 'Mes', 'Año', 
    'Número de visitas']].groupby(['Centro de trabajo', 'Mes', 'Año'], as_index=False).sum()
    groups_workcenter_visitorstype = data_frame[['Centro de trabajo', 'Tipo de visitantes', 'Número de visitas']].groupby(
        ['Centro de trabajo', 'Tipo de visitantes'], as_index=False).sum()
    groups_workcenter_visitorstype = data_frame[data_frame['Número de visitas']!= 0]    
    groups_avg_visitors_per_state = data_frame[['Estado', 'Mes' ,'Año', 'Número de visitas']].groupby(
        ['Estado', 'Mes', 'Año']).agg(Visitas_Promedio=('Número de visitas', np.mean))
    groups_avg_visitors_visitorstype_per_month = data_frame[[
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
    
    #printing the subdataframes
    print(groups_state_temp)
    print(groups_state_visitorstype_temp)
    print(groups_state_visitorstype)
    print(groups_workcenter_temp)
    print(groups_workcenter_visitorstype)
    print(groups_avg_visitors_per_state)
    print(groups_avg_visitors_visitorstype_per_month)
    print(groups_percentage_state_month_workcenter_calculate)
    print(groups_percentage_visitorstype_month_calculate)
    print(groups_percentage_visitorstype_workcenter_calculate)

    #drawing plots
    draw_plot_stacked(groups_state_temp,"Mes", "Número de visitas", "Estado", "Visitantes mensuales por estado")
    draw_plot_stacked(groups_state_visitorstype, "Estado","Número de visitas", "Tipo de visitantes", "Tipo de visitantes por estado")
    draw_plot_stacked(groups_workcenter_temp, "Mes","Número de visitas", "Centro de trabajo", "Visitantes por centro de trabajo")
    draw_plot_stacked(groups_workcenter_visitorstype, "Centro de trabajo", "Número de visitas", "Tipo de visitantes", "Tipo de visitantes por centro de trabajo")
    
def run(window):
    #entry point. define the GUI elements
    window.title("Mi primera GUI con python")
    window.geometry("1800x1000")
    lbl = tk.Label( text = "Estadisticas del INAH", font=("Arial Bold", 26))
    lbl.place(x=590, y=0)

    btn_load_csv = tk.Button( text="Buscar archivo", bg="green", fg="white", font=("Arial Bold", 18), command=lambda:button_load_csv_clicked(window))
    btn_load_csv.place(x=660, y=60)
    



if __name__ == '__main__':
    window = tk.Tk()
    run(window)
    window.mainloop()