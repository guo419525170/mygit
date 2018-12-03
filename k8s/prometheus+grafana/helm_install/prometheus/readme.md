###文档说明
###model文件夹为grafana的模板，helm安装已经自带了
###test文件夹是get -o yaml导出的文件，可以忽略


##安装说明
+ prom-alertsmanager.yaml为告警通知配置
+ prom-alertrules.yaml设置告警规则


一、安装配置prometheus

``` bash
helms install \
        --name monitor \
        --namespace monitoring \
        -f prom-settings.yaml \
        -f prom-alertsmanager.yaml \
        -f prom-alertrules.yaml \
        prometheus
 
```	  
二、安装grafana图形界面

``` bash
helms install \
	--name grafana \
	--namespace monitoring \
	-f grafana-settings.yaml \
	-f grafana-dashboards.yaml \
	grafana
 
```	  

三、管理操作
+ 升级（修改配置）：修改配置请在prom-settings.yaml prom-alertsmanager.yaml 等文件中进行，保存后执行：
# 修改prometheus
``` bash
helms upgrade monitor -f prom-settings.yaml -f prom-alertsmanager.yaml -f prom-alertrules.yaml prometheus
```
# 修改grafana
``` bash
helms upgrade grafana -f grafana-settings.yaml -f grafana-dashboards.yaml grafana
```

