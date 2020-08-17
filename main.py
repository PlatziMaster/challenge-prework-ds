import pandas as pd
import numpy as np
from tkinter import *
from tkinter import filedialog

def load_file():
  filename=filedialog.askopenfile(title="Selecciona archivo",filetypes = (("CSV Files","*.csv"),))
  df_read = pd.read_csv(filename.name, encoding ='latin', thousands=',')
  print(df_read)
  
  df_read.convert_dtypes().dtypes
  print(df_read[['Estado','Clave SIINAH', 'Centro de trabajo', 'Año', 'Mes', 'Tipo de visitantes', 'Número de visitas', 'Nacionalidad']])

if __name__ == '__main__':

  root=Tk()
  root.title('Reto ds')
  root.geometry("300x100")

  btn_cargar = Button(root, text="Cargar archivo", padx=40, pady=10, command=load_file)
  btn_cargar.pack()

  root.mainloop()

