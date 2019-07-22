from flask import Flask,request
from flask_restful import Api,Resource
import pandas as pd

app = Flask(__name__)
api = Api(app)

class store(Resource):
    def post(self):
        dat = request.get_json()
        dict_dat = dict(dat)
        dataframe = pd.DataFrame(dict_dat)
        dataframe.to_csv("data.csv")
        return dict_dat,200

api.add_resource(store,"/")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="5000",debug=True)
