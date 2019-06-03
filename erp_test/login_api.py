#-*- coding:utf-8 -*-
import sys
import json
import requests
import urllib
import urllib2
import cookielib

reload(sys)
sys.setdefaultencoding( "utf-8" )

'''配置登录地址'''
erp_url="http://192.168.1.241:8881/"
pda_url="http://192.168.1.241:3000/"

'''ERP登录配置'''
def login_requests():
	session=requests.Session()
	login_url=""+erp_url+"Account/Login"
	login_data={"userName":"admin","password":"123456","rememberMe":False}
	session.post(login_url,data=login_data)
	return session

def login_urllib():
	cj=cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	login_url = ""+erp_url+"Account/Login"	#登陆地址
	login_data = urllib.urlencode({"userName":"admin","password":"123456","rememberMe":False}).encode('utf-8')
	opener.open(login_url,login_data)
	return opener

'''pda登录配置'''
def login_pda():
	session=requests.Session()
	login_url=""+pda_url+"login"
	login_data={"userNameOrEmail":"mjy","password":"idh#01"}
	session.post(login_url,data=login_data)
	return session

def login_pda_urllib():
	cj=cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	login_url = ""+pda_url+"login"	#登陆地址
	login_data = urllib.urlencode({"userNameOrEmail":"mjy","password":"idh#01"})
	opener.open(login_url,login_data)
	return opener