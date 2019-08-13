from flask import Flask,request,jsonify,make_response
from flask_restful import Api,Resource
import jwt
import datetime

app = Flask(__name__)
api = Api(app)

class auth(Resource):
    def get(self):
        if request.authorization and request.authorization.username == "jvs" and request.authorization.password == "ggsafehouse":
            encoded = jwt.encode({"user":request.authorization.username,"exp":datetime.datetime.utcnow()+datetime.timedelta(minutes=30)},"thisisshit",algorithm="HS256")
            return encoded.decode("UTF-8"),200
        else:
            return make_response("you are dead",200)

api.add_resource(auth,"/login")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="3000",debug=True)

# curl -u jvs:ggsafehouse http://127.0.0.1:3000/login
