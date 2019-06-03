# encoding=utf-8
def isdigit(strVar):
    for i in strVar:
        if i < '0' or i > '9':
            return False
    return True

def strip(s):
    if len(s) == 0:
        return ''
    stringList = list(s)
    sapceLetter = [' ','\t','\n','\f','\v','\r']
    for i in range(len(stringList)):
        if stringList[i] in sapceLetter:
            stringList[i] = ''
        else:
            break
    for i in range(1,len(stringList)+1):
        if stringList[-i] in sapceLetter:
            stringList[-i] = ''
        else:
            break
    return ''.join(stringList)

def join(strList,joinLetter=''):
    joinedStr = ''
    for i in strList:
        if joinedStr == '':
            joinedStr = str(i)
        else:
            joinedStr += joinLetter + str(i)
    return joinedStr

def split(strVar,splotStr = None):
    if splotStr is None:
        pSeq = [' ','\t','\n','\f','\v','\r']
        stringList = list(strVar)
        for i in range(len(stringList)):
            if stringList[i] in pSeq:
                stringList[i] = ''
                if i+1 < len(stringList) and stringList[i+1] in pSeq:
                    stringList[i] = ''
        strVar = ''.join(stringList)
        splotStr = ' '
    tmp = ''
    length = len(splotStr)
    result = []
    i = 0
    while i <= len(strVar)-1:
        if strVar[i:i+length] == splotStr:
            result.append(tmp)
            tmp = ''
            i += length
        else:
            tmp += strVar[i]
            i += 1
    result.append(tmp)










