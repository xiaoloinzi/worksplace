from flask import Flask

class FlaskHelper(object):
   INSTANCE = None
   app = None

   def __new__(cls, *args, **kwargs):
      if not cls.INSTANCE:
         cls.INSTANCE = super(FlaskHelper, cls).__new__(cls, *args, **kwargs)
         cls.INSTANCE.app = Flask('PayMocker')
      return cls.INSTANCE



