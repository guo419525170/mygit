#!/bin/bash
#!/bin/sh
while true;
do
	nginx_cont=`ps -A |grep nginx |wc -l`
	if [ $nginx_cont -eq 0 ];
		then
		 nginx -c /etc/nginx/nginx.conf
	else
		echo "nginx is start" >/dev/null
	fi
	php_fpm_cont=`ps -A|grep php|wc -l`
	if [ $php_fpm_cont -eq 0 ];
		then
			/sbin/php-fpm
	else
		echo "php-fpm is start" >/dev/null
	fi
done
