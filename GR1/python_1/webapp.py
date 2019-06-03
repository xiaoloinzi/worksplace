# encoding=utf-8
from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
import qrc
app = Flask(__name__)

@app.route('/')#‘/'页面或路径
def index():
    return redirect(url_for('url'))

@app.route('/url',methods=['GET','POST'])
def url():#默认请求方式为get
    #request中包含所有用户发起请求的信息
    if request.method == 'GET':
        return render_template('url.html')
    else:
        url = request.form['url']
        imgurl = qrc.url(url)
        return render_template('img.html',imgurl=imgurl)

@app.route('/text',methods=['GET','POST'])
def text():
    if request.method == 'GET':
        return render_template('url.html')
    else:
        url = request.form['url']
        imgurl = qrc.url(url)
        return render_template('img.html',imgurl=imgurl)
if __name__=='__main__':
    app.debug = True
    app.run()#app.run(debug=True)