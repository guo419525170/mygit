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
6、创建一个名为moniter的数据库以及alarm_info、error_info、exclusion_info三个表

CREATE TABLE `alarm_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `datetime` datetime NOT NULL,
  `hostname` varchar(128) NOT NULL,
  `error_log` longtext NOT NULL,
  `channel` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `datetime_idx` (`datetime`)
) ENGINE=InnoDB AUTO_INCREMENT=118 DEFAULT CHARSET=utf8;

CREATE TABLE `error_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `datetime` datetime NOT NULL,
  `hostname` varchar(128) NOT NULL,
  `error_log` longtext NOT NULL,
  `errortype` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `datetime_idx` (`datetime`)
) ENGINE=InnoDB AUTO_INCREMENT=2306 DEFAULT CHARSET=utf8;

CREATE TABLE `exclusion_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `error_log` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;