import sqlite3
from urllib import request
import json
import sys


def node_control(ip,values):
    database = sqlite3.connect("dat.db")
    db = database.cursor()
    data = db.execute("SELECT * FROM node")
    data = list(data)
    for i in data:
        if ip in i:
            break
    key = i[-3]
    port = ":5000"
    http = "http://"
    dir = "/work/"
    keys = "key={}".format(key)
    print(keys)
    val = "val="
    use = http+ip+port+dir+"?"+keys+"&"+val+values
    dat = request.urlopen(use)
    print(json.load(dat))


if __name__ == "__main__":
    node_control(sys.argv[1],sys.argv[2])
