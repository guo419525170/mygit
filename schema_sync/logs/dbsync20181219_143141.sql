alter table tb_activity_config_copy add  column startTime bigint(16) not null COMMENT '' AFTER conditions ;
alter table tb_activity_config_copy add  column endTime bigint(16) not null COMMENT '' AFTER startTime ;
alter table tb_activity_config_copy add  key index_start_time(startTime);
alter table tb_activity_config_copy add  key index_end_time(endTime);
