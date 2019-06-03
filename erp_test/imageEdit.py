#-*- coding:utf-8 -*-
import sys
import json
import xlrd
import database_api
import login_api

reload(sys)
sys.setdefaultencoding( "utf-8" )


'''设置登陆'''
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

		sql_imageid="select [Id] from [dbo].[EditingTask_Image] where [Id]='"+taskid_str+"'"
		editimage_id=database_api.sql_multconn(db_edit,sql_imageid)

		db_package="systemmanagementsystem"
		sql_packageId="select [Id] from [dbo].[Package] where [Name]='"+text_content[5]+"'"
		packageId=database_api.sql_conn(db_package,sql_packageId)
		sql_pgWeight="select [Weight] from [dbo].[Package] where [Id]='"+packageId+"'"
		pgWeight=database_api.sql_conn(db_package,sql_pgWeight)

		if editimage_id:
			sql_entityId="select [EntityId] from [dbo].[EditingTask] where [Id]='"+taskid_str+"'"
			entityId=database_api.sql_conn(db_edit,sql_entityId)	
			sql_detailId="select [Id] from [dbo].[ImageTaskDetail] where [ImageTaskId]='"+taskid_str+"'"
			sql_subid="select [SubEntityId] from [dbo].[ImageTaskDetail] where [ImageTaskId]='"+taskid_str+"'"
			imagedetailid=database_api.sql_multconn(db_edit,sql_detailId)
			subid=database_api.sql_multconn(db_edit,sql_subid)

			for i in range(0,len(subid)):
				submitId=str(subid[i][0])
				imagetaskdetailid=str(imagedetailid[i][0])
				
				'''产品头图'''
				url_uploadimage=""+login_api.erp_url+"Products/UpLoadImage"
				headimage=open("./images/"+text_content[11]+"",'rb')
				head_files={'files[]':headimage}
				data1={'imageType':0,'SubEntityId':submitId,'imageTaskDetailId':imagetaskdetailid,'taskId':taskid_str}
				req1=edit_req.post(url_uploadimage,files=head_files,data=data1)
				print "产品图上传信息返回:"+req1.text
				submit=json.loads(req1.text)

				'''产品描述图'''
				imagedetail=open("./images/"+text_content[12]+"",'rb')
				detail_files={'files[]':imagedetail}
				data2={'imageType':1,'SubEntityId':submitId,'imageTaskDetailId':imagetaskdetailid,'taskId':taskid_str}
				req2=edit_req.post(url_uploadimage,files=detail_files,data=data2)
				print "产品描述图上传信息返回:"+req2.text

			'''完成图片编辑'''
			url_submit=""+login_api.erp_url+"Products/SubmitImageTask"
			postdata={"TaskId":taskid_str,"entityId":entityId,"imageName":submit['data']['file']['imageName']}
			req3=edit_req.post(url_submit,data=postdata)
			print "完成图片编辑信息返回:"+req3.text
			