# encoding=utf-8
from flask import Flask,request,jsonify,send_file,abort,make_response
import OperateExcel

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.errorhandler(404)
def testError404(msg):
    mr = make_response("")

    return jsonify(mr)


@app.route("/addContent",methods=["post"])
def addConcent():
    contentValue = request.args.get("contentValue")
    file = request.files["file"]
    result = OperateExcel.addContent(contentValue,file)
    return jsonify(result)

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
    return jsonify(result)

if __name__=="__main__":
    app.run(host="127.0.0.1",port=80,debug=True)










