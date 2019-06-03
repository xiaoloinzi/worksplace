#encoding=utf-8
import hashlib

#签名算法
class SignHelper:
    @staticmethod
    def BuildDataSign(requestObj):
        attrDict = {}
        for key in requestObj:
            attrDict[key] = requestObj[key]
        content = ''
        for key in sorted(attrDict.keys()):
            if key == 'sign':
                continue
            if content != '':
                content += '&'
            content += key + '=' + str(attrDict[key])
        md5 = hashlib.md5()
        md5.update(content.encode('utf-8'))
        return str(md5.hexdigest().upper())