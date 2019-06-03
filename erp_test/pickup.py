#-*- coding:utf-8 -*-
import sys
import requests
import xlrd
import database_api
import login_api
import urllib
import urllib2
import json

reload(sys)
sys.setdefaultencoding( "utf-8" )

header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36","Content-Type": "application/x-www-form-urlencoded",
"Accept": "application/json","X-Requested-With": "XMLHttpRequest","Accept-Encoding": "gzip, deflate"}

'''登录pda设置'''
pda=login_api.login_pda_urllib()

'''读取excel表格'''
excel=xlrd.open_workbook('./data_config.xls')
sh=excel.sheet_by_name("pickup拣货")
rows=sh.nrows

for i in range(1,rows):
	text_content=sh.row_values(i)

	db_warehouse="warehousesystem"
	'''获取拣货单id'''
	sql_pickingid="select [Id] from [dbo].[PickingList] where [Code]='"+text_content[0]+"'"
	pickingListId=database_api.sql_conn(db_warehouse,sql_pickingid)
	#print pickingListId

	'''输入批次卡'''
	url_batchcard=""+login_api.pda_url+"ajax/Picking/UpdatePickingListBatchCard"
	postdata_batchcard=urllib.urlencode({"PickingListId":pickingListId,"SerialNumber":text_content[1]}).encode('utf-8')
	req_batchcard=urllib2.Request(url_batchcard,postdata_batchcard,header)
	print "输入批次卡返回信息:"+pda.open(req_batchcard).read()

	if text_content[2]:
		sku=text_content[2].split(',')
		for j in sku:
			'''获取skuid'''
			sql_skuid="select [Id] from [dbo].[Sku] where [Code]='"+j+"'"
			skuid=database_api.sql_conn(db_warehouse,sql_skuid)
			# print skuid

			'''获取Taskid'''
			sql_picktaskid="select [PickingTaskId] from [dbo].[PickSkuList] where [SkuId]='"+skuid+"' and [PickingListId]='"+pickingListId+"' and [PickedAmount]=0"
			picktaskid=database_api.sql_conn(db_warehouse,sql_picktaskid)
			
			'''获取sku数量'''
			sql_skuamount="select [ToPickAmount] from [dbo].[PickSkuList] where [SkuId]='"+skuid+"' and [PickingListId]='"+pickingListId+"' and [PickedAmount]=0"
			skuamount=database_api.sql_conn(db_warehouse,sql_skuamount)

			'''sku拣货'''
			url_SingleSkuCompleted=""+login_api.pda_url+"ajax/Picking/SingleSkuCompleted"
			postdata_SingleSkuCompleted=urllib.urlencode({"rqjson":"{\"PickingListID\":\""+pickingListId+"\",\"PickingTaskID\":\""+picktaskid+"\",\"SkuId\":\""+skuid+"\",\"Qty\":\""+skuamount+"\"}"}).encode('utf-8')
			#print type(postdata_SingleSkuCompleted)
			req_SingleSkuCompleted=urllib2.Request(url_SingleSkuCompleted,postdata_SingleSkuCompleted,header)
			print "sku拣货返回信息:"+pda.open(req_SingleSkuCompleted).read()
			print "\n"

		'''标记缺货'''
		sql_stockout="select [SkuId] from [dbo].[PickSkuList] where [PickingListId]='"+pickingListId+"' and [PickedAmount]=0"
		stockout=database_api.sql_multconn(db_warehouse,sql_stockout)
		#print stockout
		for k in stockout:
			stockoutid=str(k[0])
			url_stockout=""+login_api.pda_url+"ajax/Picking/SkuStockout"
			postdata_stockout=urllib.urlencode({"rqjson":"{\"PickingListID\":\""+pickingListId+"\",\"PickingTaskID\":\""+picktaskid+"\",\"SkuId\":\""+stockoutid+"\",\"Qty\":\"0\",\"TryMatch\":\"true\"}"}).encode('utf-8')
			req_stockout=urllib2.Request(url_stockout,postdata_stockout,header)
			print "标记缺货:"+pda.open(req_stockout).read()
			postdata_surestockout=urllib.urlencode({"rqjson":"{\"PickingListID\":\""+pickingListId+"\",\"PickingTaskID\":\""+picktaskid+"\",\"SkuId\":\""+stockoutid+"\",\"Qty\":\"0\",\"TryMatch\":\"false\"}"}).encode('utf-8')
			req_surestockout=urllib2.Request(url_stockout,postdata_surestockout,header)
			print "确认标记缺货:"+pda.open(req_surestockout).read()
			print "\n"
	else:

		sql_skuid="select [SkuId] from [dbo].[PickSkuList] where [PickingListId]='"+pickingListId+"' and [PickedAmount]=0"
		skuid=database_api.sql_multconn(db_warehouse,sql_skuid)
		for m in skuid:
			allskuid=str(m[0])
			'''获取Taskid'''
			sql_picktaskid="select [PickingTaskId] from [dbo].[PickSkuList] where [SkuId]='"+allskuid+"' and [PickingListId]='"+pickingListId+"' and [PickedAmount]=0"
			picktaskid=database_api.sql_conn(db_warehouse,sql_picktaskid)

			'''获取sku数量'''
			sql_skuamount="select [ToPickAmount] from [dbo].[PickSkuList] where [SkuId]='"+allskuid+"' and [PickingListId]='"+pickingListId+"' and [PickedAmount]=0"
			skuamount=database_api.sql_conn(db_warehouse,sql_skuamount)

			'''sku拣货'''
			url_SingleSkuCompleted=""+login_api.pda_url+"/ajax/Picking/SingleSkuCompleted"
			postdata_SingleSkuCompleted=urllib.urlencode({"rqjson":"{\"PickingListID\":\""+pickingListId+"\",\"PickingTaskID\":\""+picktaskid+"\",\"SkuId\":\""+allskuid+"\",\"Qty\":\""+skuamount+"\"}"}).encode('utf-8')
			#print type(postdata_SingleSkuCompleted)
			req_SingleSkuCompleted=urllib2.Request(url_SingleSkuCompleted,postdata_SingleSkuCompleted,header)
			print "sku拣货返回信息:"+pda.open(req_SingleSkuCompleted).read()
			print "\n"

	'''归配货框'''
	sql_boundid="select [Id] from [dbo].[PickingTask] where [PickingListId]='"+pickingListId+"' and ([Status]=0 or [Status]=1)"
	boundid=database_api.sql_multconn(db_warehouse,sql_boundid)
	for n in boundid:
		allboundid=str(n[0])
		url_bound=""+login_api.pda_url+"ajax/Picking/ToBound"
		postdata_bound=urllib.urlencode({"SerialNumber":text_content[1],"PickingListId":pickingListId,"PickingTaskID":allboundid})
		req_bount=urllib2.Request(url_bound,postdata_bound,header)
		print "归配货框返回信息:"+pda.open(req_bount).read()







