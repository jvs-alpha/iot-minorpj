from flask_sqlalchemy import SQLAlchemy
from flask import Flask,request
import datetime
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dat.db"
db = SQLAlchemy(app)

class node(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    pub_id = db.Column(db.String(40),unique=True,nullable=False)
    nodename = db.Column(db.String(20),unique=True,nullable=False)
    encode_jwt = db.Column(db.String(200),unique=True,nullable=False)
    updated_time = db.Column(db.DateTime,nullable=True,default=datetime.datetime.utcnow())

# for creating the databse import db from this file in python3 and run
# db.create_all() for creating the database
# then we need to import the node class to put the data in the as varialbe
# then add and commit the data to the database
