#-*- coding:utf-8 -*-
import sys
import requests
import xlrd
import database_api
import login_api
import urllib
import urllib2
import json
import time

reload(sys)
sys.setdefaultencoding( "utf-8" )

header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36","Content-Type": "application/x-www-form-urlencoded",
"Accept": "application/json","X-Requested-With": "XMLHttpRequest","Accept-Encoding": "gzip, deflate"}

'''登录pda设置'''
pda=login_api.login_pda_urllib()

'''读取excel表格'''
excel=xlrd.open_workbook('./data_config.xls')
sh=excel.sheet_by_name("DistributeSku配货")
rows=sh.nrows

for i in range(1,rows):
	text_content=sh.row_values(i)

	url_ScanSerialNumber=""+login_api.pda_url+"ajax/Distribute/ScanSerialNumber"
	postdata_ScanSerialNumber=urllib.urlencode({"SerialNumber":text_content[1]})
	req_ScanSerialNumber=urllib2.Request(url_ScanSerialNumber,postdata_ScanSerialNumber,header)
	print "扫描批次卡返回信息:"+pda.open(req_ScanSerialNumber).read()

	db_warehouse="warehousesystem"
	'''获取拣货单id'''
	sql_pickingid="select [Id] from [dbo].[PickingList] where [Code]='"+text_content[0]+"'"
	pickingListId=database_api.sql_conn(db_warehouse,sql_pickingid)

	'''获取拣货单对应的SKUID'''
	sql_skuids="select [SkuId] from [dbo].[DistributeSkuList] where [PickingListId]='"+pickingListId+"'"
	skuids=database_api.sql_multconn(db_warehouse,sql_skuids)
	# skulist=[]
	for j in skuids:
		skuid=str(j[0])
		'''获取SKUID对应的SKUCODE'''
		sql_skucode="select [Code] from [dbo].[Sku] where [Id]='"+skuid+"'"
		skucode=database_api.sql_conn(db_warehouse,sql_skucode)
		print skuid
		url_scansku=""+login_api.pda_url+"ajax/Distribute/ScanSkuCode"
		postdata_scansku=urllib.urlencode({"SkuCode":skucode,"PickingListId":pickingListId,"ShippingOrderID":""})
		req_scansku=urllib2.Request(url_scansku,postdata_scansku,header)
		scan_info=pda.open(req_scansku).read()
		print "扫描sku返回信息:"+scan_info

		scan_dic=json.loads(scan_info)

		try:
			ToDistributeAmount=scan_dic['data']['dataMeta']['ToDistributeAmount']
			DistributedAmount=scan_dic['data']['dataMeta']['DistributedAmount']
			ShippingOrderId=scan_dic['data']['dataMeta']['ShippingOrderId']

			# print ToDistributeAmount,DistributedAmount,ShippingOrderId

			if ToDistributeAmount>DistributedAmount:
				for i in range(0,int(ToDistributeAmount)-int(DistributedAmount)):
					url_summitsku=""+login_api.pda_url+"ajax/Distribute/SummitSkuCode"
					postdata_summitsku=urllib.urlencode({"SkuCode":skucode,"PickingListId":pickingListId,"ShippingOrderId":ShippingOrderId,"AddAmount":1})
					req_summitsku=urllib2.Request(url_summitsku,postdata_summitsku,header)
					print "提交sku返回信息:"+pda.open(req_summitsku).read()
		except:
			print "当前sku已配货完毕"

	time.sleep(1)		

	url_complete=""+login_api.pda_url+"ajax/Distribute/CurrentDistributerCompleted"
	postdata_complete=urllib.urlencode({"PickingListId":pickingListId})
	req_complete=urllib2.Request(url_complete,postdata_complete,header)
	print "完成配货返回信息:"+pda.open(req_complete).read()

	url_GetExceptionSkuNum=""+login_api.pda_url+"ajax/Distribute/GetExceptionSkuNum"
	postdata_GetExceptionSkuNum=urllib.urlencode({"PickingListId":pickingListId})
	req_GetExceptionSkuNum=urllib2.Request(url_GetExceptionSkuNum,postdata_GetExceptionSkuNum,header)
	print "获取异常SKU信息:"+pda.open(req_GetExceptionSkuNum).read()

	url_comfirm=""+login_api.pda_url+"ajax/Distribute/ConfirmCompleted"
	postdata_comfirm=urllib.urlencode({"PickingListId":pickingListId})
	req_comfirm=urllib2.Request(url_comfirm,postdata_comfirm,header)
	print "确认完成配货返回信息:"+pda.open(req_comfirm).read()

