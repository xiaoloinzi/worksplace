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
new=login_api.login_requests()

'''读取excel表格'''
excel=xlrd.open_workbook('./data_config.xls')
sh=excel.sheet_by_name("newproduct新品开发")
rows=sh.nrows
cols=sh.ncols

'''读取表头信息'''
list_info=[]
for row in range(0,cols):
	list_info.append(sh.cell_value(0,row))
#print list_info

info=[]	
num=0		
for i in range(1,rows):
		info.append(sh.row_values(i))

		'''数据库连接查询分类ID'''
		category_db='productsystem'
		category_sql="select [Id] from [dbo].[Category] where [Name]='"+info[num][1]+"'"
		info[num][1]=database_api.sql_conn(category_db,category_sql)

		'''数据库连接查询站点ID'''
		site_db='systemmanagementsystem'
		site_sql="select [Id] from [dbo].[Site] where [Name]='"+info[num][4]+"'"
		info[num][4]=database_api.sql_conn(site_db,site_sql)

		'''数据库连接查询供应商ID'''
		supplier_db='purchasesystem'
		supplier_sql="select [Id] from [dbo].[Supplier] where [Name]='"+info[num][13]+"'"
		info[num][13]=database_api.sql_conn(supplier_db,supplier_sql)

		'''搜索仓库ID'''
		db_warehouse='systemmanagementsystem'
		sql_warehouse="select [Id] from [dbo].[Warehouse] where [Name]='"+info[num][26]+"'"
		info[num][26]=database_api.sql_conn(db_warehouse,sql_warehouse)

		dist=dict(zip(list_info,info[num]))

		'''发送添加新品请求'''
		add_url=""+login_api.erp_url+"Purchase/SaveNewProduct"
		postdata_add={'formdata':(None,'%257B%2522actionType%2522%253A%2522add%2522%252C%2522id%2522%253A%2522%2522%252C%2522code%2522%253A%2522%2522%252C%2522imageName%2522%253A%2522%2522%252C%2522categoryId%2522%253A%2522'+dist['category']+'%2522%252C%2522title%2522%253A%2522'+dist['title']+'%2522%252C%2522isVariation%2522%253A'+dist['isVariation']+'%252C%2522type%2522%253A%2522'+dist['itemtype']+'%2522%252C%2522warehouseId%2522%253A%2522'+dist['warehouse']+'%2522%252C%2522siteId%2522%253A%2522'+dist['site']+'%2522%252C%2522competitorItemNumber%2522%253A%2522'+dist['competitorItemNumber']+'%2522%252C%2522referenceImageUrl%2522%253A%2522http%253A%252F%252F'+dist['referenceImageUrl']+'%2522%252C%2522referenceUrl%2522%253A%2522%2522%252C%2522description%2522%253A%2522%253Cp%253E'+dist['description']+'%253C%252Fp%253E%2522%252C%2522needPreparedItems%2522%253A'+dist['needPreparedItems']+'%252C%2522hasQuantityAttribute%2522%253A'+dist['hasQuantityAttribute']+'%252C%2522minimumSaleAmount%2522%253A%2522'+dist['minimumSaleAmount']+'%2522%252C%2522unit%2522%253A%2522'+dist['unit']+'%2522%252C%2522detail%2522%253A%257B%2522id%2522%253A%2522%2522%252C%2522length%2522%253A%2522'+dist['length']+'%2522%252C%2522width%2522%253A%2522'+dist['width']+'%2522%252C%2522height%2522%253A%2522'+dist['height']+'%2522%252C%2522weight%2522%253A%2522'+dist['weight']+'%2522%252C%2522price%2522%253A%2522'+dist['price']+'%2522%252C%2522minimumOrderAmount%2522%253A%2522'+dist['minimumOrderAmount']+'%2522%252C%2522supplierId%2522%253A%2522'+dist['supplier']+'%2522%252C%2522supplierCode%2522%253A%2522'+dist['supplierCode']+'%2522%252C%2522supplierDeliveryDays%2522%253A%2522'+dist['supplierDeliveryDays']+'%2522%252C%2522mustCombined%2522%253A'+dist['mustCombined']+'%252C%2522isFirstOrderCommission%2522%253A'+dist['isFirstOrderCommission']+'%252C%2522type%2522%253A%2522'+dist['itemtype']+'%2522%252C%2522currency%2522%253A%2522'+dist['currency']+'%2522%252C%2522purchaseLink%2522%253A%2522'+dist['purchaseLink']+'%2522%252C%2522purchaseLinkType%2522%253A%2522'+dist['purchaseLinkType']+'%2522%257D%252C%2522files%2522%253A%255B%255D%257D')}

		#postdata={'actionType':'add','id':'','code':'','imageName':'','categoryId':dist['category'],'title':dist['title'],'isVariation':dist['isVariation'],'type':dist['itemtype'],'warehouseId':'01602662-74ce-4ab8-aabb-3f6c5e5c9f34','siteId':dist['site'],'competitorItemNumber':dist['competitorItemNumber'],'referenceImageUrl':'http'+dist['referenceImageUrl']+'',}
		req_add=new.post(add_url,data=postdata_add)
		print "添加新品返回信息:" + req_add.text
