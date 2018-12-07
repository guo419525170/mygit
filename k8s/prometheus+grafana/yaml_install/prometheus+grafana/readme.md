###文档说明

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

+ 告警通知没设置
+ 配置文件在alertmanater的config目录