#encoding=utf-8

#校验非空
def validate(contentDict,keys):
    keyList = []
    for key in keys:
        if contentDict[key] == None:
            keyList.append(key)
    if len(keyList) > 0:
        raise Exception("missing an argument:"+str(keyList))