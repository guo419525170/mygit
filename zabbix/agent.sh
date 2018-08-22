#!/bin/bash
#获取客户端IP
agentIP=`ifconfig eth0|awk 'NR==2{print$2}'`
####填写zabbix服务端IP
serverIP=10.28.143.239
###安装客户端
rpm -ivh http://repo.zabbix.com/zabbix/3.4/rhel/7/x86_64/zabbix-release-3.4-2.el7.noarch.rpm
yum install zabbix-agent  -y    
###默认为0，改为1以后，表示用户自定义的脚本中可以包含特殊字符
sed -i 's@# UnsafeUserParameters=0@UnsafeUserParameters=1@g' /etc/zabbix/zabbix_agentd.conf
####修改hostname注意：Hostname应该和web监控配置主机名称一样
sed -i "s#Hostname=Zabbix server#Hostname=$(hostname)#g" /etc/zabbix/zabbix_agentd.conf
#####填写服务端IP
sed -i "s#Server=127.0.0.1#Server=$serverIP#g" /etc/zabbix/zabbix_agentd.conf
#####填写本机IP
sed -i "s@# SourceIP=@SourceIP=$agentIP@g" /etc/zabbix/zabbix_agentd.conf
####客户端监听端口
sed -i 's/# ListenPort/ListenPort/g' /etc/zabbix/zabbix_agentd.conf
####配置客户端自动发现
sed -i "s/ServerActive=127.0.0.1/ServerActive=$serverIP/g" /etc/zabbix/zabbix_agentd.conf
##########启动客户端并且加入开机启动，
service zabbix-agent start
chkconfig zabbix-agent on
