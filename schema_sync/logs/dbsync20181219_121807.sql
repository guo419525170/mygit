alter table tb_activity_config_copy add  column endTime bigint(16) not null COMMENT '' AFTER startTime ;
alter table tb_activity_config_copy add  column action tinyint(2) COMMENT '0无，1跳转商城，2跳转网页，3分享' AFTER content ;
alter table tb_activity_config_copy add  column xiaoyu tinyint(2) COMMENT '' AFTER target ;
alter table tb_activity_config_copy add  key index_end_time(endTime);
