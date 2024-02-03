import sqlite3

# Verbindung zur SQLite-Datenbank herstellen

conn = sqlite3.connect("vornamen_database.db")

# Ein Cursor-Objekt erstellen, um SQL-Befehle auszuführen

cursor = conn.cursor()

# Eine SQL-Abfrage definieren, um die ersten 5 Zeilen aus der Tabelle 'vornamen' abzurufen

query = "SELECT * FROM vornamen LIMIT 5"

# Die Abfrage ausführen, um die ersten 5 Zeilen abzurufen

cursor.execute(query)

# Die Ergebnisse abrufen

rows = cursor.fetchall()

# Die Verbindung zur Datenbank schließen

conn.close()

# Die ersten 5 Zeilen ausgeben

for row in rows:
    print(row)