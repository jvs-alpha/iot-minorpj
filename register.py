from create_db import db,node
from read_db import *
from flask import Flask,request,jsonify
import uuid

app = Flask(__name__)

inside_data = []

@app.route("/user",methods=["GET"])
def get_all_data():
    inside_data = read_db()
    print(inside_data)
    return "good"

#@app.route("/user",methods=["POST"])
#def create_user():
#    inside_data = read_db()
#    return jsonify(inside_data),200


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port="3000")
