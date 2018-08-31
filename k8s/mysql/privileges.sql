use mysql;
select host, user from user;
-- 因为mysql版本是5.7，因此新建用户为如下命令：
--create user qjadmin identified by 'Qjclouds.com';
grant all on *.* to root@'%' identified by '123456' with grant option;
flush privileges;
--source /var/lib/mysql/qjpaas-all.sql
