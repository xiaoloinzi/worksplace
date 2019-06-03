#-*- coding:utf-8 -*-
import sys
import json
import requests
import xlrd
import database_api
import login_api

reload(sys)
sys.setdefaultencoding( "utf-8" )

'''设置登陆session'''
new=login_api.login_requests()

'''读取excel表格'''
excel=xlrd.open_workbook('./data_config.xls')
sh=excel.sheet_by_name("newproduct新品开发")
rows=sh.nrows


for i in range(1,rows):
	text_content=sh.row_values(i)
	'''搜索中国仓ID'''
	db_warehouse='systemmanagementsystem'
	sql_warehouse="select [Id] from [dbo].[Warehouse] where [Name]='中国仓库'"
	id_warehouse=database_api.sql_conn(db_warehouse,sql_warehouse)
	#print id_warehouse
	'''搜索产品id'''
	db_newproduct='productsystem'
	sql_newproduct="select [Id] from [dbo].[NewProduct] where [WarehouseId]='"+id_warehouse+"' and [Title]='"+text_content[0]+"' order by [LastModified] desc "
	id_newproduct=database_api.sql_conn(db_newproduct,sql_newproduct)
	#print id_newproduct
	'''发送提审请求'''
	check_url=""+login_api.erp_url+"Purchase/BatchSubmitAuditor"
	postdata_check=json.loads('{"idList":["'+id_newproduct+'"]}')
	req_check=new.post(check_url,data=postdata_check)
	print "提审返回信息:"+req_check.text

	'''通过审核'''
	pass_url=""+login_api.erp_url+"Purchase/BatchPass"
	postdata_pass=json.loads('{"idList":["'+id_newproduct+'"],"unSaleSites":[]}')
	req_pass=new.post(pass_url,data=postdata_pass)
	print "通过返回信息:"+req_pass.text