from flask import Flask,request
import sqlite3


def search_by_id(id):
    database = sqlite3.connect("dat.db")
    cursor = database.cursor()
    data = cursor.execute("SELECT * FROM node WHERE id = {}".format(id))
    data = list(data)
    database.close()
    return data

app = Flask(__name__)

@app.route("/",methods=["GET"])
def index():
    dat = request.headers["id"]
    data = search_by_id(int(dat))
    return {"data":data[0]},200

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port="3003")
