import hashlib

class SignHelper:
    @staticmethod
    def BuildDataSign(requestObj):
        attrDict = {}
        for key in requestObj.__dict__:
            attrDict[key] = requestObj.__dict__[key]
        content = ''
        for key in sorted(attrDict.keys()):
            if key == 'sign':
                continue
            if content != '':
                content += '&'
            content += key + '=' + str(attrDict[key])
        md5 = hashlib.md5()
        md5.update(content.encode('utf-8'))
        return md5.hexdigest().upper()