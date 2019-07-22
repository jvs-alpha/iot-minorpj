from flask import Flask,request
from flask_restful import Api,Resource
import csv

app = Flask(__name__)
api = Api(app)

class base(Resource):
    def post(self):
        dat = request.get_json()
        dict_dat = dict(dat)
        print(dict_dat)
        return dict_dat,200

api.add_resource(base,"/")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="5000",debug=True)
