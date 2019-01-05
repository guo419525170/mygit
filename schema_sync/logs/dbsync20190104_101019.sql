alter table tb_goldfield_new_year_activity add  column lastRecvDate bigint(16) COMMENT '最新领取日期(yyyymmdd)' AFTER createDate ;
alter table tb_goldfield_new_year_activity add  column days varchar(256) COMMENT '第一天领取' AFTER lastRecvDate ;
alter table tb_goldfield_new_year_activity drop column day2;
alter table tb_goldfield_new_year_activity drop column day3;
alter table tb_goldfield_new_year_activity drop column day6;
alter table tb_goldfield_new_year_activity drop column day4;
alter table tb_goldfield_new_year_activity drop column day7;
alter table tb_goldfield_new_year_activity drop column day5;
alter table tb_goldfield_new_year_activity drop column day1;
