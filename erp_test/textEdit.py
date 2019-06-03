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

		sql_textid="select [Id] from [dbo].[EditingTask_Text] where [Id]='"+taskid_str+"'"
		edittext_id=database.sql_multconn(db_edit,sql_textid)

		db_package="systemmanagementsystem"
		sql_packageId="select [Id] from [dbo].[Package] where [Name]='"+text_content[5]+"'"
		packageId=database_api.sql_conn(db_package,sql_packageId)
		sql_pgWeight="select [Weight] from [dbo].[Package] where [Id]='"+packageId+"'"
		pgWeight=database_api.sql_conn(db_package,sql_pgWeight)
		'''判断是否为文字编辑ID'''
		if edittext_id:
			sql_editMeasurement="select [MustEditMeasurement] from [dbo].[EditingTask_Text] where [Id]='"+taskid_str+"'"
			editMeasurement=database_api.sql_multconn(db_edit,sql_editMeasurement)
			'''请求文字编辑连接地址'''
			textEdit_url=""+login_api.erp_url+"Products/UpdateTextTask"
			'''判断来源是否需要编辑实物属性'''
			#print type(editMeasurement[0][0])			
			if editMeasurement[0][0]:
				sql_entityId="select [EntityId] from [dbo].[EditingTask] where [Id]='"+taskid_str+"'"
				entityId=database_api.sql_conn(db_edit,sql_entityId)			
				postdata2_edittext={"taskId":""+taskid_str+"","taskStatus":2,"languageDataList":[{"cultureCode":"zh-CN","cultureName":"中文","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"en-US","cultureName":"美国","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"en-CA","cultureName":"加拿大","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"en-AU","cultureName":"澳洲","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"en-IE","cultureName":"爱尔兰","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"en-GB","cultureName":"英国","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"de-AT","cultureName":"奥地利","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"de-CH","cultureName":"瑞士","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"de-DE","cultureName":"德国","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"fr-FR","cultureName":"法国","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"es-ES","cultureName":"西班牙","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"it-IT","cultureName":"意大利","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"nl-NL","cultureName":"荷兰","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"ja-JP","cultureName":"日本","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"ru-RU","cultureName":"俄罗斯","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"pt-PT","cultureName":"葡萄牙","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""}],"measurementDataList":[{"entityId":""+entityId+"","tag":"","grossWeight":""+text_content[6]+"","weight":""+text_content[7]+"","length":""+text_content[8]+"","width":""+text_content[9]+"","height":""+text_content[10]+"","package":{"id":""+packageId+"","packageWeight":""+pgWeight+"","storageId":"01602662-74ce-4ab8-aabb-3f6c5e5c9f34"}}],"mustEditMeasurement":"value","cultureCode":"en-US"}
				req_edittext2=urllib2.Request(url=textEdit_url,data=json.dumps(postdata2_edittext),headers=header)
				print "完成文字编辑返回信息:"+edit.open(req_edittext2).read()	
		
			else:
				#print taskid_str
				postdata1_edittext={"taskId":""+taskid_str+"","taskStatus":2,"languageDataList":[{"cultureCode":"zh-CN","cultureName":"中文","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"en-US","cultureName":"美国","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"en-CA","cultureName":"加拿大","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"en-AU","cultureName":"澳洲","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"en-IE","cultureName":"爱尔兰","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"en-GB","cultureName":"英国","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"de-AT","cultureName":"奥地利","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"de-CH","cultureName":"瑞士","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"de-DE","cultureName":"德国","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"fr-FR","cultureName":"法国","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"es-ES","cultureName":"西班牙","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"it-IT","cultureName":"意大利","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"nl-NL","cultureName":"荷兰","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"ja-JP","cultureName":"日本","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"ru-RU","cultureName":"俄罗斯","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""},{"cultureCode":"pt-PT","cultureName":"葡萄牙","title":""+text_content[1]+"","keywords":""+text_content[2]+"","entityDescription":""+text_content[3]+"","declareName":""+text_content[4]+""}],"measurementDataList":[],"mustEditMeasurement":"","cultureCode":"en-US"}
				req_edittext1=urllib2.Request(url=textEdit_url,data=json.dumps(postdata1_edittext),headers=header)
				print "完成文字编辑返回信息:"+edit.open(req_edittext1).read()