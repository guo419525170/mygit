摘要：
1、  日志收集
通过脚本write_errorlog.py收集错误日志，并写入数据库，脚本部署在各个服务器，日志目录在conf.py
/usr/bin/python /data/shell/moniter/write_errorlog.py
2、，web显示日志
在堡垒机部署web接口showwebnew.py脚本，并且配置nginx用于web显示错误日志，主要内容在web文件夹
/bin/python showwebnew.py 8388
3、告警系统
在web服务器部署告警脚本alarm.py，写入计划任务，每分钟读取mysql中的错误日志，错误日志达到指定次数就发送钉钉或者微信告警
*/1 * * * * /usr/bin/python /data/shell/moniter/alarm.py > /data/shell/moniter/alarm.txt 2>&1
4、配置文件
在各个服务器配置conf.py脚本，alarm.py、 showwebnew.py和write_errorlog.py需要引用该模块
5、nginx配置文件在web目录