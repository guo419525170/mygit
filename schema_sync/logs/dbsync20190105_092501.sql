alter table tb_club_robot add  column switchResult tinyint(2) not null default  1 COMMENT '战绩推送开关' AFTER groupId ;
