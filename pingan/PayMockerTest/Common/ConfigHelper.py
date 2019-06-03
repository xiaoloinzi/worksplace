import json

ConfigFile = None
ConfigJson = None

def LoadConfigFile(configFile):
    global ConfigFile
    ConfigFile = configFile.replace('\n','')
    file = open(ConfigFile,'r')
    global ConfigJson
    ConfigJson = json.load(file)
    file.close()

def ReLoadConfig():
    LoadConfigFile(ConfigFile)

def GetPayResult():
    ReLoadConfig()
    return ConfigJson['PayResult']

def GetNotifyDelay():
    ReLoadConfig()
    return int(ConfigJson['NotifyDelay'])

def GetValue(itemName):
    ReLoadConfig()
    if itemName not in ConfigJson:
        return None
    return ConfigJson[itemName]