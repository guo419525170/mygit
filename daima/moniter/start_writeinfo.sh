#!/bin/sh
serverPath=$(cd `dirname $0`; pwd)
cd $serverPath
logpath='/home/jtcf/logs/'
modelist=`ls -l /home/jtcf/logs/|grep '^d'|awk '{print $NF}'`
pidlist=`ps aux|grep write_errorlog|grep -v grep|grep jtcf|awk '{print $2}'`
for pid in $pidlist
do
	kill -9 $pid
done
for mode in $modelist
do
	file=${logpath}${mode}/`date +%Y%m%d`.txt
	if [ -f $file ]
	then
		nohup python /data/shell/moniter/write_errorlog.py $file $mode & 
	fi
done
