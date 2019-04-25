# -*- coding: utf-8 -*-
import time,sys,re,os,socket,datetime
def follow(thefile):
        thefile.seek(1,2)
        while True:
                line = thefile.readline()
                if not line:
                        time.sleep(0.1)
                        continue
                yield line

if __name__ == '__main__':
        logfile = open("/usr/local/script/moniter/test.log","r")
        loglines = follow(logfile)
	fullinfo=[]
        for line in loglines:
		typeerrorstr=re.findall(r'TypeError:.+\s+at .+\d\)',line)
		if len(typeerrorstr) > 0:
			typeerrorlist=typeerrorstr[0].split('\\n')
			print "错误类型：%s 错误详情：%s"%(typeerrorlist[0],typeerrorlist)
		errorlist=re.findall(r'(^Error:.+)|(^TypeError:.+)|(^SyntaxError:.+)|(^\s+at .+[\d|\)])',line)
		if len(errorlist) > 0:
			for info in errorlist[0]:
				if info != '':
					fullinfo.append(info)
		else:
			if len(fullinfo) > 0:
				#将错误信息入库
				print "错误类型：%s 错误详情：%s"%(fullinfo[0],fullinfo)
			fullinfo=[]
