#-*- coding:utf-8 -*-
import sys
import json
import xlrd
import database_api
import login_api
import urllib2

reload(sys)
sys.setdefaultencoding( "utf-8" )

header = {'Host':login_api.erp_url,'Connection':' keep-alive','Accept': 'application/json, text/javascript, */*; q=0.01','Origin':'http://192.168.1.220:8881','X-Requested-With': 'XMLHttpRequest','User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36','Content-Type': 'application/json','Accept-Encoding': 'gzip, deflate','Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6'}

'''设置登陆'''
edit=login_api.login_urllib()

'''读取excel表格'''
excel=xlrd.open_workbook('./data_config.xls')
sh=excel.sheet_by_name("signpurchase")
rows=sh.nrows

for i in range(1,rows):
	text_conten=sh.row_values(i)
	db_editingsystem="editingsystem"
	sql_batchid="select [Id] from [dbo].[EntityReceivingBatch] where [ReferencedNumber]='"+text_conten[0]+"'"
	batchid=database_api.sql_conn(db_editingsystem,sql_batchid)
	url_sign=""+login_api.erp_url+"Products/SignInEntityReceivingBatch"
	postdata_sign={"batchIdList":[batchid],"isSign":"true"}
	req_sign=urllib2.Request(url=url_sign,data=json.dumps(postdata_sign),headers=header)
	print "签收采购单返回信息:"+edit.open(req_sign).read()