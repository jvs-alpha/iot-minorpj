import sqlite3
import sys

def search_node_db(pub_id):
    print(pub_id)
    database = sqlite3.connect("dat.db")
    cursor = database.cursor()
    data = cursor.execute("SELECT * FROM node WHERE pub_id = %s" % pub_id)
    data = list(data)
    database.close()
    return out_data


if __name__ == "__main__":
    print(search_node_db(sys.argv[1]))
