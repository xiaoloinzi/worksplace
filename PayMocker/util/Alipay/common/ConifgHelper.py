#encoding=utf-8
import json,os
global aliPayConfigInfo
def initConfig(configFile):
    with open(configFile, "r") as f:
        global aliPayConfigInfo
        aliPayConfigInfo = json.load(f)
