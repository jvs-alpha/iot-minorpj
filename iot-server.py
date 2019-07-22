from flask import Flask,request
from flask_restful import Api,Resource
import sqlite3
import datetime

app = Flask(__name__)
api = Api(app)

class store(Resource):
    def post(self):
        dat = request.get_json()
        dict_dat = dict(dat)
        id = dict_dat["id"]
        name = dict_dat["name"]
        date = datetime.date.today().strftime("%Y-%m-%d")
        database = sqlite3.connect("data.db")
        cursor = database.cursor()
        command = '''
        INSERT INTO DATA (`ID`,`NAME`,`UPLOAD_DATE`) VALUES ({},"{}","{}")
        '''.format(id,name,date)
        cursor.execute(command)
        database.commit()
        database.close()
        return dict_dat,200

api.add_resource(store,"/")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="5000",debug=True)
