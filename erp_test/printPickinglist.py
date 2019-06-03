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
login=login_api.login_requests()

'''读取excel表格'''
excel=xlrd.open_workbook('./data_config.xls')
sh=excel.sheet_by_name("printPickinglist生成批次")
rows=sh.nrows

for i in range(1,rows):
	text_content=sh.row_values(i)

	db_shippingsystem="shippingsystem"
	db_warehouse="warehousesystem"
	db_user="usersystem"

	'''判断订单类型'''
	if text_content[0]=="单发":
		printType="0"

		'''运输类型ID'''
		if text_content[1]=="全部":
			sql_shippingIDs="select [Id] from [dbo].[ShippingMethod] where [WarehouseId]='01602662-74ce-4ab8-aabb-3f6c5e5c9f34' and [Enabled]=1 and ([ShippingType]=1 or [ShippingType]=0)"
			shippingIDs=database_api.sql_multconn(db_shippingsystem,sql_shippingIDs)

		else:
			shippingIDs=[]
			shippingType_list=text_content[1].split(',')
			for shippingType in shippingType_list:
				sql_shippingID="select [Id] from  [dbo].[ShippingMethod] where [WarehouseId]='01602662-74ce-4ab8-aabb-3f6c5e5c9f34' and [Enabled]=1 and ([ShippingType]=1 or [ShippingType]=0) and [Name]='"+shippingType+"'"
				shippingID=database_api.sql_conn(db_shippingsystem,sql_shippingID)
				shippingIDs.append(shippingID)
			#print shippingIDs

		'''拣单数量'''
		orderAmount=int(text_content[2])

		'''拣货区ID'''
		locations_list=text_content[3].split(',')
		locationIDs=[]
		for location in locations_list:
			sql_locationID="select [Id] from [dbo].[Area] where [Name]='"+location+"'"
			locationID=database_api.sql_conn(db_warehouse,sql_locationID)
			locationIDs.append(locationID)
		# print locationIDs

		'''拣货区格数ID'''
		rowIDs=[]
		for AreaId in locationIDs:
			sql_rowID="select [Id] from [dbo].[Row] where [AreaId]='"+AreaId+"'"
			rowID=database_api.sql_multconn(db_warehouse,sql_rowID)
			for i in rowID:
				rowIDs.append(i)
		# print rowIDs
		# print len(rowIDs)

		'''拣货员ID'''
		sql_pickerID="select [Id] from [dbo].[User] where [Name]='"+text_content[4]+"'"
		pickerID=database_api.sql_conn(db_user,sql_pickerID)
		# print pickerID

		'''请求单发批次'''
		url_single=""+login_api.erp_url+"ShippingOrder/PrintPickingList"
		postdata_single={"type":"printpicking","printType":printType,"orderAmount":orderAmount,"locations":locationIDs,"shippingMethods":shippingIDs,"picker":pickerID,"rows":rowIDs}
		req_single=login.post(url_single,data=postdata_single)
		print "生成单发批次返回信息:"+req_single.text
		
	elif text_content[0]=="配发":
		printType="1"

		'''运输类型ID'''
		if text_content[1]=="全部":
			sql_shippingIDs="select [Id] from [dbo].[ShippingMethod] where [WarehouseId]='01602662-74ce-4ab8-aabb-3f6c5e5c9f34' and [Enabled]=1 and ([ShippingType]=1 or [ShippingType]=0)"
			shippingIDs=database_api.sql_multconn(db_shippingsystem,sql_shippingIDs)

		else:
			shippingIDs=[]
			shippingType_list=text_content[1].split(',')
			for shippingType in shippingType_list:
				sql_shippingID="select [Id] from  [dbo].[ShippingMethod] where [WarehouseId]='01602662-74ce-4ab8-aabb-3f6c5e5c9f34' and [Enabled]=1 and ([ShippingType]=1 or [ShippingType]=0) and [Name]='"+shippingType+"'"
				shippingID=database_api.sql_conn(db_shippingsystem,sql_shippingID)
				shippingIDs.append(shippingID)
			#print shippingIDs

		'''拣单数量'''
		orderAmount=int(text_content[2])

		'''请求配发批次'''
		url_mult=""+login_api.erp_url+"ShippingOrder/PrintPickingList"
		postdata_mult={"type":"printpicking","printType":printType,"orderAmount":orderAmount,"locations":[],"shippingMethods":shippingIDs,"picker":"0","rows":[]}
		req_mult=login.post(url_mult,data=postdata_mult)
		print "生成配发批次返回信息:"+req_mult.text

	elif text_content[0]=="快递":
		printType="2"
		'''运输类型ID'''
		if text_content[1]=="全部":
			sql_shippingIDs="select [Id] from [dbo].[ShippingMethod] where [WarehouseId]='01602662-74ce-4ab8-aabb-3f6c5e5c9f34' and [Enabled]=1 and [ShippingType]=2"
			shippingIDs=database_api.sql_multconn(db_shippingsystem,sql_shippingIDs)

		else:
			shippingIDs=[]
			shippingType_list=text_content[1].split(',')
			for shippingType in shippingType_list:
				sql_shippingID="select [Id] from  [dbo].[ShippingMethod] where [WarehouseId]='01602662-74ce-4ab8-aabb-3f6c5e5c9f34' and [Enabled]=1 and [ShippingType]=2 and [Name]='"+shippingType+"'"
				shippingID=database_api.sql_conn(db_shippingsystem,sql_shippingID)
				shippingIDs.append(shippingID)
			#print shippingIDs

		'''拣单数量'''
		orderAmount=int(text_content[2])

		'''拣货员ID'''
		sql_pickerID="select [Id] from [dbo].[User] where [Name]='"+text_content[4]+"'"
		pickerID=database_api.sql_conn(db_user,sql_pickerID)
		# print pickerID

		'''请求快递批次'''
		url_express=""+login_api.erp_url+"ShippingOrder/PrintPickingList"
		postdata_express={"type":"printpicking","printType":printType,"orderAmount":orderAmount,"locations":[],"shippingMethods":shippingIDs,"picker":pickerID,"rows":[]}
		req_express=login.post(url_express,data=postdata_express)
		print "生成快递批次返回信息:"+req_express.text

	elif text_content[0]=="多规格非快递":
		printType="3"
		'''运输类型ID'''
		if text_content[1]=="全部":
			sql_shippingIDs="select [Id] from [dbo].[ShippingMethod] where [WarehouseId]='01602662-74ce-4ab8-aabb-3f6c5e5c9f34' and [Enabled]=1 and ([ShippingType]=1 or [ShippingType]=0)"
			shippingIDs=database_api.sql_multconn(db_shippingsystem,sql_shippingIDs)

		else:
			shippingIDs=[]
			shippingType_list=text_content[1].split(',')
			for shippingType in shippingType_list:
				sql_shippingID="select [Id] from  [dbo].[ShippingMethod] where [WarehouseId]='01602662-74ce-4ab8-aabb-3f6c5e5c9f34' and [Enabled]=1 and ([ShippingType]=1 or [ShippingType]=0) and [Name]='"+shippingType+"'"
				shippingID=database_api.sql_conn(db_shippingsystem,sql_shippingID)
				shippingIDs.append(shippingID)
			#print shippingIDs

		'''拣单数量'''
		orderAmount=int(text_content[2])

		'''拣货员ID'''
		sql_pickerID="select [Id] from [dbo].[User] where [Name]='"+text_content[4]+"'"
		pickerID=database_api.sql_conn(db_user,sql_pickerID)
		# print pickerID

		'''请求多规格非快递批次'''
		url_multnoexpress=""+login_api.erp_url+"ShippingOrder/PrintPickingList"
		postdata_multnoexpress={"type":"printpicking","printType":printType,"orderAmount":orderAmount,"locations":[],"shippingMethods":shippingIDs,"picker":pickerID,"rows":[]}
		req_multnoexpress=login.post(url_multnoexpress,data=postdata_multnoexpress)
		print "生成多规格非快递返回信息:"+req_multnoexpress.text

	elif text_content[0]=="多规格快递":
		printType="4"
		'''运输类型ID'''
		if text_content[1]=="全部":
			sql_shippingIDs="select [Id] from [dbo].[ShippingMethod] where [WarehouseId]='01602662-74ce-4ab8-aabb-3f6c5e5c9f34' and [Enabled]=1 and [ShippingType]=2"
			shippingIDs=database_api.sql_multconn(db_shippingsystem,sql_shippingIDs)
			# print shippingIDs
		else:
			shippingIDs=[]
			shippingType_list=text_content[1].split(',')
			for shippingType in shippingType_list:
				sql_shippingID="select [Id] from  [dbo].[ShippingMethod] where [WarehouseId]='01602662-74ce-4ab8-aabb-3f6c5e5c9f34' and [Enabled]=1 and [ShippingType]=2 and [Name]='"+shippingType+"'"
				shippingID=database_api.sql_conn(db_shippingsystem,sql_shippingID)
				shippingIDs.append(shippingID)
			#print shippingIDs

		'''拣单数量'''
		orderAmount=int(text_content[2])

		'''拣货员ID'''
		sql_pickerID="select [Id] from [dbo].[User] where [Name]='"+text_content[4]+"'"
		pickerID=database_api.sql_conn(db_user,sql_pickerID)
		# print pickerID

		'''请求多规格快递批次'''
		url_multexpress=""+login_api.erp_url+"ShippingOrder/PrintPickingList"
		postdata_multexpress={"type":"printpicking","printType":printType,"orderAmount":orderAmount,"locations":[],"shippingMethods":shippingIDs,"picker":pickerID,"rows":[]}
		req_multexpress=login.post(url_multexpress,data=postdata_multexpress)
		print "生成多规格快递返回信息:"+req_multexpress.text

	
	

