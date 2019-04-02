# -*- coding: utf-8 -*-
import time,sys,re,os,socket,datetime
with open('/etc/profile','r') as prof:
	for strs in prof.readlines():
		bb=re.search("export NODE_ENV",strs.strip() )
		if bb:
			area=bb.string.split('=')[1]

cnt={'yueyang':10,'shaoyang':10,'jinzhong':10,'js3mj':5,'hengyang':5,'yongzhou':5,'haian':5,'huaian':5,'leiyang':5,'xiangxiang':5,'xuzhou':5,'nantong':5}
hostname=socket.gethostname()

#stoptime = int((datetime.datetime.now()+datetime.timedelta(hours=2.5)).strftime('%Y%m%d%H%M'))
#logname=str(time.strftime("%Y%m%d", time.localtime()))+'.txt'
logname="/data/shell/1.txt"
def follow(thefile):
	thefile.seek(1,2)
	while True:
		line = thefile.readline()
		if not line:
			time.sleep(0.1)
			continue
		yield line

if __name__ == '__main__':
	flog=0 #标记错误出现次数
	i=1 #标记邮件发送次数
	y=0 #标记正常日志连续出现的次数
#	logfile = open("/root/logs/game/"+logname,"r")
	logfile = open(logname,"r")
	loglines = follow(logfile)
	for line in loglines:
		y+=1
		ontime = int(time.strftime("%Y%m%d%H%M", time.localtime()))
#		if ontime > stoptime:
#                        sys.exit(0)
		errorlist=re.findall(r'Error:',line)
                print errorlist
		#errorlist=re.findall(r'\[INFO\]',line)
		if len(errorlist):
			flog+=1
			y=0
			if flog%cnt[area] == 0:
				if i <= 3: 
                                        print "NO"
					command='/usr/bin/curl -d \"content=' + hostname + ' 节点有大量报错累计超过'+str(cnt[area]*i)+'次'+',报错信息为: '+line + ''
				#	os.system(command)
					i+=1
				flog=1
		if y == 500 and i == 4:
			command='/usr/bin/curl -d \"content=' + hostname + ' 监测到非Error日志连续输出操过200条 问题已经被修复,请相关人员及时确认 ' + ''
		#	os.system(command)
