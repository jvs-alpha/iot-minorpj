import sqlite3

def read_user_db():
    database = sqlite3.connect("dat2.db")
    cursor = database.cursor()
    data = cursor.execute("SELECT * FROM user")
    out_data = list(data)
    database.close()
    return out_data

if __name__ == "__main__":
    list_data = read_user_db()
    for i in list_data:
        print(i)
