import sqlite3

database = sqlite3.connect("dat.db")
cursor = database.cursor()
data = cursor.execute("SELECT * FROM node")
print(list(data))
database.close()
