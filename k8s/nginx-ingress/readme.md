###说明
###本目录为nginx-ingress的安装和使用，以及配置https
+ 1、首先执行kubectl apply -f configmap-ingress.yaml ，这个文件集合了namespace以及nginx-ingress的configMap
+ 2、部署tomcat测试服务，执行kubectl apply -f deploy-tomcat.yaml
+ 3、部署nginx-ingress默认后端，执行kubectl apply -f default-backend.yaml
+ 4、部署Nginx-ingress，执行kubectl apply -f nginx-ingress.yaml，这个文件集合了对nginx-ingress的RABC授权、pod以及service
+ 5、最后部署ingrss服务，执行kubectl apply -f ingress-tomcat.yaml

+ ####为应用配置https
+ 说明: 尽管ingress可以实现暴露很少的端口，通过域名来提供多种服务，但使用https更为安全，这里将示例tomcat为https访问。

+ tomcat: 假如tomcat通过http方式已经可以访问,配置https访问如下：
+ 1、在nginx-ingress的pod添加hostNetwork网络
``` bash
spec:
      serviceAccountName: nginx-ingress-serviceaccount
      hostNetwork: true
```

+ 2、创建证书：

``` bash
openssl genrsa -out tls.key 2048
openssl req -new -x509 -key tls.key -out tls.crt -subj /CN=jtcf.tomcat.com
```

+ 3、创建secret: 
``` bash
kubectl create secret tls tomcat-ingress-secret --cert=tls.crt --key=tls.key
```
+ 4、编辑ing-tomcat.yaml文件：加上tls,然后apply


``` bash
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: ingress-tomcat
  namespace: default
  annotations:
    kubernetes.io/ingress.class: "nginx"
spec:
  tls:
  - hosts:
    - jtcf.tomcat.com
    secretName: tomcat-ingress-secret
  rules:
  - host: jtcf.tomcat.com
    http:
      paths:
      - path:
        backend:
          serviceName: tomcat
          servicePort: 8080
 
```	  
+ 通过浏览器http访问（需要添加域名解析）
    jtcf.tomcat.com:30080      

+ 通过https访问,如果没有自动重定向
    https://jtcf.tomcat.com:30443	