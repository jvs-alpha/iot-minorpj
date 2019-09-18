import sqlite3

def read_db():
    database = sqlite3.connect("dat.db")
    cursor = database.cursor()
    data = cursor.execute("SELECT * FROM node")
    database.close()
    return data
