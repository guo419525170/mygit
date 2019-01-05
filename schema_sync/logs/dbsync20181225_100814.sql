alter table tb_goldfield add  column protectSwitch tinyint(2) not null default  0 COMMENT '新手保护开关' AFTER robotSwitch ;
alter table tb_goldfield modify column robotSwitch tinyint(2) not null default 0 COMMENT '机器人开关' AFTER countdown ;
