# encoding=utf-8
from flask import Flask,request,jsonify,send_file,abort,make_response
import OperateExcel
import comm

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.errorhandler(404)
def testError404(msg):
    mr = make_response("")

    return jsonify(mr)

@app.route("/login",methods=["get"])
def login():
    username = request.args.get("userName")
    userpwd = request.args.get("userPwd")
    result = comm.login(username,userpwd)
    #自定义为字符串形式返回
    return str(result)


@app.route("/addContent",methods=["post"])
def addConcent():
    contentValue = request.args.get("contentToken")
    file = ''#request.files["file"]
    result = OperateExcel.addContent(contentValue,file)
    return str(result)

@app.route("/queryContent",methods=["get"])
def queryConcent():
    contentId = request.args.get("contentId")
    result = OperateExcel.queryContent(contentId)
    print result
    return jsonify(result)


@app.route("/deleteContent",methods=["delete"])
def deleteConcent():
    contentId = request.args.get("contentId")
    result = OperateExcel.deleteContent(contentId)
    return str(result)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8888,debug=True)










