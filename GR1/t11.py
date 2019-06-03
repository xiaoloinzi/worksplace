# encoding=utf-8
import requests,json

# encoding=utf-8
import requests,json

urlGet = 'http://httpbin.org/get'
paramsGet = {'key1':'v1','key2':'v2'}
r = requests.get(urlGet,paramsGet)
print r.text
print r.status_code
print '*******'

urlPost = 'http://httpbin.org/post'
paramsPost = {'key1':'v1','key2':'v2'}
dataPost = {'keyP1':'v1','keyP2':'v2'}
r2 = requests.post(urlPost,data=dataPost,params=paramsPost)
print r2.text
print r2.status_code
print '*******'


urlGet = 'http://httpbin.org/delete'
paramsdelete = {'key1':'v1','key2':'v2'}
r = requests.delete(urlGet,params=paramsdelete)
print r.text
print r.status_code
print '*******'

urlput = 'http://httpbin.org/put'
paramsput = {'key1':'v1','key2':'v2'}
dataput = {'keyP1':'v1','keyP2':'v2'}
r2 = requests.put(urlput,data=dataput,params=paramsput)
print r2.text
print r2.status_code
print '*******'