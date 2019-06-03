#-*- coding:utf-8 -*-
import time
import sys
import urllib
import urllib2
import cookielib
import json
import requests
import xlrd
import pymssql
import database
import threading
import login_api
import database_api

reload(sys)
sys.setdefaultencoding( "utf-8" )

class postRequest():  
    def __init__(self,url,values,interface_name):  
        self.url = url  
        self.values = values  
        #self.interface_name = interface_name  
          
    def post(self):  
        parms=self.values  
        #querystring = parse.urlencode(parms)  
        try:
            new=login_api.login_requests()
            u = new.post(self.url,data=parms)  
            resp = u.text  
            #print(u"接口名字为：",self.interface_name)  
            #print (u"所传递的参数为：\n",parms)  
            print "服务器返回:"+resp
        except URLError as e:  
            print (e)  
  
def Login(qcorderid):                        #定义接口函数  
	'''读取表头信息'''
	# list_info=[]
	# for row in range(0,cols):
	# 	list_info.append(sh.cell_value(0,row))
	# #print list_info

	# info=[]	
	# num=0		

	# info.append(sh.row_values(i))
	# text_content=sh.row_values(i)
	'''数据库连接查询分类ID'''
	warehousesystem_db='warehousesystem'
	qcid_sql="select [Id] from [dbo].[InRequest] where [RelatedCode]='"+qcorderid+"'"
	qcid=database_api.sql_conn(warehousesystem_db,qcid_sql)

	'''数据库连接查询站点ID'''
	# site_db='systemmanagementsystem'
	purchase_sql="select [PurchaseId] from [dbo].[InRequest] where [RelatedCode]='"+qcorderid+"'"
	purchaseid=database_api.sql_conn(warehousesystem_db,purchase_sql)

	#实例化接口对象
	login=postRequest(""+login_api.erp_url+"InRequest/ReturnToRequest",{"id":qcid,"purchaseId":purchaseid,"remark":"bbb"},"test")
	return login.post()  

try:  
	i = 0  
	tasks = []                                      #任务列表  
	task_number = 10  
	excel=xlrd.open_workbook('./data_config.xls')
	sh=excel.sheet_by_name("qcreturn质检退回")
	rows=sh.nrows
	text_content=sh.row_values(1)
	a=text_content[0].split(',')
	# print a[0]
	while i < task_number:  
		t = threading.Thread(target=Login(a[i]))    
		tasks.append(t)                        #加入线程池，按需使用  
		t.start()
		i=i+1
	# 	time.sleep(1)
	# t.join()                   
except Exception as e:  
	print (e) 






