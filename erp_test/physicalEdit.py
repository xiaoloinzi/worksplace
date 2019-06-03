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
sh=excel.sheet_by_name("editproduct产品编辑")
rows=sh.nrows

for i in range(1,rows):
	text_content=sh.row_values(i)
	'''根据产品编码查询任务id'''
	db_edit="editingsystem"
	sql_Id="select [Id] from [dbo].[EditingTask] where [EntityCode]='"+text_content[0]+"'"
	editTaskid=database_api.sql_multconn(db_edit,sql_Id)
	for taskid in editTaskid:
		taskid_str=str(taskid[0])
		
		sql_physicalid="select [Id] from [dbo].[EditingTask_Physical] where [Id]='"+taskid_str+"'"
		editphysical_id=database_api.sql_multconn(db_edit,sql_physicalid)

		db_package="systemmanagementsystem"
		sql_packageId="select [Id] from [dbo].[Package] where [Name]='"+text_content[5]+"'"
		packageId=database_api.sql_conn(db_package,sql_packageId)
		sql_pgWeight="select [Weight] from [dbo].[Package] where [Id]='"+packageId+"'"
		pgWeight=database_api.sql_conn(db_package,sql_pgWeight)

		if editphysical_id:
			editphysical_url=""+login_api.erp_url+"Products/UpdatePhysicalTask"
			postdata_editphysical={"taskId":""+taskid_str+"","taskStatus":2,"netWeight":""+text_content[7]+"","length":""+text_content[8]+"","width":""+text_content[9]+"","height":""+text_content[10]+"","grossWeight":""+text_content[6]+"","package":{"id":""+packageId+"","packageWeight":""+pgWeight+"","storageId":"01602662-74ce-4ab8-aabb-3f6c5e5c9f34"}}
			req_editphysical=urllib2.Request(url=editphysical_url,data=json.dumps(postdata_editphysical),headers=header)
			print "完成实物编辑返回信息:"+edit.open(req_editphysical).read()