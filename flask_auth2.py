from flask import Flask,request,jsonify,make_response
from flask_sqlalchemy import SQLAlchemy
import jwt
import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dat2.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class user(db.Model):
    encode_jwt = db.Column(db.String(200),primary_key=True,unique=True,nullable=False)

    def __rep__(self):
        return "<User %r>" % self.username

@app.route("/login",methods=["GET"])
def login():
    if request.authorization and request.authorization.username == "jvs" and request.authorization.password == "ggsafehouse":
        encoded = jwt.encode({"user":request.authorization.username,"exp":datetime.datetime.utcnow()+datetime.timedelta(minutes=30)},"thisisshit",algorithm="HS256")
        token = encoded.decode("UTF-8")
        dat = user(encode_jwt=token)
        db.session.add(dat)
        db.session.commit()
        return token,200
    else:
        return make_response("you are dead",200)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="3001",debug=True)

# curl -u jvs:ggsafehouse http://127.0.0.1:3001/login
