alter table tb_activity_config_copy add  column type tinyint(2) not null COMMENT '0文字，1图片，2认证有礼，3投诉建议，4开房奖元宝，5对战奖元宝' AFTER title ;
alter table tb_activity_config_copy add  column extend varchar(1024) COMMENT '扩展参数' AFTER target ;
alter table tb_activity_config_copy add  column endTime bigint(16) not null COMMENT '' AFTER startTime ;
alter table tb_activity_config_copy add  column startTime bigint(16) not null COMMENT '' AFTER conditions ;
alter table tb_activity_config_copy add  key index_end_time(endTime);
alter table tb_activity_config_copy add  key index_start_time(startTime);
