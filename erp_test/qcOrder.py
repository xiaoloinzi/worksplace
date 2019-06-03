#-*- coding:utf-8 -*-
import sys
import json
import requests
import xlrd
import database_api
import login_api
import time
import urllib2

reload(sys)
sys.setdefaultencoding( "utf-8" )

header = {'Connection':' keep-alive','Accept': 'application/json, text/javascript, */*; q=0.01','X-Requested-With': 'XMLHttpRequest','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0','Content-Type': 'application/json','Accept-Encoding': 'gzip, deflate','Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6'}

'''设置登陆session'''
login=login_api.login_requests()
login2=login_api.login_urllib()

excel=xlrd.open_workbook('./data_config.xls')
sh=excel.sheet_by_name("qcOrder生成质检")
rows=sh.nrows

db_purchasesystem="purchasesystem"
db_warehousesystem="warehousesystem"

'''查询可以生成到货单的采购单ID，数据配置需要生成几个，查询语句就写Top几'''
# n=str(rows-1)
sql_caigouid="Select Top 4 [Id],[OrderNumber] From [dbo].[PurchaseOrder] Where [Type]=0 And [IsSync]=0 And [Status]=0 And [Freight] IS NOT NULL Order By [Created]"
caigouid=database_api.sql_multconn(db_purchasesystem,sql_caigouid)
# print caigouid

caigoulist=[]
for j in caigouid:
	cgd=str(j[1])
	caigoulist.append(cgd)
print "采购单号：%s" % (caigoulist)
print '\n'

pg=1
area=1
baoguo=[]
cgids=[]

'''添加包裹并生成到货单'''
for i in caigouid:
	cgid=str(i[0])
	cgids.append(cgid)
	#print cgid
	sql_caigou="Select [PurchaseOrderId] From [dbo].[LogisticsPackages] Where [PurchaseOrderId]='"+cgid+"'"
	caigou=database_api.sql_multconn(db_purchasesystem,sql_caigou)
	# print caigou
	if caigou:
		a=caigou
	else:
		#print cgid
		text_content=sh.row_values(pg)
		logistnum=text_content[0].split(',')
		for k in logistnum:
			url_caigou=""+login_api.erp_url+"Purchase/AddLogisticsNumber"
			postdata_caigou={"id":cgid,"logisticsNumber":k}
			req_caigou=login.post(url_caigou,data=postdata_caigou)
			caigou_info=req_caigou.text
			print caigou_info
			baoguoid=json.loads(caigou_info)
			baoguo.append(baoguoid['data'])
			print "添加包裹："+caigou_info		
		pg=pg+1	

'''生成到货单'''
url_daohuo=""+login_api.erp_url+"Purchase/SubmitToArrivalOrder"
postdata_daohuo={"orderIdList":cgids}
req_daohuo=login.post(url_daohuo,data=postdata_daohuo)
print "生成到货单："+req_daohuo.text

'''签收并上架到货单'''
for j in caigouid:
	cgid=str(j[0])
	# print cgid
	text_content=sh.row_values(area)

	sql_areaid="Select [Id] From [dbo].[Area] Where [Name]='"+text_content[1]+"'"
	areaid=database_api.sql_conn(db_warehousesystem,sql_areaid)

	sql_daohuoid="Select [Id] From [dbo].[InRequest] Where [PurchaseId]='"+cgid+"'"
	daohuoid=database_api.sql_conn(db_warehousesystem,sql_daohuoid)
	# print daohuoid

	'''到货单签收包裹'''
	url_sign=""+login_api.erp_url+"InRequest/BatchSignLogisticsPackage"
	postdata_sign={"requestModel":[{"PurchaseId":daohuoid,"listPackgeId":baoguo}],"areaId":areaid,"areaCode":text_content[1]}
	req_sign=urllib2.Request(url=url_sign,data=json.dumps(postdata_sign),headers=header)
	print "签收："+login2.open(req_sign).read()

	time.sleep(1)

	'''到货单上架包裹'''
	url_ruku=""+login_api.erp_url+"InRequest/BatchWarehouseIn"
	postdata_ruku={"requestModel":[{"purchaseId":daohuoid,"listPackgeId":baoguo}]}
	req_ruku=urllib2.Request(url=url_ruku,data=json.dumps(postdata_ruku),headers=header)
	print "上架："+login2.open(req_ruku).read()
	area=area+1
	time.sleep(1)