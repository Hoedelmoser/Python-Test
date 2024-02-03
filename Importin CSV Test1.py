
import requests

import pandas as pd

import numpy



# Definiere die URL der CSV-Datei aus dem Internet

csv_url = "https://data.statistik.gv.at/data/OGDEXT_VORNAMEN_1.csv"

response = requests.get(csv_url)


if response.status_code == 200:

    # Save the CSV data to a file or use it as needed

    with open("vornamen_by_year.csv", "wb") as file:

        file.write(response.content)

    # Load the CSV data into a pandas DataFrame with the correct delimiter (;)

    df = pd.read_csv("vornamen_by_year.csv", delimiter=";")

else:

    print("Fehler beim Abrufen der CSV-Daten.")



print(df.head())  # Anzeigen der ersten Zeilen des DataFrames


df.shape