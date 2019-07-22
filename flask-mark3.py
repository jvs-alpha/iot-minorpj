#!/usr/bin/python3
from flask import Flask,request
from flask_restful import Resource,Api
from controls import *
import socket

app = Flask(__name__)
api = Api(app)

class work(Resource):
    def get(self):
        key = "qxZVfGaLXvOaWH7W6fISF457hBAZRynlT9MVEuAqvbN6f7ZJMgvx9i9Wb8iGeAkUK28OrL5wRFWaHy48gz4o4BCAqTHnFQN8tFph"
        # Key to check with
        check_key = request.args.get("key") # Gets the key from user
        if(check_key == key):   # If the key matches proceed
            val = request.args.get("val")   # Check if the val
            if(val == "True"):
                on()
                print("on")
                return "on",200
            elif(val == "False"):
                off()
                print("off")
                return "off",200
            else:
                return "query problem",422
        else:
            return "key not found",401

class basic(Resource):  # This class is just for fun
    def get(self):
        return "GGSafeHouse",200    # This will return the name GGSafeHouse

api.add_resource(basic,"/")
api.add_resource(work,"/work/")

if(__name__ == "__main__"):
    app.run("0.0.0.0","5000",debug=True)
