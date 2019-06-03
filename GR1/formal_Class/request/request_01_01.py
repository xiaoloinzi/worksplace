# encoding=utf-8

from flask import Flask,request,jsonify
import random
from logic import model_01


app = Flask(__name__)


@app.route("/zc",methods=["POST"])
def test():
    telnumber = request.args.get("telnumber")
    userpwd = request.args.get("pwd")
    result = model_01.register(telnumber,userpwd)
    return jsonify(result)

@app.route("/login",methods=["POST"])
def login():
    usertel = request.args.get("usertel")
    userpwd = request.args.get("userpwd")
    result = model_01.login(usertel,userpwd)
    return jsonify(result)


if __name__=="__main__":
    app.run(host='127.0.0.1',port=80,debug=True)
















