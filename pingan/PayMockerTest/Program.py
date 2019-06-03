#!/usr/bin/env python
import os
import sys
import threading
from Common import PathHelper,ConfigHelper
# import Weixin.views
import Alipay.views
from Common.FlaskHelper import *

if __name__ == "__main__":

    ConfigHelper.LoadConfigFile(PathHelper.ConfigFile)

    # task = threading.Thread(target=Weixin.views.StartNotifyTask)
    # task.setDaemon(True)
    # task.start()
    task = threading.Thread(target=Alipay.views.StartNotifyTask)
    task.setDaemon(True)
    task.start()

    FlaskHelper().app.run(host='0.0.0.0', port=8001,debug=True)
