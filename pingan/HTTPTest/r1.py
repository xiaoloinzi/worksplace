# coding=utf-8

import requests

url_get = 'http://httpbin.org/ip'
r = requests.get(url_get)
print 'GET response:'
print r.text

url_post = 'http://httpbin.org/post'
postData = {'key1':'v1',
        'key2':'v2'}
r2 = requests.post(url_post,data=postData)
print 'POST response:'
print r2.text


url_put = 'http://httpbin.org/put'
putData = {'key1':'v1',
        'key2':'v2'}
r3 = requests.put(url_put,data=putData)
print 'PUT response:'
print r3.text

