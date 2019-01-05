alter table tb_user_present_reason add  column state tinyint(4) not null default1 COMMENT '0无效 1有效' AFTER updateTime ;
alter table tb_goldfield add  column protectSwitch tinyint(2) not null default0 COMMENT '是否开启新手保护' AFTER robotSwitch ;
