###文档说明

##安装说明
+ prom-alertsmanager.yaml为告警通知配置
+ prom-alertrules.yaml设置告警规则


+ 安装配置


``` bash
kubectl apply -f ExtraAddons/prometheus/
kubectl apply -f ExtraAddons/prometheus/operator/

# 这边要等 operator 起來并建立好 CRDs 才能进行

kubectl apply -f ExtraAddons/prometheus/alertmanater/
kubectl apply -f ExtraAddons/prometheus/node-exporter/
kubectl apply -f ExtraAddons/prometheus/kube-state-metrics/
kubectl apply -f ExtraAddons/prometheus/grafana/
kubectl apply -f ExtraAddons/prometheus/kube-service-discovery/
kubectl apply -f ExtraAddons/prometheus/prometheus/
kubectl apply -f ExtraAddons/prometheus/servicemonitor/
```	  

