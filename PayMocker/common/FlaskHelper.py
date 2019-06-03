#encoding=utf-8
from flask import Flask

class FlaskHelper(object):
   INSTANCE = None
   app = None
   #使用单例模式返回flask对象
   def __new__(cls, *args, **kwargs):
      if not cls.INSTANCE:
         cls.INSTANCE = super(FlaskHelper, cls).__new__(cls, *args, **kwargs)
         cls.INSTANCE.app = Flask('PayMocker')
      return cls.INSTANCE



