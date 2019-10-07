'''
we need to have two sections in the iot node one to get the authentication jwt from the dat2.db
and the second one is for using it to control the switch
'''

#!/usr/bin/python3
from flask import Flask,request
from read_node_db import *
from controls import *
import socket
import sqlite3
