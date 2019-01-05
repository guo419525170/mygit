alter table tb_goldfield add  column protectSwitch tinyint(2) not null default0 COMMENT '是否开启新手保护' AFTER robotSwitch ;
alter table tb_member_hide add unique key PRIMARY (memberId);
