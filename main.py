
import sqlite3

conn = sqlite3.connect('miFichero.db')

cursor = conn.cursor()

rows = cursor.execute('SELECT * FROM Alumnos WHERE nombre = "Itati"')

for row in rows:
    print(row)

cursor.close()
conn.close()
