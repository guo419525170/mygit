# -*- coding: utf-8 -*-
import time,sys,re,os,socket,datetime,pymysql
import conf
hostname=socket.gethostname()
stopline=str(time.strftime("%Y-%m-%d", time.localtime()))+' 23:30:00'
stoptime=int(time.mktime(time.strptime(stopline, "%Y-%m-%d %H:%M:%S")))
logname=str(time.strftime("%Y%m%d", time.localtime()))+'.txt'

def execute(sql,hostname,writetime,errortype,fullinfo):
	conn = pymysql.connect(host=conf.host,user=conf.user,password=conf.password,database=conf.database,charset=conf.charset)
	cursor = conn.cursor()
	cursor.execute(sql,[hostname,writetime,errortype,str(fullinfo)])
	conn.commit()
	cursor.close()
	conn.close()


def follow(thefile):
	thefile.seek(1,2)
	while True:
		line = thefile.readline()
		if not line:
			time.sleep(0.1)
			continue
		yield line

if __name__ == '__main__':
	logfile = open(conf.logpath+logname,"r")
	loglines = follow(logfile)
	fullinfo=[]
	for line in loglines:
		ontime = int(time.mktime(datetime.datetime.now().timetuple()))
		if ontime > stoptime:
                        sys.exit(0)
		sql="insert into error_info (hostname,datetime,errortype,error_log)  values (%s,%s,%s,%s);"
		writetime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		typeerrorstr=re.findall(r'TypeError:.+\s+at .+\d\)',line)
		if len(typeerrorstr) > 0:
			typeerrorlist=typeerrorstr[0].split('\\n')
			execute(sql,hostname,writetime,typeerrorlist[0],typeerrorlist)
		errorlist=re.findall(r'(^Error:.+)|(^TypeError:.+)|(^SyntaxError:.+)|(^\s+at .+[\d|\)])',line)
		if len(errorlist):
			for info in errorlist[0]:
				if info != '':
					fullinfo.append(info)
		else:
			if len(fullinfo):
				errortype=re.sub('pkroom\d+','pkroom',fullinfo[0])
				execute(sql,hostname,writetime,errortype,fullinfo)
			fullinfo=[]

