# -*- coding: utf-8 -*-
import time,sys,re,os,socket,datetime,pymysql,urllib2,json
import conf
import dingding
with open('/etc/profile','r') as prof:
	for strs in prof.readlines():
		bb=re.search("export NODE_ENV",strs.strip() )
		if bb:
			area=bb.string.split('=')[1]
cnt={'yueyang':5,'shaoyang':5,'jinzhong':5,'js3mj':5,'hengyang':5,'yongzhou':5,'haian':5,'huaian':5,'leiyang':5,'xiangxiang':5,'xuzhou':5,'nantong':5,'guizhou':5,'wangwang':5,'field':5}
#获取是否有需要告警的信息
sql='select * from (select count(*) cnt ,hostname,errortype,mode from '+area+'error_info where datetime > date_sub(now(), interval 1 hour) and errortype not in (select error_log from exclusion_info) group by errortype,hostname,mode) t1 where t1.cnt >= %s;'
#查询所在主机上的错误信息是否有告警过
alarmsql='select count(*) from alarm_info where datetime > date_sub(now(), interval 1 hour) and hostname=%s and error_log=%s and mode=%s;'
#将发送过告警的信息写入到alarm_info表
sendinsertsql="insert into alarm_info (hostname,datetime,error_log,channel,mode)  values (%s,%s,%s,%s,%s);"
conn = pymysql.connect(host=conf.host,user=conf.user,password=conf.password,database=conf.database,charset=conf.charset)
cursor = conn.cursor()
def WeChatpush(cur,x,name,info):
	data=json.dumps({'content':'The '+name+' node has a lot of ('+str(x)+') error messages.\nSee http://hdlog.tocooltech.com/ for details. \n'+info})
	headers={'Content-Type':'application/json'}
	request = urllib2.Request(conf.url,data,headers)
	for s in range(1,4):
		time.sleep(2)
		try:
			response = urllib2.urlopen(request)
		except Exception as e:
			print "wx异常重试"+s
			continue
		else:
			print "wx正常退出"
			break
	message = response.read()
	returninfo=json.loads(message)
	starus=returninfo['message']
	if starus == 'SUCCESS':
		cur.execute(sendinsertsql,[name,alarmtime,info,'wechat',mode])
		conn.commit()
		print "WeChat告警成功 %s"%(message)
		cur.close()
		return 'ok'
	else:
		return 'err'
def DingDingpush(cur,x,name,info):
	text='The '+name+' node has a lot of ('+str(x)+') error messages.\nSee http://hdlog.tocooltech.com/ for details. \n'+info
	for s in range(1,4):
		time.sleep(2)
		try:
			message=dingding.msg(text)
		except Exception as e:
			print "dd异常重试"+s
			continue
		else:
			print "dd正常退出"
			break
	returninfo=json.loads(message)
	starus=returninfo['errmsg']
	if starus == 'ok':
		cur.execute(sendinsertsql,[name,alarmtime,info,'dingding',mode])
		conn.commit()
		print "DingDing告警成功 %s"%(message)
		cur.close()
		return 'ok'
	else:
		return 'err'


#同一主机上相同类型的告警一个小时只允许发送三次
if __name__ == '__main__':
	cursor.execute(sql,[cnt[area]])
	alarmtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	for line in cursor.fetchall():
		x=line[0]
		name=line[1]
		info=line[2]
		mode=line[3]
		cur = conn.cursor()
		cur.execute(alarmsql,[name,info,mode])
		#定义已经告警的次数
		alarmcnt=cur.fetchone()
		print "alarmcnt is %s : info is %s from %s . %s"%(alarmcnt[0],info,name,mode)
		if alarmcnt[0] < 1:
			sta=WeChatpush(cur,x,name,info)
			if sta != 'ok':
				DingDingpush(cur,x,name,info)
				
		else:
			print "告警超频"
	cursor.close()
	conn.close()
