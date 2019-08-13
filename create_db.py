from flask_sqlalchemy import SQLAlchemy
from flask import Flask,request
import datetime
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dat.db"
db = SQLAlchemy(app)

class node(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nodename = db.Column(db.String(20),unique=True,nullable=False)
    encode_jwt = db.Column(db.String(200),unique=True,nullable=False)
    updated_time = db.Coumn(db.DateTime,nullable=True,default=datetime.datetime.utcnow())
