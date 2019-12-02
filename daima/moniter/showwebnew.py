# -*- coding: utf-8 -*-
import web
import conf
import pymysql
import json
import sys
reload(sys)
sys.setdefaultencoding("utf8")
urls = (
	'/api/showlog/(.*)', 'showlog',
	'/api/count/env=(.*)&time=(.*)','count',
	'/api/excludelog/(.*)','excludelog',
	'/api/delexclog/id=(.*)&env=(.*)','delexclog',
	'/api/waringinfo/(.*)','waringinfo',
	'/api/insertexcludelog/info=(.*)&env=(.*)','insertexcludelog',
)
app = web.application(urls, globals())
def executesql(sql,area,types):
	passd = conf.password
	us = conf.user
	dbs= conf.database
	ht=conf.host
	conn = pymysql.connect(host=ht,user=us,passwd=passd,db=dbs,charset='utf8mb4')
	cur = conn.cursor()
	if types == 'POST':
		try:
			cur.execute(sql)
		except Exception as e:
			conn.rollback()
			data=0
			print data
		else:
			conn.commit()
			data=1
			print data
	else:
		cur.execute(sql)
		data = cur.fetchall()
	cur.close()
	conn.close()
	return data

class count:
	def GET(self,area,time):
		if time == 'day':
			sql='select count(1),hostname,errortype from '+area+'error_info where datetime >= curdate() group by errortype,hostname order by 1 desc limit 15;'
		if time == 'week':
			sql='select count(1),hostname,errortype from '+area+'error_info where datetime >= DATE_SUB(CURDATE(), INTERVAL 7 DAY) group by errortype,hostname order by 1 desc limit 20;'
		if time == 'month':
			sql='select count(1),hostname,errortype from '+area+'error_info where datetime >= DATE_SUB(CURDATE(), INTERVAL 30 DAY) group by errortype,hostname order by 1 desc limit 30;'
		data=executesql(sql,area,'GET')
		jsonload = []
                content = {}
		for result in data:
			content = {'num':result[0],'hostname':str(result[1]),'error_log':str(result[2])}
			jsonload.append(content)
			content = {}
		return json.dumps(jsonload)


class excludelog:
	def GET(self, area):
		sql="SELECT id,error_log from exclusion_info"
		data=executesql(sql,area,'GET')
		jsonload = []
		content = {}
		for result in data:
			content = {'id':result[0],'error_log':str(result[1])}
			jsonload.append(content)
			content = {}
		return json.dumps(jsonload)
class delexclog:
        def GET(self,did,area):
		print did,area
                sql="delete from exclusion_info where id in (%s);"%(did)
		print sql
		jsonload = []
		content = {}
                data=executesql(sql,area,'POST')
		content = {'status':data}
                jsonload.append(content)
                return json.dumps(jsonload)



class insertexcludelog:
	def GET(self,info,area):
		sql="insert into exclusion_info (error_log)values(\"%s\");"%(info)
		jsonload = []
		content = {}
		data=executesql(sql,area,'POST')
		content = {'status':data}
		jsonload.append(content)
		content = {}
		return json.dumps(jsonload)
			
		
class waringinfo:
	def GET(self, area):
		sql="select datetime,hostname,channel,error_log,mode from alarm_info where hostname like '"+area+"%' order by datetime desc limit 20;"
		print sql
		data=executesql(sql,area,'GET')
		jsonload = []
		content = {}
		for result in data:
			content = {'datetime':str(result[0]),'hostname':str(result[1]),'status':str(result[2]),'error_log':str(result[3]),'mode':str(result[4])}
			jsonload.append(content)
			content = {}
		return json.dumps(jsonload)

class showlog:
	def GET(self, area):
		sql="SELECT s.errortype,s.datetime,s.hostname,s.mode,s.error_log FROM "+area+"error_info s order by s.datetime desc limit 100;"
		data=executesql(sql,area,'GET')
		jsonload = []
		content = {}
		for result in data:
			#将unicode转换成str
			info=result[4].encode('unicode-escape').decode('string_escape')
			content = {'errortype':result[0],'datetime':str(result[1]),'hostname':str(result[2]),'mode':str(result[3]),'error_log':eval(info)}
			jsonload.append(content)
			content = {}
		return json.dumps(jsonload)
if __name__ == "__main__":
	app.run()
