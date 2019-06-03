# encoding=utf-8
import requests
from flask import Flask,request,jsonify
import func_model

app = Flask(__name__)


@app.route("/rigester",methods=["GET","POST"])
def rigester():
    username = request.args.get("userName")
    userpwd = request.args.get("userPwd")

    result = func_model.rigester(username,userpwd)

    return jsonify(result)

@app.route("/login",methods=["GET","POST"])
def login():
    username = request.args.get("userName")
    userpwd = request.args.get("userPwd")

    result = func_model.login(username,userpwd)

    return jsonify(result)

@app.route("/login",methods=["GET","POST"])
def login():
    username = request.args.get("userName")
    userpwd = request.args.get("userPwd")

    result = func_model.login(username,userpwd)

    return jsonify(result)


if __name__=="__main__":
    app.run(host="127.0.0.1",port=80,debug=True)























