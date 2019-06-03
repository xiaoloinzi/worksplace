import re
from random import choice
from Common import ConfigHelper

def RandomErrCode(itemName):
    itemValue = ConfigHelper.GetValue(itemName)
    if itemValue == '' or itemValue == None:
        return None
    valueList = re.split('/',itemValue)
    return choice(valueList)