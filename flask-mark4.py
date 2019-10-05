#!/usr/bin/python3
from flask import Flask,request
from flask_restful import Resource,Api
from read_node_db import *
from controls import *
import socket
import sqlite3

app = Flask(__name__)
api = Api(app)
