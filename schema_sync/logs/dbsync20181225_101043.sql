alter table tb_user_present_reason add  column state tinyint(4) not null default  1 COMMENT '0无效 1有效' AFTER updateTime ;
alter table tb_goldfield add  column protectSwitch tinyint(2) not null default  0 COMMENT '新手保护开关' AFTER robotSwitch ;
alter table tb_goldfield modify column robotSwitch tinyint(2) not null default 0 COMMENT '机器人开关' AFTER countdown ;
