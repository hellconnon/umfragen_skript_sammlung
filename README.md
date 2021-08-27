# Eezi Skript Sammlung
Hier finden sich die Skripts, welche zur autmatischen Verarbeitung der Umfragedaten verwendet werden können.
Es können auch weitere Funktionen hinzukommen und auch weitere Abläufe automatisiert werden.


# Skript benutzen

## umfragen_skript.py

Das Skript ist dafür da um die Input Dateien zu lesen und nach den Vorgaben zu exportieren und in einen Output Ordner zu exportieren.
Es kann über die Kommandozeile mit einem relativem Pfad zur input-Datei gestartet werden.

```python umfragen_skript.py pfad/zu/input.csv```

oder 

```python umfragen_skript.py pfad/zu/input.xlsx```


außerdem kann der Dateityp der Exportdateien angepasst werden.


## use_input.py

Mit diesem Skript kann man einfach eine oder mehrere Input-Dateien in den Ordner 'Input' legen und dann per Doppelklick oder Kommandozeile das Skript ausfürhren.
Das Funktioniert aber nur, wenn es sich bei den Dateien um __.csv__ Dateien handelt.


# Erwartete Ordnerstruktur

Die Skripte erwarten eine gewisse Ordnerstruktur, die wie folgt aussieht:

    .
    ├── use_input.py                         # Skript um Input einfacher zu gestalten
    ├── umfragen_skript.py                   # Skript um Umfragen zu bearbeiten
    ├── README.txt                           # Diese Datei
    ├── requirements.txt                     # Enthält Abhängigkeiten, die mithilfe von pip installiert werden müssen
    ├── input                                # Ordner um Batch-processing zu verwenden
        ├── Beliebige_csv_Datei.csv
        ├── Beliebige_csv_Datei_2.csv


# Abhängigkeiten installieren

Um das Skript ausführen zu können werden unterschiedliche Module benötigt.
Diese können einfach mithilfe von pip installiert werden.

``` pip install -r requirements.txt ```