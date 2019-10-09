#!/usr/bin/python3
from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
#from controls import *
import socket
import datetime

app = Flask(__name__)
#db = SQLAlchemy(app)

#class node(db.Model):
#    id = db.Column(db.Integer,unique=True,nullable=False)
#    pub_id = db.Column(db.String(40),primary_key=True,unique=True,nullable=False)
#    nodename = db.Column(db.String(20),unique=True,nullable=False)
#    encode_jwt = db.Column(db.String(200),unique=True,nullable=False)
#    ip = db.Column(db.String(20),unique=True,nullable=False)
#    updated_time = db.Column(db.DateTime,nullable=True,default=datetime.datetime.utcnow())

@app.route("/",methods=["POST"])
def index():
    data = request.get_json()
    print(data)
    return "ggwp",200


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port="3003")
