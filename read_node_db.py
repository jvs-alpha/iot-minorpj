import sqlite3

def read_node_db():
    database = sqlite3.connect("dat.db")
    cursor = database.cursor()
    data = cursor.execute("SELECT * FROM node")
    out_data = list(data)
    database.close()
    return out_data

if __name__ == "__main__":
    list_data = read_node_db()
    for i in list_data:
        print(i)
