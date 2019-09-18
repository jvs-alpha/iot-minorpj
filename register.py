from flask_sqlalchemy import SQLAlchemy
from flask import Flask,request,jsonify
from read_db import *
import datetime
import uuid

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dat.db"
db = SQLAlchemy(app)

class node(db.Model):
    id = db.Column(db.Integer,primary_key=True,unique=True,nullable=False)
    pub_id = db.Column(db.String(40),unique=True,nullable=False)
    nodename = db.Column(db.String(20),unique=True,nullable=False)
    encode_jwt = db.Column(db.String(200),unique=True,nullable=False)
    admin = db.Column(db.Boolean,nullable=False)
    updated_time = db.Column(db.DateTime,nullable=True,default=datetime.datetime.utcnow())

    def __rep__(self):
        return "<User %r>" % self.username

@app.route("/user",methods=["GET"])
def get_all_data():
    inside_data = read_db()
    return jsonify({"data":inside_data})

@app.route("/user",methods=["POST"])
def create_user():
    data = request.get_json()
    inside_data = read_db()
    pre_id = inside_data[-1][0]
    id = pre_id + 1
    if data["admin"] == "True":
        admin = True
    else:
        admin = False
    new_user = node(id=id,pub_id=str(uuid.uuid4()),nodename=data["nodename"],encode_jwt=data["jwt"],admin=admin)
    db.session.add(new_user)
    db.session.commit()
    return "user created",200


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port="3000")

#curl -d '{"key1":"value1", "key2":"value2"}' -H "Content-Type: application/json" -X POST http://localhost:5000
