'''
we need to have two sections in the iot node one to get the authentication jwt from the dat2.db
and the second one is for using it to control the switch
'''

#!/usr/bin/python3
from flask import Flask,request
import requests
import sys
#from controls import *
import socket
import sqlite3

def read_jwt(id,ip):
    data = requests.get(
    "http://127.0.0.1:3003",
    headers={"id":str(id)},
    )
    print(data.json())

if __name__ == "__main__":
    read_jwt(1,"127.0.0.1")
