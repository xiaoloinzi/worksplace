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
edit_req=login_api.login_requests()

'''读取excel表格'''
excel=xlrd.open_workbook('./data_config.xls')
sh=excel.sheet_by_name("addpurchase添加采购单")
rows=sh.nrows

for i in range(1,rows):
	text_conten=sh.row_values(i)
	db_productsystem="productsystem"
	product_id=text_conten[0].split(',')
	product_num=text_conten[2].split(',')
	product_price=text_conten[3].split(',')
	details=[]

	'''添加新品采购单'''
	for j in product_id:
		sql_detailId="select [Id] from [dbo].[NewProductDetail] where [Code]='"+j+"'"
		detailId=database_api.sql_conn(db_productsystem,sql_detailId)
		details.append(detailId)
	
	
	url_addpurchase=""+login_api.erp_url+"Purchase/BatchGeneratedPurchaseBorrow"
	postdata_addpurchase={"warehouseId":"01602662-74ce-4ab8-aabb-3f6c5e5c9f34","generatedPurchase":"true","detailIds":details}
	req_add=edit_req.post(url_addpurchase,data=postdata_addpurchase)
	print "添加新品采购单返回信息:"+req_add.text

	'''保存编辑采购单'''
	db_purchase="purchasesystem"
	sql_orderid="select [OrderId] from [dbo].[NewProductPurchaseOrderDetail] where [SkuCode]='"+product_id[0]+"'"
	orderId=database_api.sql_conn(db_purchase,sql_orderid)
	pdetails_list=[]
	for num in range(0,len(product_id)):
		pdetails_dic={}
		sql_pdetailId="select [Id] from [dbo].[NewProductPurchaseOrderDetail] where [SkuCode]='"+product_id[num]+"'"
		pdetailId=database_api.sql_conn(db_purchase,sql_pdetailId)
		pdetails_dic.update({"id":pdetailId,"quantity":product_num[num],"priceForCurrency":product_price[num]})
		pdetails_list.append(pdetails_dic)

	url_update=""+login_api.erp_url+"Purchase/BatchUpdateNewProductPurchaseOrderDetail"
	postdata_update={"orderId":orderId,"freight":text_conten[1],"details":pdetails_list}
	req_update=urllib2.Request(url=url_update,data=json.dumps(postdata_update),headers=header)
	print "保存编辑采购单饭回信息:"+edit.open(req_update).read()

	'''提交编辑采购单'''
	url_submit=""+login_api.erp_url+"Purchase/SubmitNewProductPurchaseOrder"
	postdata_submit={"orderIdList":[orderId]}
	req_submit=edit_req.post(url_submit,data=postdata_submit)
	print "提交采购单返回信息:"+req_submit.text

	'''签收采购单'''
	db_editingsystem="editingsystem"
	sql_batchid="select [Id] from [dbo].[EntityReceivingBatch] where [EntityId]='"+orderId+"'"
	batchid=database_api.sql_conn(db_editingsystem,sql_batchid)
	url_sign=""+login_api.erp_url+"Products/SignInEntityReceivingBatch"
	postdata_sign={"batchIdList":[batchid],"isSign":"true"}
	req_sign=urllib2.Request(url=url_sign,data=json.dumps(postdata_sign),headers=header)
	print "签收采购单返回信息:"+edit.open(req_sign).read()
	







