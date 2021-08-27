import pandas as pd
import plotly as pt
import plotly.express as px
from umfragen_skript import read_xls, read_csv
pd.options.plotting.backend = 'plotly'
UEBUNGSBLATT_FRAGEN = ['', '']

def main():

    dataframe = read_csv()
    data = dataframe[['Studiengang', 'GBI Anzahl Abgegeben']]
    print(data)
    fig = px.bar(data)


    fig.write_image("output.png")
    
    

if __name__ == '__main__':
    main()