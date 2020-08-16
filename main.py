import csv
import pandas as database
import plotly.express as px

def read():

        with open("INAH_detallado_2019.csv", mode="r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                line_count = 0
                for row in csv_reader:
                        if line_count == 0:
                                print(row["Estado"], row["Clave SIINAH"], row["Centro de trabajo"], row["Año"], row ["Mes"], row ["Tipo de visitantes"],
                                row ["Número de visitas"], row ["Nacionalidad"])

def clean():

        clean_db = database.read_csv ("INAH_detallado_2019.csv", encoding = "ISO-8859-1")
        print(clean_db)

def analytics():

        clean_db = database.read_csv ("INAH_detallado_2019.csv", encoding = "ISO-8859-1")
        chart = px.data()

        visitors = px.bar(chart, x="")

def run():

    while(True):

                action = str(input("""
                        ••••••••••••••••••••••••••••••••••••••••••••••
                                            INAH
                        ••••••••••••••••••••••••••••••••••••••••••••••

                        Welcome to the National Institute of Anthropology and History. What do you want to do today?

                        [R]ead raw data (Beware that data is showed in Spanish)
                        [O]pen clean data (Beware that data is showed in Spanish)
                        [S]ee data analytics
                        [E]xit

                        """).upper())
        
                if action == "R":
                        read()
                elif action == "O":
                        clean()
                elif action == "S":
                        analytics()
                elif action == "E":
                        quit()
                else:
                        while action != "R" or "E":
                                new_action = input("That's an invalid option. Press any key to try again ")
                                break


if __name__ == "__main__":
    run()