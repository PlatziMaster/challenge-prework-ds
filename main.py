from tkinter import *

from tkinter import messagebox
from tkinter import filedialog

import pandas as pd

window = Tk()

window.title("Sebastian Rodriguez Marin - Data Science")

window.geometry('720x480')

def read_csv_file(file):
    data = pd.read_csv(file, encoding = 'ISO-8859-1') 
    # Preview the first 5 lines of the loaded data 
    data.head()
    btn.destroy()
    print(file)

def file_added():
    file = filedialog.askopenfilename()
    if file:
        messagebox.showinfo('CSV File', 'Archivo cargado con exito')
        read_csv_file(file)
    else:
        messagebox.showerror('Error', 'No se pudo cargar el archivo')    #shows error message

btn = Button(window,text='Open CSV File', command=file_added)

btn.place(relx=0.5, rely=0.5, anchor=CENTER)

window.mainloop()

