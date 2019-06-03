# encoding=utf-8
import urllib
import urlparse
import re
import json
# 【python每日一练】判断一个url是不是满足restful风格，如果不满足给出提示，如果满足则对url进行解析，输出结果为json格式，例如
# {
# "httpType": "http",
# "ip": "127.0.0.1",
# "port": "80",
# "params": {
# "key1": "value1",
# "key2": "value2"
# }
# }

def urlMath(url):
    suna = '((http|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?'
    if re.match(suna,url):
        a = urlparse.urlparse(url)
        return json.dumps({
            "httpType":a.scheme,
            "ip":a.hostname,
            "port":a.port,
            "params": dict([(k,v[0]) for k,v in urlparse.parse_qs(a.query).items()])
        })
    return False


if __name__=="__main__":
    print urlMath("http://192.1.1.0:80/login?a=b&c=d")











