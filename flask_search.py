from flask import Flask,request,jsonify
from search_node_db import *
from read_user_db import *

app = Flask(__name__)

@app.route("/<pub_id>",methods=["GET"])
def search(pub_id):
    token = read_user_db()
    if request.headers["Cookie"] == token[-1][0]:
        data = search_node_db(pub_id)
        data = tuple(data)
        return jsonify(data),200
    else:
        return "no access",400

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port="3002")
