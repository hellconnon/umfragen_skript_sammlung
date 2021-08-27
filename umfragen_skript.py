import pandas as pd
import sys
from pathlib import Path



# Enthält die Logik des ladens der Umfrage und dem export nach verschiedenen werten
def main(file = None, output_prefix = None):
    make_output_dir()
    if file:
        print(file.name)
    if not file:
        file = get_input_file()

    if file.name.endswith('.csv'):
        dataframe = read_csv(file)
    elif file.name.endswith('.xlsx'):
        dataframe = read_xls(file)
    else:
        raise Exception('Die Angegebene Datei hat nicht das passende Format!' + " " + file.extension)

    split_and_save_studiengang(dataframe)
    split_and_save_tutorium(dataframe)

def get_input_file():
    terminal_arguments = sys.argv
    if len(terminal_arguments) > 1:
        file_path = terminal_arguments[1]
        file = open(file_path)
        return file
    
    raise Exception('Es wurde kein (korrekter) Pfad zu einer Datei angegeben!!')


def make_output_dir():
    # ---- erstelle output directory ----
    Path('output/csv').mkdir(parents=True, exist_ok=True)
    Path('output/excel').mkdir(parents=True, exist_ok=True)

def read_csv(path = 'input_csv.csv'):
    output_dataframe = pd.read_csv(path, encoding="latin", sep=';')
    output_dataframe.drop(index=0, axis='index', inplace=True)
    return output_dataframe


def read_xls(path = 'input_xls.xlsx'):
    output_dataframe = pd.read_excel(path)
    output_dataframe.drop(index=0, axis='index', inplace=True)
    return output_dataframe

# Unterteilt die Eingabedatei nach Studiengang und schreibt die Daten für jeden Studiengang in den output Ordner
def split_and_save_studiengang(dataframe : pd.DataFrame, output_mode = 'csv'):
    studiengang_auswahl = dataframe.loc[:, 'Studiengang'].unique()

    for studiengang in studiengang_auswahl:
        current = dataframe.loc[dataframe['Studiengang'] == studiengang]
        output_path = studiengang
        write_dataframe(dataframe=current, path=output_path, output_mode=output_mode)

# Unterteilt die Eingabedatei nach Tutoriumsnummer und schreibt die Daten für jedes Tutorium in den Output Ordner 
def split_and_save_tutorium(dataframe: pd.DataFrame, output_mode = 'csv'):
    tutorien = dataframe.loc[:, 'Tutoriumsnummer'].unique()
    
    for tut in tutorien:
        current = dataframe.loc[dataframe['Tutoriumsnummer'] == tut]
        output_path = 'Tutorium Nummer ' + str(tut)
        write_dataframe(dataframe=current, path=output_path, output_mode=output_mode)


# Schreibt den gegebenen Abschnitt als Datei
def write_dataframe(dataframe, path, output_mode):
    # ---- Exportiert die Datei als CSV Datei ----
    if output_mode == 'csv':
        dataframe.to_csv('output/csv/' + path + ".csv", encoding='latin1')
    # ---- Exportiert die Datei als Excel Datei ----
    elif output_mode == 'xlsx' or 'xls':
        dataframe.to_excel('output/excel/' + path + ".xlsx")
    else:
        raise Exception("Die gegebene Dateiendung kann nicht exportiert werden!" + " " + output_mode)



if __name__ == "__main__":
    main()