from flask import Flask,request
from flask_restful import Api,Resource
from controls import *
 app = Flask(__name__)
 api = Api(app)
