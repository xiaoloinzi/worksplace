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
sh=excel.sheet_by_name("delivery发货")
rows=sh.nrows

for i in range(1,rows):
	text_content=sh.row_values(i)
	db_warehouse="warehousesystem"

	'''根据发货单发货'''
	if text_content[1]:
		delivery_num=text_content[1].split(',')
		for k in delivery_num:

			'''查询发货单ID'''
			sql_orderId="select [Id] from [dbo].[ShippingOrder] where [Code]='"+k+"'"
			orderId=database_api.sql_conn(db_warehouse,sql_orderId)

			'''查询重量'''
			sql_weight="select [Weight] from [dbo].[ShippingOrder] where [Code]='"+k+"'"
			weight=database_api.sql_conn(db_warehouse,sql_weight)

			'''打印发货'''
			url_print=""+login_api.erp_url+"ShippingOrder/GetOrderForPrint"
			postdata_print={"orderIds":[orderId]}
			req_print=login.post(url_print,data=postdata_print)
			print "打印发货返回信息:"+req_print.text

			'''发货'''
			url_delivery=""+login_api.erp_url+"ShippingOrder/ShippingOrderDelivery"
			postdata_delivery={"orderIds":[orderId],"weight":weight}
			req_delivery=login.post(url_delivery,data=postdata_delivery)
			print "发货返回信息:"+req_delivery.text
			print "\n"

	else:
		sql_picklist="select [Id] from [dbo].[PickingList] where [Code]='"+text_content[0]+"'"
		picklist=database_api.sql_conn(db_warehouse,sql_picklist)

		sql_orderIds="select [OrderId] from [dbo].[PickingListDetail] where [ListId]='"+picklist+"'"
		orderIds=database_api.sql_multconn(db_warehouse,sql_orderIds)
		
		'''遍历全部未发货的发货单id'''
		for j in orderIds:
			allorderIds=str(j[0])
			sql_orderId="select [Id] from [dbo].[ShippingOrder] where [Id]='"+allorderIds+"' and [Status]=3"
			orderId=database_api.sql_multconn(db_warehouse,sql_orderId)
			#orderId=list(orderId)
			if orderId:
				orderId=str(orderId[0][0])
				sql_weight="select [Weight] from [dbo].[ShippingOrder] where [Id]='"+orderId+"'"
				weight=database_api.sql_conn(db_warehouse,sql_weight)

				url_print=""+login_api.erp_url+"ShippingOrder/GetOrderForPrint"
				postdata_print={"orderIds":[orderId]}
				req_print=login.post(url_print,data=postdata_print)
				print "发货打印返回信息:"+req_print.text

				url_delivery=""+login_api.erp_url+"ShippingOrder/ShippingOrderDelivery"
				postdata_delivery={"orderIds":[orderId],"weight":weight}
				req_delivery=login.post(url_delivery,data=postdata_delivery)
				print "发货返回信息:"+req_delivery.text
				print "\n"

		url_finish=""+login_api.erp_url+"ShippingOrder/FinishCurrentPickingList"
		postdata_finish={"pCode":text_content[0]}
		req_finish=login.post(url_finish,data=postdata_finish)
		print "结束批次返回信息:"+req_finish.text
		
				







