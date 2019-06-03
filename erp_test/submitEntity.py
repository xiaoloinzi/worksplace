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
sh=excel.sheet_by_name("submitentity入库")
rows=sh.nrows

for i in range(1,rows):
	text_content=sh.row_values(i)
	'''查询采购单id'''
	db_editingsystem="editingsystem"
	sql_batchid="select [Id] from [dbo].[EntityReceivingBatch] where [ReferencedNumber]='"+text_content[0]+"'"
	batchid=database_api.sql_conn(db_editingsystem,sql_batchid)

	'''查询库管员id'''
	db_usersystem="usersystem"
	sql_operatorid="select [Id] from [dbo].[User] where [Name]='"+text_content[1]+"'"
	operatorid=database_api.sql_conn(db_usersystem,sql_operatorid)

	'''提交库管'''
	url_submitEntity=""+login_api.erp_url+"Products/BatchSubmitEntityReceivingBatchToWareHouse"
	postdata_submitEntity={"batchIdList":[batchid],"operatorId":operatorid,"operatorName":text_content[1]}
	req_submitEntity=urllib2.Request(url=url_submitEntity,data=json.dumps(postdata_submitEntity),headers=header)
	print "提交库管返回信息:"+edit.open(req_submitEntity).read()

	'''入库'''
	'''获取推荐库位'''
	db_warehouse="warehousesystem"
	sql_requestid="select [Id] from [dbo].[InRequest] where [Code]='"+text_content[0]+"'"
	requestid=database_api.sql_conn(db_warehouse,sql_requestid)

	sql_areaid="select [Id] from [dbo].[Area] where [Code]='"+text_content[2]+"'"
	areaid=database_api.sql_conn(db_warehouse,sql_areaid)

	url_locatrd=""+login_api.erp_url+"InRequest/LocationRecommend"
	postdata_locatrd={"requestId":requestid,"areaId":areaid}
	req_locatrd=urllib2.Request(url_locatrd,data=json.dumps(postdata_locatrd),headers=header)
	print "推荐入库信息返回:"+edit.open(req_locatrd).read()

	'''检查SKU数量'''
	sql_amountid="select [Id] from [dbo].[InRequestDetail] where [RequestId]='"+requestid+"'"
	amountid=database_api.sql_multconn(db_warehouse,sql_amountid)
	#print amountid
	#print type(amountid[0][0])
	amountid_list=[]
	for j in range(0,len(amountid)):
		amountid_list.append(str(amountid[j][0]))
		url_checkamount=""+login_api.erp_url+"InRequest/RecordCheckAmount"
		postdata_checkamount={"id":str(amountid[j][0]),"requestId":requestid}
		req_checkamount=urllib2.Request(url_checkamount,data=json.dumps(postdata_checkamount),headers=header)
		print "检查数量信息返回:"+edit.open(req_checkamount).read()

	'''打印'''
	url_print=""+login_api.erp_url+"InRequest/GetInRequestForPrint"
	postdata_print={"id": requestid}
	req_print=urllib2.Request(url_print,data=json.dumps(postdata_print),headers=header)
	print "打印信息返回:"+edit.open(req_print).read()


	'''提交入库'''
	url_submit=""+login_api.erp_url+"InRequest/SubmitSkusInStock"
	postdata_submit={"id":requestid,"ids":amountid_list}
	req_submit=urllib2.Request(url_submit,data=json.dumps(postdata_submit),headers=header)
	print "提交入库信息返回:"+edit.open(req_submit).read()
