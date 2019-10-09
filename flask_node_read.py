import requests
import sqlite3


def search_by_id(id):
    database = sqlite3.connect("dat.db")
    cursor = database.cursor()
    data = cursor.execute("SELECT * FROM node WHERE id = {}".format(id))
    data = list(data)
    database.close()
    return data

def send_data(data):
    data = data[0]
    id = data[0]
    pub_id = data[1]
    nodename = data[2]
    encode_jwt = data[3]
    ip = data[4]
    updated_time = data[5]
    requests.post(
    f"http://127.0.0.1:3003/", # chage the 127.0.0.1 to {ip}
    data={"id":int(id),"pub_id":pub_id,"nodename":nodename,"encode_jwt":encode_jwt,"ip":ip,"updated_time":updated_time}
    )

if __name__ == "__main__":
    data = search_by_id(1)
    send_data(data)
