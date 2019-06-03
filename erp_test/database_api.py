#-*- coding:utf-8 -*-
import sys
import pymssql

reload(sys)
sys.setdefaultencoding( "utf-8" )

def sql_conn(db_name,sql):
	conn=pymssql.connect(host='192.168.1.200',user='sa',password='Idh#168',database=db_name)
	cur=conn.cursor()
	cur.execute(sql)
	List=cur.fetchall()
	#print "ceshi",List
	cur.close()
	conn.close()
	ID=str(List[0][0])
	return ID

def sql_multconn(db_name,sql):
	conn=pymssql.connect(host='192.168.1.200',user='sa',password='Idh#168',database=db_name)
	cur=conn.cursor()
	cur.execute(sql)
	List=cur.fetchall()
	#print "ceshi",List
	cur.close()
	conn.close()
	return List



