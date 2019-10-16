import sqlite3

def node_control(ip,):
    database = sqlite3.connect("dat.db")
    db = database.cursor()
    data = db.execute("SELECT * FROM node")
    data = list(data)
    for i in data:
        print(i)
        print()


if __name__ == "__main__":
    node_control()
