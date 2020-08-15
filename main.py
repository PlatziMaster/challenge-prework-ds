import tkinter as tk
from tkinter.filedialog import askopenfile

import pandas as pd





def button_load_csv_clicked( window):
    file_name = askopenfile(
                           filetypes =(("CSV File", "*.csv"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    
    data = pd.read_csv(file_name, sep=',') 


    data_frame = pd.DataFrame(data)

    #root = window

    table = tk.Text()
    table.place(x=250, y=200)
    table.insert(tk.INSERT, data_frame.to_string())
    
    #table.pack() 
    """
    try:
        with open(file_name,'r') as CSVFile:
            pass
    except:
        print("No existe el archivo")
        """

def run(window):
    
    window.title("Mi primera GUI con python")
    window.geometry("1000x1000")
    lbl = tk.Label( text = "Estadisticas del INAH", font=("Arial Bold", 26))
    lbl.place(x=390, y=0)

    btn_load_csv = tk.Button( text="Buscar archivo", bg="green", fg="white", font=("Arial Bold", 18), command=lambda:button_load_csv_clicked(window))
    #btn_load_csv = tk.Button( text="Buscar archivo", bg="green", fg="white", font=("Arial Bold", 18), command=button_load_csv_clicked)
    btn_load_csv.place(x=460, y=60)
    



if __name__ == '__main__':
    window = tk.Tk()
    run(window)
    window.mainloop()