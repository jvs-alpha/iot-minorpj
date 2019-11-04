from flask import Flask,request

app = Flask(__name__)

@app.route("/",methods=["POST"])
def get_environ():
    data = request.get_json()
    print(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port="3004",debug=True)
