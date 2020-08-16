import csv

def read():

        with open('INAH_detallado_2019.csv', mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                line_count = 0
                for row in csv_reader:
                        if line_count == 0:
                                print(row["Estado"], row["Clave SIINAH"], row["Siglas"], row["Año"], row ["Mes"], row ["Tipo de visitantes"],
                                row ["Número de visitas"], row ["Nacionalidad"])

def run():

    while(True):

                action = str(input("""
                        ••••••••••••••••••••••••••••••••••••••••••••••
                                            INAH
                        ••••••••••••••••••••••••••••••••••••••••••••••

                        Welcome to the National Institute of Anthropology and History. What do you want to do today?

                        [R]ead the database (Beware that data will be showed raw and in Spanish)
                        [E]xit

                        """).upper())
        
                if action == "R":
                        read()
                elif action == "E":
                        quit()
                else:
                        while action != "R" or "E":
                                new_action = input("That's an invalid option. Press any key to try again ")
                                break


if __name__ == "__main__":
    run()