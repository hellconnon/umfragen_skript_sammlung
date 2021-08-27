import pandas as pd
import sys
from pathlib import Path



# Enthält die Logik des ladens der Umfrage und dem export nach verschiedenen werten
def main(file = None, output_prefix = None):
    # Erstelle Ausgabeordner
    make_output_dir()
    # Wird nur ausgeführt wenn Skript über die Kommandozeile ausgeführt wird
    if __name__ == '__main__':
        file = get_input_file()
    # Wandle Datei in Pandas Dataframe um
    dataframe = read_dataframe(file)
    # Teile Daten nach Studiengang und speichere diese im Ausgabeordner
    split_and_save_studiengang(dataframe)
    # Teile Daten nach Tutorium und speichere diese im Ausgabeordner
    split_and_save_tutorium(dataframe)


# Liest die angegebene Datei in einen dataframe und gibt diesen zurück
def read_dataframe(file):
    if file.name.endswith('.csv'):
        output_dataframe = pd.read_csv(file, encoding="latin", sep=';')
    elif file.name.endswith('.xlsx'):
        output_dataframe = pd.read_excel(file)
    else:
        raise Exception('Die Angegebene Datei hat nicht das passende Format!' + " " + file.extension)

    # Löscht die erste Zeile der Daten, da dort nur murks drinsteht
    output_dataframe.drop(index=0, axis='index', inplace=True)
    return output_dataframe

# Lädt die über das Terminal angegebene Datei und gibt diese zurück. Wird nur bei Aufruf über das Terminal benötigt.
def get_input_file():
    terminal_arguments = sys.argv
    if len(terminal_arguments) > 1:
        file_path = terminal_arguments[1]
        file = open(file_path)
        return file
    
    raise Exception('Es wurde kein (korrekter) Pfad zu einer Datei angegeben!!')


# Erstellt den Output Ordner, in welchem die Daten gespeichert werden
def make_output_dir():
    Path('output/csv').mkdir(parents=True, exist_ok=True)
    Path('output/excel').mkdir(parents=True, exist_ok=True)


# Unterteilt die Eingabedatei nach Studiengang und schreibt die Daten für jeden Studiengang in den output Ordner
# Hier kann auch der output_mode manipuliert werden um die Daten als excel Datei zu speichern, einfach immer csv mit xls oder xlsx ersetzten
def split_and_save_studiengang(dataframe : pd.DataFrame, output_mode = 'csv'):
    # ---- Sucht sich alle gegebenen Antworten raus, auch die in Freitext ----
    studiengang_auswahl = dataframe.loc[:, 'Studiengang'].unique()

    # ---- Speichert für jeden gegebenen Studiengang eine Datei in Output ----
    for studiengang in studiengang_auswahl:
        current = dataframe.loc[dataframe['Studiengang'] == studiengang]
        # ---- kann geändert werden um eine andere Namenskonvention zu nutzen ----
        output_prefix = studiengang
        write_dataframe(dataframe=current, path=output_prefix, output_mode=output_mode)

# Unterteilt die Eingabedatei nach Tutoriumsnummer und schreibt die Daten für jedes Tutorium in den Output Ordner 
# Hier kann auch der output_mode manipuliert werden um die Daten als excel Datei zu speichern, einfach immer csv mit xls oder xlsx ersetzten
def split_and_save_tutorium(dataframe: pd.DataFrame, output_mode = 'csv'):
    tutorien = dataframe.loc[:, 'Tutoriumsnummer'].unique()
    
    for tut in tutorien:
        current = dataframe.loc[dataframe['Tutoriumsnummer'] == tut]
        output_prefix = 'Tutorium Nummer ' + str(tut)
        write_dataframe(dataframe=current, path=output_prefix, output_mode=output_mode)


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