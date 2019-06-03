# encoding=utf-8
import requests

#将CookieJar转为字典：
cookies = requests.utils.dict_from_cookiejar(r.cookies)

#将字典转为CookieJar：
cookies = requests.utils.cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)
