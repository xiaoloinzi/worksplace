# encoding=utf-8
from flask import Flask,request,jsonify,make_response,abort,send_file
import OperateExcel,os

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

imageRootPath = os.getcwd()+"\\upload"

#下载
@app.route("/downLoad",methods=["get"])
def downLoad():
    fileName = request.args.get("fileName")
    filePath = imageRootPath+"\\"+str(fileName)
    if os.path.exists(filePath):
        mr = make_response(send_file(filePath))
    else:
        abort(404)
    return mr


@app.route("/addContent",methods=["post"])
def addContent():
    contentValue = request.args.get("contentValue")
    file = request.files["file"]
    result = OperateExcel.addContent(contentValue,file)
    return jsonify(result)

@app.route("/queryContent",methods=["get"])
def queryContent():
    contentId= request.args.get("contentId")
    result = OperateExcel.queryContent(contentId)
    return jsonify(result)
#删除不存在的一样提示
@app.errorhandler(404)
def testError404(msg):
    mr = make_response(jsonify({"message":"resource not found","status":0}))
    mr.status_code = 404
    return mr

@app.route("/deleteContent",methods=["delete"])
def deleteContent():
    contentId= request.args.get("contentId")
    result = OperateExcel.deleteContent(contentId)
    if result == 0:
        abort(404)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host="127.0.0.1",port=8888,debug=True)
