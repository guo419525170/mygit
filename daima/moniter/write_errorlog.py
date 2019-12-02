# -*- coding: utf-8 -*-
import time,sys,re,os,socket,datetime,pymysql
import conf
hostname=socket.gethostname()
tablename=hostname.split('-')[0]+'error_info'
stopline=str(time.strftime("%Y-%m-%d", time.localtime()))+' 23:58:00'
stoptime=int(time.mktime(time.strptime(stopline, "%Y-%m-%d %H:%M:%S")))
logname=sys.argv[1]
#logname='/usr/local/script/moniter/test.log'
mode=sys.argv[2]
#mode='game'


def execute(sql,hostname,mode,writetime,errortype,fullinfo):
	conn = pymysql.connect(host=conf.host,user=conf.user,password=conf.password,database=conf.database,charset=conf.charset)
	cursor = conn.cursor()
	cursor.execute(sql,[hostname,mode,writetime,errortype,str(fullinfo)])
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
	logfile = open(logname,"r")
	loglines = follow(logfile)
	fullinfo=[]
	for line in loglines:
		ontime = int(time.mktime(datetime.datetime.now().timetuple()))
		if ontime > stoptime:
                        sys.exit(0)
		sql="insert into "+tablename+" (hostname,mode,datetime,errortype,error_log)  values (%s,%s,%s,%s,%s);"
		writetime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		typeerrorstr=re.findall(r'[TypeError|ReferenceError|SyntaxError]:.+\s+at .+[\d|\)]',line)
		if len(typeerrorstr) > 0:
			typeerrorlist=typeerrorstr[0].split('\\n')
			print "错误类型：%s 错误详情：%s"%(typeerrorlist[0],typeerrorlist)
			execute(sql,hostname,mode,writetime,typeerrorlist[0],typeerrorlist)
		#errorlist=re.findall(r'(^Error:.+)|(^ReferenceError:.+)|(^TypeError:.+)|(^SyntaxError:.+)|(uncaughtException.+)|(^\s+ .+)|(^\s+at .+[\d|\)|\}])|(^\s+[a-zA-Z]+: .+)',line)
		errorlist=re.findall(r'(^Error:.+)|(^ReferenceError:.+)|(^TypeError:.+)|(^SyntaxError:.+)|(uncaughtException.+)|(^\s+ .+)',line)
		if len(errorlist):
			for info in errorlist[0]:
				if info != '':
					infos=re.sub('uncaughtException\s+[\{|\[] ','',info)
					fullinfo.append(infos)
		else:
			if len(fullinfo):
				etypeidx=[i for i,x in enumerate(fullinfo) if x.find('Error:')!=-1]
				if len(etypeidx):
					etype=fullinfo[etypeidx[0]]
				else:
					etype=r'Incorrect format did not get a specific type'
				errortype=re.sub('pkroom\d+','pkroom',etype)
				print errortype
				fullinfo2 = sorted(set(fullinfo),key=fullinfo.index)
				execute(sql,hostname,mode,writetime,errortype,fullinfo2)
				print fullinfo2
			fullinfo=[]
