## In this first part we import the libraries for our proyect. We name our panda library as pd in order to make it managable.

import csv
import pandas as pd

def read():

## This function has the only purpose of opening the data on a raw fashion in the terminal. In this case we use the .DictReader as our main
## method to do so and a simple for loop to iterate through each of the lines in the csv file. 

        with open("INAH_detallado_2019.csv", mode="r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                line_count = 0
                for row in csv_reader:
                        if line_count == 0:
                                print(row["Estado"], row["Clave SIINAH"], row["Centro de trabajo"], row["Año"], row ["Mes"], row ["Tipo de visitantes"],
                                row ["Número de visitas"], row ["Nacionalidad"])

def clean():

        ## Using the pandas library, we take the raw data from the last function, clean it and make it more presentable.
        ## Is important to keep the encoding variable in order to avoid an error while running the code. 
        ## Quick note: This is the first time I ever use pandas. 

        clean_db = pd.read_csv ("INAH_detallado_2019.csv", encoding = "ISO-8859-1")
        print(clean_db)

def analytics():

        ## The anaylitics function has the only purpose of presenting organized data. In this case, I focused only on grouping and counting
        ## the total number of visitors on each state -- as well as the nationality. 
        ## Here you will only find a simple table which will be visible in the terminal. 

        clean_db = pd.read_csv ("INAH_detallado_2019.csv", encoding = "ISO-8859-1")
        columns = clean_db.columns
        groupby_state = clean_db.groupby("Estado")["Número de visitas"].count()
        groupby_nationality = clean_db.groupby("Nacionalidad")["Número de visitas"].count()

        print(groupby_state)
        print(groupby_nationality)

def run():

        ## Our run function contains a simple menu in order to let the use to easily decide what action to execute. 
        ## We keep it on a while loop, so that the program keeps running even after executing one of the four options available. 
        ## It's important to keep the .upper method, so that the menu options run smoothley no matter if the user type mayus or minus keys.

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
                        while action != "R" or "O" or "S" or "E":
                                new_action = input("That's an invalid option. Press any key to try again ")
                                break


if __name__ == "__main__":
    run()

    ## Here we only invoke our run function to start our program.
    ## Thank you for reviewing my code. Looking forward to become a legendary data scientist. 