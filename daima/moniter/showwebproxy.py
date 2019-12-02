# -*- coding: utf-8 -*-
import web
import conf
import MySQLdb
import json
import paramiko
from sshtunnel import SSHTunnelForwarder
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
	if area == 'hengyang':
		port,host = 12307,conf.hengyanghost
	if area == 'leiyang':
		port,host = 12307,conf.leiyanghost
	if area == 'shaoyang':
		port,host = 12307,conf.shaoyanghost
	if area == 'yueyang':
		port,host = 12307,conf.yueyanghost
	if area == 'yongzhou':
		port,host = 12307,conf.yongzhouhost
	if area == 'xiangxiang':
		port,host = 12307,conf.xiangxianghost
	if area == 'wangwang':
		port,host = 12307,conf.wangwanghost
	if area == 'field':
		port,host = 12307,conf.fieldhost
	if area == 'haian':
		port,host = 22175,conf.haianhost
	if area == 'huaian':
		port,host = 22172,conf.huaianhost
	if area == 'nantong':
		port,host = 22178,conf.nantonghost
	if area == 'js3mj':
		port,host = 22187,conf.js3mjhost
	if area == 'xuzhou':
		port,host = 22169,conf.xuzhouhost
	if area == 'jinzhong':
		port,host = 22165,conf.jinzhonghost
	if area == 'guizhou':
		port,host = 22194,conf.guizhouhost
	password = conf.password
	user = conf.user
	database= conf.database
	private_key = paramiko.RSAKey.from_private_key_file('/home/jtcf/.ssh/id_rsa')
	with SSHTunnelForwarder(ssh_address_or_host=(conf.proxyhost, port),ssh_pkey=private_key,ssh_username='jtcf',remote_bind_address=(host, 3306)) as server:
		conn = MySQLdb.connect(host='127.0.0.1', user=user, passwd=password, db=database, charset="utf8mb4",port=server.local_bind_port)
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
			sql='select count(1),hostname,errortype from moniter.error_info where datetime >= curdate() group by errortype,hostname order by 1 desc limit 15;'
		if time == 'week':
			sql='select count(1),hostname,errortype from moniter.error_info where datetime >= DATE_SUB(CURDATE(), INTERVAL 7 DAY) group by errortype,hostname order by 1 desc limit 20;'
		if time == 'month':
			sql='select count(1),hostname,errortype from moniter.error_info where datetime >= DATE_SUB(CURDATE(), INTERVAL 30 DAY) group by errortype,hostname order by 1 desc limit 30;'
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
		sql="SELECT id,error_log from moniter.exclusion_info"
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
                sql="delete from moniter.exclusion_info where id in (%s);"%(did)
		print sql
		jsonload = []
		content = {}
                data=executesql(sql,area,'POST')
		content = {'status':data}
                jsonload.append(content)
                return json.dumps(jsonload)



class insertexcludelog:
	def GET(self,info,area):
		sql="insert into moniter.exclusion_info (error_log)values(\'%s\');"%(info)
		arealist=['hengyang','leiyang','xiangxiang','yueyang','shaoyang','yongzhou','js3mj','nantong','xuzhou','haian','huaian','jinzhong','wangwang','field','guizhou']
		jsonload = []
		content = {}
		for area in arealist:
			data=executesql(sql,area,'POST')
			content = {'status':data}
			jsonload.append(content)
			content = {}
		return json.dumps(jsonload)
			
		
class waringinfo:
	def GET(self, area):
		sql="select datetime,hostname,channel,error_log from moniter.alarm_info order by datetime desc limit 20;"
		data=executesql(sql,area,'GET')
		jsonload = []
		content = {}
		for result in data:
			content = {'datetime':str(result[0]),'hostname':str(result[1]),'status':str(result[2]),'error_log':str(result[3])}
			jsonload.append(content)
			content = {}
		return json.dumps(jsonload)

class showlog:
	def GET(self, area):
		sql="SELECT s.errortype,s.datetime,s.hostname,s.error_log FROM moniter.error_info s order by s.datetime desc limit 100;"
		data=executesql(sql,area,'GET')
		jsonload = []
		content = {}
		for result in data:
			#将unicode转换成str
			info=result[3].encode('unicode-escape').decode('string_escape')
			content = {'errortype':result[0],'datetime':str(result[1]),'hostname':str(result[2]),'error_log':eval(info)}
			jsonload.append(content)
			content = {}
		return json.dumps(jsonload)
if __name__ == "__main__":
	app.run()
