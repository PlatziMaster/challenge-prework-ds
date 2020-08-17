import pandas as pd
datos = pd.read('INAH_detallado_2019.csv', header=0)
print(datos)

# import csv

# with open('INAH_detallado_2019.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     for row in csv_reader:
#         print(row)