# -*- coding: utf-8 -*-
import time,sys,re,os,socket,datetime,pymysql,urllib2,json
import conf
import dingding
with open('/etc/profile','r') as prof:
	for strs in prof.readlines():
		bb=re.search("export NODE_ENV",strs.strip() )
		if bb:
			area=bb.string.split('=')[1]
cnt={'yueyang':5,'shaoyang':5,'jinzhong':5,'js3mj':5,'hengyang':5,'yongzhou':5,'haian':5,'huaian':5,'leiyang':5,'xiangxiang':5,'xuzhou-test':5,'nantong':5}
#获取是否有需要告警的信息
sql='select * from (select count(*) cnt ,hostname,errortype from error_info where datetime >=date_sub(now(), interval 0.5 hour) and errortype not in (select error_log from exclusion_info) group by errortype,hostname) t1 where t1.cnt >= %s;'
#查询所在主机上的错误信息是否有告警过
alarmsql='select count(*) from alarm_info where datetime >=date_sub(now(), interval 1 hour) and hostname=%s and error_log=%s and channel=%s;'
#将发送过告警的信息写入到alarm_info表
sendinsertsql="insert into alarm_info (hostname,datetime,error_log,channel)  values (%s,%s,%s,%s);"
conn = pymysql.connect(host=conf.host,user=conf.user,password=conf.password,database=conf.database,charset=conf.charset)
cursor = conn.cursor()
#同一主机上相同类型的告警一个小时只允许发送三次
if __name__ == '__main__':
	for channel in ['wechat','dingding']:
		cursor.execute(sql,[cnt[area]])
		alarmtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		for line in cursor.fetchall():
			x=line[0]
			name=line[1]
			info=line[2]
			cur = conn.cursor()
			cur.execute(alarmsql,[name,info,channel])
			#定义已经告警的次数
			alarmcnt=cur.fetchone()
			print "alarmcnt is %s : info is %s"%(alarmcnt[0],info)
			if alarmcnt[0] < 3:
				if channel == "dingding":
					text='The '+name+' node has a lot of ('+str(x)+') error messages.\nSee http://errorlog.5292game.com/ for details. \n'+info
					message=dingding.msg(text)
					returninfo=json.loads(message)
					starus=returninfo['errmsg']
					print starus
					if starus == 'ok':
						cur.execute(sendinsertsql,[name,alarmtime,info,channel])
						conn.commit()
						print "DingDing告警成功 %s"%(message)
						cur.close()
				if channel == "wechat":
					data=json.dumps({'content':'The '+name+' node has a lot of ('+str(x)+') error messages.\nSee http://errorlog.5292game.com/ for details. \n'+info})
					headers={'Content-Type':'application/json'}
					request = urllib2.Request(conf.url,data,headers)
					response = urllib2.urlopen(request)
					message = response.read()
					returninfo=json.loads(message)
					print message
					starus=returninfo['message']
					print starus
                                        if starus == 'SUCCESS':
                                                cur.execute(sendinsertsql,[name,alarmtime,info,channel])
                                                conn.commit()
                                                print "WeChat告警成功 %s"%(message)
                                                cur.close()
						time.sleep(3)
			else:
				print "%s告警超频"%(channel)
	cursor.close()
	conn.close()
