import csv
import pandas as pd 


def mostrarArchivoTerminal():
    with open('INAH_detallado_2019.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def crearDataFrame():
    print('Data en CSV-----------------------------------------------')
    dataINAH = pd.read_csv('INAH_detallado_2019.csv', engine='python')
    dataINAH = dataINAH.drop(['Siglas'],axis=1)
    print(dataINAH)
    return dataINAH

def filtrarData(data,campo='Estado',valor='Aguascalientes'):
    print(f'\nData filtrada por {campo} [{valor}]-----------------------------------------------')
    filtro = data[campo] == valor
    return data[filtro]

def totalesEstadoTemporalidad(data):

if __name__ == '__main__':
  INAHDataFrame = crearDataFrame()
  print(filtrarData(INAHDataFrame))