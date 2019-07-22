import sqlite3

database = sqlite3.connect("data.db")
cursor = database.cursor()
data = cursor.execute("SELECT * FROM DATA")
print(list(data))
database.close()
